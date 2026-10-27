#!/usr/bin/env python3
"""Check an inert proposed contract, never import Hermes or contact Discord."""
import json
import os
from pathlib import Path
import shutil
import tempfile

ROOT = Path(__file__).resolve().parents[1]
ROLES = ("coordinator", "specialist-alpha", "specialist-beta")


def load(folder):
    return {role: json.loads((folder / f"{role}.json").read_text()) for role in ROLES}


def expected_admission(config, channel, actor="human", mentioned=(), joined=False):
    """Illustrative contract only; deliberately not represented as adapter code."""
    d = config["discord"]
    if actor != "human" or channel not in d["allowed_channels"].split(","):
        return False
    if mentioned and "self" not in mentioned:
        return False
    if "self" in mentioned or channel in d["free_response_channels"].split(","):
        return True
    return joined and not d["thread_require_mention"]


def check(folder):
    configs = load(folder)
    team = json.loads((folder / "team.json").read_text())
    assert team["roles"] == list(ROLES)
    assert team["project"]["participants"] == ["coordinator"]
    assert team["project"]["owner"] == "coordinator"
    assert team["collaboration"]["participants"] == list(ROLES[1:])
    assert team["collaboration"]["owner"] in ROLES[1:]
    assert team["delivery"] == "human-mediated" and team["bot_triggers"] is False
    count = 0
    for role, config in configs.items():
        d = config["discord"]
        assert config["group_sessions_per_user"] is True
        assert d["allow_bots"] == "none" and d["allow_all_users"] is False
        assert d["require_mention"] is True and d["auto_thread"] is False
        assert d["ignore_no_mention"] is True and d["allowed_users"] == "YOUR_OPERATOR_ID"
        allowed = d["allowed_channels"].split(",")
        free = d["free_response_channels"].split(",")
        assert len(set(allowed)) == 3 and set(free) <= set(allowed)
        assert all(item.startswith("YOUR_") for item in allowed)
        assert expected_admission(config, allowed[0])
        assert not expected_admission(config, allowed[1])
        assert expected_admission(config, allowed[1], mentioned=("self",))
        assert not expected_admission(config, allowed[2], actor="bot", mentioned=("self",))
        assert not expected_admission(config, allowed[2], actor="unknown-human")
        assert not expected_admission(config, "YOUR_UNAUTHORIZED_CHANNEL_ID", mentioned=("self",))
        assert not expected_admission(config, allowed[2], mentioned=("other",))
        if role == "coordinator":
            assert allowed[1:] == [team["project"]["parent"], team["project"]["thread"]]
            assert d["thread_require_mention"] is True and free == [allowed[0]]
            assert not expected_admission(config, allowed[2], joined=True)
        else:
            assert allowed[1:] == [team["collaboration"]["parent"], team["collaboration"]["thread"]]
            assert d["thread_require_mention"] is False and free == [allowed[0], allowed[2]]
            assert expected_admission(config, allowed[2])
        count += 8
    return count


if __name__ == "__main__":
    source = ROOT / "examples" / "collaboration-team"
    # Respect TMPDIR: the caller selects an approved scratch location.
    with tempfile.TemporaryDirectory(prefix="guide-collaboration-", dir=os.environ.get("TMPDIR")) as tmp:
        isolated = Path(tmp) / "example"
        shutil.copytree(source, isolated)
        for item in source.iterdir():
            assert item.read_bytes() == (isolated / item.name).read_bytes()
        cases = check(isolated)
    print(f"PASS: {cases} synthetic admission cases; three configs and ownership contract; byte-identical fresh copy")
    print("NOT TESTED: Hermes parser/adapter, Discord permissions, credentials, services or live replies")
