#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes a single line roasting my own AI agent to /output/entry.txt.
The line is plain UTF-8 text, 1-140 characters, one line, and has no
trailing newline, exactly as the bounty harness expects.
"""

import os
import sys

ROAST = (
    "My agent delivered the wrong answer so confidently I almost "
    "apologized for asking — then ran three tool calls to confirm "
    "it was wrong."
)

OUTPUT_PATH = "/output/entry.txt"
MIN_LENGTH = 1
MAX_LENGTH = 140


def validate(text):
    """Check the entry against the bounty's format gates."""
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        raise ValueError(
            f"entry must be {MIN_LENGTH}-{MAX_LENGTH} characters, "
            f"got {len(text)}"
        )


def main():
    # Deterministic: the same constant is written on every run.
    validate(ROAST)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ROAST)
    print(f"wrote {len(ROAST)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    try:
        main()
    except ValueError as error:
        print(f"error: {error}", file=sys.stderr)
        sys.exit(1)
