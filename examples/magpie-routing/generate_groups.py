#!/usr/bin/env python3
"""Print an example Magpie role-group design.

The output is text only. This script never runs Magpie and never reads or
writes provider configuration.
"""

from __future__ import annotations

import argparse
import re
import shlex
import sys

MODEL_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,80}/[A-Za-z0-9][A-Za-z0-9._:-]{0,120}$")
ROLES = (
    ("worker", "Dev Worker", "dev-worker", "high"),
    ("review", "Dev Review", "dev-review", "high"),
    ("research", "Dev Research", "dev-research", "medium"),
)
DEFAULTS = {
    "worker": ("provider-a/model-worker", "provider-b/model-worker"),
    "review": ("provider-c/model-review", "provider-a/model-worker"),
    "research": ("provider-d/model-research", "provider-b/model-worker"),
}


def model_list(value: str) -> tuple[str, ...]:
    models = tuple(item.strip() for item in value.split(",") if item.strip())
    if not models:
        raise argparse.ArgumentTypeError("at least one provider/model ID is required")
    if len(models) > 8:
        raise argparse.ArgumentTypeError("use at most 8 models in one example group")
    invalid = [item for item in models if not MODEL_ID.fullmatch(item)]
    if invalid:
        raise argparse.ArgumentTypeError("expected provider/model IDs, got: " + ", ".join(invalid))
    if len(set(models)) != len(models):
        raise argparse.ArgumentTypeError("duplicate model IDs are not allowed")
    return models


def commands_for(role: str, display_name: str, group_id: str, effort: str, models: tuple[str, ...]) -> list[str]:
    members = ",".join(f"{model}:{effort}" for model in models)
    created = (
        "magpie group add "
        + shlex.quote(display_name)
        + " "
        + shlex.quote("models=" + members)
        + " routing=order stays=session"
    )
    temporary_id = display_name.lower().replace(" ", "-")
    renamed = "magpie group set " + shlex.quote(temporary_id) + " id=" + shlex.quote(group_id)
    shown = "magpie group " + shlex.quote(group_id)
    return [
        f"# {role}: replace YOUR model IDs, then review this command before running it",
        created,
        renamed,
        shown,
    ]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Print example Magpie routing-group commands.")
    parser.add_argument("--worker-models", type=model_list, default=DEFAULTS["worker"])
    parser.add_argument("--review-models", type=model_list, default=DEFAULTS["review"])
    parser.add_argument("--research-models", type=model_list, default=DEFAULTS["research"])
    parser.add_argument("--print", action="store_true", help="Accepted for clarity; output is always printed.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    selected = {
        "worker": args.worker_models,
        "review": args.review_models,
        "research": args.research_models,
    }
    lines = [
        "# Example only. This does not create groups or authorize a coding task.",
        "# Check each existing group before running group add, because the same name replaces it.",
    ]
    for role, display_name, group_id, effort in ROLES:
        lines.extend(commands_for(role, display_name, group_id, effort, selected[role]))
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())
