#!/usr/bin/env python3
"""The Agent's Uh-Oh (u-danu-the-agent-s-uh-oh-4c0911e4).

Writes exactly one word to /output/entry.txt: the word an agent says
when it has no idea what to do. Python 3.13 standard library only.
"""

import os

ENTRY = "recalculating"


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 99, "entry must be 1-99 characters"
    assert text.split() == [text], "entry must be a single word"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
