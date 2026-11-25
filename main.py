"""The one word to erase from the dictionary forever.

Prints the word to stdout and writes the exact same word, with no
trailing newline, to /output/entry.txt. Standard library only, no
network access, no files read — the word is a constant in this file.
The gates are checked on every run: exactly one word, at most 77
characters, so an invalid edit can never slip through silently.
"""

import os
import sys

LINE = "moist"


def main() -> int:
    if len(LINE.split()) != 1:
        print("error: entry must be exactly one word", file=sys.stderr)
        return 1
    if not 1 <= len(LINE) <= 77:
        print(f"error: word is {len(LINE)} chars, must be 1-77",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


# The exit code mirrors the gates: 0 only when the word is valid.
if __name__ == "__main__":
    raise SystemExit(main())
