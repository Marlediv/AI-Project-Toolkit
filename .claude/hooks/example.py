#!/usr/bin/env python3

"""
Example Claude Code hook.

PURPOSE

This file demonstrates where project-specific Claude Code hook
implementations can live.

It is intentionally NOT enabled by default.

Claude Code hooks are configured through .claude/settings.json.
Keeping this example disabled ensures that creating a project from this
template does not automatically execute project-provided code.

When creating a project from this template:

1. Copy or rename this file for a concrete hook.
2. Implement the required behavior.
3. Configure the hook explicitly in .claude/settings.json.
4. Test the hook independently before enabling it.
5. Remove this example if the project does not require hooks.

Hooks should automate small, predictable lifecycle actions.
They should not become another source of project knowledge.

Shared project knowledge belongs in docs/.
General Claude Code instructions belong in CLAUDE.md.
"""

import json
import sys
from typing import Any


def read_input() -> dict[str, Any]:
    """
    Read the hook input from standard input.

    Claude Code hooks may receive structured input through stdin.
    A real hook should validate the fields it actually requires.
    """

    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        raise ValueError("Hook input is not valid JSON.") from exc

    if not isinstance(data, dict):
        raise ValueError("Hook input must be a JSON object.")

    return data


def main() -> int:
    """
    Example no-op hook.

    This implementation intentionally performs no project action and
    modifies no files or external systems.

    Replace this function with concrete hook behavior when creating an
    actual project hook.
    """

    _hook_input = read_input()

    # Intentionally no operation.
    #
    # A real hook may inspect the received event and produce the output
    # required by the corresponding Claude Code hook contract.
    #
    # Consult the current Claude Code hook documentation before
    # implementing event-specific input or output behavior.

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValueError as exc:
        print(f"Hook error: {exc}", file=sys.stderr)
        raise SystemExit(1)