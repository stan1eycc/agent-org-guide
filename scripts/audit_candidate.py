#!/usr/bin/env python3
"""Audit working files and every local Git object; never print matched values."""
import ast
import importlib.util
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("guide_scan", ROOT / "scripts" / "check_docs.py")
assert spec is not None and spec.loader is not None
scan = importlib.util.module_from_spec(spec)
spec.loader.exec_module(scan)
EXTRA = {
    "github_credential": re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b"),
    "cookie_assignment": re.compile(r"(?i)\bcookie\s*[:=]\s*[A-Za-z0-9_]{8,}"),
}
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
URL = re.compile(r"https?://[^\s<>\"')`]+")
DOMAIN = re.compile(r"\b(?:[A-Za-z0-9-]+\.)+(?:com|org|net|io|ai|local|lan|dev)\b", re.I)
ALLOWED_DOMAINS = {".".join(parts) for parts in [
    ("hermes-agent", "nousresearch", "com"), ("github", "com"),
    ("usemagpie", "ai"), ("openrouter", "ai"),
    ("raw", "githubusercontent", "com"), ("hindsight", "vectorize", "io"),
]}


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, check=True).stdout


def findings(raw, location, domains=False):
    result = []
    try:
        text = raw.decode("utf-8")
    except UnicodeError:
        return [{"category": "opaque_payload", "location": location}]
    for category, regex in {**scan.PATTERNS, **EXTRA}.items():
        for match in regex.finditer(text):
            result.append({"category": category, "location": f"{location}:{text.count(chr(10), 0, match.start()) + 1}"})
    if domains:
        # Domain substrings inside source URLs are source citations; unrelated prose domains are flagged.
        cleaned = URL.sub("", text)
        for match in DOMAIN.finditer(cleaned):
            result.append({"category": "domain_outside_citation", "location": f"{location}:{cleaned.count(chr(10), 0, match.start()) + 1}"})
        for url in URL.findall(text):
            from urllib.parse import urlsplit
            if urlsplit(url).hostname not in ALLOWED_DOMAINS:
                result.append({"category": "unreviewed_url_domain", "location": location})
    return result


