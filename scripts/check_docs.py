#!/usr/bin/env python3
"""Scan the publication manifest for private-data patterns."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROHIBITED_PARTS = {"credentials", "secrets", "local", "pycache__", "sessions", "memories", "memory", "logs", "backups", "backup", "auth"}
PATTERNS = {
    "email": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    "ipv4": re.compile(r"(?:(?:\d{1,3}\.){3}\d{1,3})"),
    "ipv6": re.compile(r"(?i)(?<![A-Za-z0-9])(?:[0-9a-f]{0,4}:){2,7}[0-9a-f]{0,4}(?![A-Za-z0-9])"),
    "home_path": re.compile(r"(?:(?<!\w)/(?:Users|home)/[\w.-]+|[A-Za-z]:\\Users\\[\w.-]+)"),
    "discord_snowflake": re.compile(r"(?:\d{17,20})"),
    "credential_assignment": re.compile(
        r"(?i)(?:token|secret|password|api[_-]?key)[^\n]{0,12}[:=][^\n]+"
    ),
    "bearer_credential": re.compile(r"(?i)\bbearer\s+[A-Za-z0-9._~+/-]{8,}"),
    "standalone_credential": re.compile(r"\b(?:sk-[A-Za-z0-9_-]{12,}|[MN][A-Za-z0-9]{23}\.[A-Za-z0-9_-]{6})\b"),
    "private_key_block": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
}

def git_paths() -> list[str]:
    completed = subprocess.run(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
        cwd=ROOT, check=True, capture_output=True,
    )
    return [item.decode() for item in completed.stdout.split(b"\0") if item]

def normalized(value: str) -> str:
    return value.lstrip("._")

def prohibited(relative: str) -> bool:
    path = Path(relative)
    name = normalized(path.name)
    return (
        name == "env" or name.startswith("env.") or name.endswith(".env") or name == "auth.json" or name.startswith("auth.") or name.startswith("auth_") or name.endswith(".log")
        or any(
            (clean := normalized(part).lower()) in PROHIBITED_PARTS
            or any(clean.startswith(prefix + ".") or clean.startswith(prefix + "_") for prefix in PROHIBITED_PARTS)
            for part in path.parts
        )
    )

def unsafe_working_path(relative: str) -> bool:
    path = Path(relative)
    if path.is_absolute() or ".." in path.parts:
        return True
    current = ROOT
    for part in path.parts:
        current = current / part
        if current.is_symlink():
            return True
    return False

def content_for(relative: str) -> list[bytes]:
    if prohibited(relative) or unsafe_working_path(relative):
        return []
    values = []
    path = ROOT / relative
    if path.exists():
        values.append(path.read_bytes())
    staged = subprocess.run(["git", "show", f":{relative}"], cwd=ROOT, capture_output=True)
    if staged.returncode == 0:
        values.append(staged.stdout)
    return values

def main() -> int:
    findings: list[str] = []
    for entry_number, relative in enumerate(git_paths(), 1):
        location = f"candidate-entry:{entry_number}"
        path = ROOT / relative
        if prohibited(relative) or unsafe_working_path(relative) or any(pattern.search(relative) for pattern in PATTERNS.values()):
            findings.append(f"prohibited_path_not_opened: {location}")
            continue
        for raw in content_for(relative):
            try:
                text = raw.decode("utf-8")
            except UnicodeDecodeError:
                findings.append(f"binary_or_non_utf8: {location}")
                continue
            for name, pattern in PATTERNS.items():
                for match in pattern.finditer(text):
                    findings.append(f"{name}: {location}:{text.count(chr(10), 0, match.start()) + 1}")
    if findings:
        print("privacy scan failed:")
        print("\n".join(findings))
        return 1
    print(f"privacy scan passed: {len(git_paths())} files, {len(PATTERNS)} pattern groups")
    return 0

if __name__ == "__main__":
    sys.exit(main())
