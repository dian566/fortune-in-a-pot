#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Fortune in a Pot — make.fun entry writer.
# Running this script produces exactly one line in /output/entry.txt.

from pathlib import Path

TEXT = "Good news: you will outgrow this pot. Bad news: your human still waters you like a rumor."
TARGET = Path("/output/entry.txt")
LIMIT = 120


def main() -> None:
    line = TEXT.strip()
    assert line, "entry may not be empty"
    assert len(line) <= LIMIT, "entry exceeds 120 characters"
    assert "\n" not in line and "\r" not in line, "entry must stay on one line"
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