def audit():
    issues = []
    files = []
    metadata = []
    entry_number = 0
    for current, dirs, names in os.walk(ROOT, followlinks=False):
        if Path(current) == ROOT and ".git" in dirs:
            dirs.remove(".git")  # Git payloads are enumerated below, not silently exempted.
        for name in list(dirs):
            p = Path(current) / name
            if p.is_symlink() or scan.prohibited(p.relative_to(ROOT).as_posix()):
                issues.append({"category": "protected_or_symlink_directory_not_opened", "location": "working-directory-entry"})
                dirs.remove(name)
        for name in names:
            p = Path(current) / name
            rel = p.relative_to(ROOT).as_posix()
            entry_number += 1
            location = f"working-entry:{entry_number}"
            if scan.prohibited(rel) or findings(rel.encode(), location, domains=True):
                issues.append({"category": "prohibited_path_not_opened", "location": location})
                continue
            if not stat.S_ISREG(p.lstat().st_mode) or p.is_symlink():
                issues.append({"category": "nonregular_file", "location": location})
                continue
            files.append(rel)
            if (list_attrs := getattr(os, "listxattr", None)) is not None and list_attrs(p, follow_symlinks=False):
                metadata.append({"category": "extended_attributes", "location": location})
            if p.suffix not in {".md", ".py", ".json"} and name not in {"LICENSE", ".gitignore"}:
                issues.append({"category": "unreviewed_file_type", "location": location})
            raw = p.read_bytes()
            issues.extend(findings(raw, location, domains=True))
            try:
                text = raw.decode("utf-8")
            except UnicodeError:
                continue
            if p.suffix == ".py":
                try:
                    ast.parse(text)
                except SyntaxError:
                    issues.append({"category": "invalid_python", "location": location})
            if p.suffix == ".json":
                try:
                    json.loads(text)
                except ValueError:
                    issues.append({"category": "invalid_json", "location": location})
            if p.suffix == ".md":
                for target in LINK.findall(text):
                    if target.startswith(("https://", "http://", "#")):
                        continue
                    dest = (p.parent / target.split("#", 1)[0]).resolve()
                    if not dest.is_relative_to(ROOT) or not dest.exists():
                        issues.append({"category": "broken_local_link", "location": location})
    objects = git("cat-file", "--batch-all-objects", "--batch-check=%(objectname) %(objecttype)").decode().splitlines()
    # Inventory paths before opening any blob. Unknown/unbound objects are not opened.
    known_blobs = set()
    blocked_blobs = set()
    for entry in objects:
        tree_oid, kind = entry.split()
        if kind != "tree":
            continue
        for record in git("ls-tree", "-r", "-z", tree_oid).split(b"\0"):
            if not record:
                continue
            header, path = record.split(b"\t", 1)
            mode, object_kind, blob_oid = header.decode().split()
            if object_kind != "blob":
                continue
            known_blobs.add(blob_oid)
            if scan.prohibited(path.decode()) or findings(path, "history-path") or mode == "120000":
                blocked_blobs.add(blob_oid)
                issues.append({"category": "prohibited_history_path_not_opened", "location": f"git-tree:{tree_oid}"})
    reachable = {line.split()[0] for line in git("rev-list", "--objects", "--all").decode().splitlines()}
    for entry in git("ls-files", "--stage", "-z").split(b"\0"):
        if not entry:
            continue
        header, path = entry.split(b"\t", 1)
        mode, blob_oid, _ = header.decode().split()
        known_blobs.add(blob_oid)
        reachable.add(blob_oid)
        if scan.prohibited(path.decode()) or findings(path, "index-path") or mode == "120000":
            blocked_blobs.add(blob_oid)
            issues.append({"category": "prohibited_index_path_not_opened", "location": "git-index"})
    blobs = commits = tags = 0
    historical_metadata = []
    local_only_unbound = []
    for entry in objects:
        oid, kind = entry.split()
        if kind not in {"blob", "commit", "tag"}:
            continue
        if kind == "blob" and (oid in blocked_blobs or oid not in known_blobs):
            finding = {"category": "blocked_or_unbound_blob_not_opened", "location": f"git-blob:{oid}"}
            if oid not in reachable and oid not in known_blobs:
                # An unreferenced local object is not sent by a normal explicit ref push.
                # Inventory it without reading, deleting or claiming it content-scanned.
                local_only_unbound.append(finding)
            else:
                issues.append(finding)
            continue
        raw = git("cat-file", kind, oid)
        if kind == "blob":
            blobs += 1
            issues.extend(findings(raw, f"git-blob:{oid}"))
        else:
            commits += kind == "commit"
            tags += kind == "tag"
            header, _, body = raw.partition(b"\n\n")
            issues.extend(findings(body, f"git-{kind}-message:{oid}"))
            for line in header.splitlines():
                if line.startswith((b"author ", b"committer ", b"tagger ")):
                    historical_metadata.append({"category": "existing_public_git_identity", "location": f"git-{kind}:{oid}"})
    return {"working_files": len(files), "pattern_groups": len(scan.PATTERNS) + len(EXTRA),
            "git_blobs": blobs, "git_commits": commits, "git_tags": tags,
            "git_scope": "all objects inventoried; path-bound blobs scanned; blocked/reachable unknown blobs fail; unreferenced unbound objects reported without reading",
            "working_scope": "all files including ignored/hidden; credential-like paths refused without reading",
            "findings": issues, "metadata_review": metadata,
            "existing_public_identity_records": historical_metadata,
            "unreferenced_local_objects_not_opened_or_pushed": local_only_unbound,
            "limitations": "Manual semantic/name review still required; existing public identity is not newly introduced or erased."}


if __name__ == "__main__":
    try:
        report = audit()
    except (OSError, subprocess.CalledProcessError, ValueError):
        print(json.dumps({"error": "audit_failed_without_raw_diagnostics"}))
        sys.exit(1)
    print(json.dumps(report, indent=2))
    sys.exit(bool(report["findings"] or report["metadata_review"]))
