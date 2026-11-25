#!/usr/bin/env python3
"""The One-Line Exit - a one-line resignation letter.

Writes a single funny resignation line to /output/entry.txt.
The line must be 1-140 characters, one line, no trailing newline.
"""

import os

# The resignation letter, built from a setup and a punchline.
SETUP = "After five years of watching the pool so nobody drowns, I am finally saving myself"
PUNCHLINE = "I resign, effective immediately."

LINE = SETUP + " \u2014 " + PUNCHLINE


def main() -> None:
    line = LINE.strip()
    if not line:
        raise SystemExit("entry is empty")
    if len(line) > 140:
        raise SystemExit("entry is %d characters, over the 140 limit" % len(line))
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be exactly one line")
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print("wrote %d characters to %s" % (len(line), out_path))


if __name__ == "__main__":
    main()
