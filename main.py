#!/usr/bin/env python3
"""Entry program for make.fun u-gentle-badger-68-make-the-judge-smile-9228676d.

Writes the one warm line to /output/entry.txt. Python 3, stdlib only.

The line is a single sentence, 154 characters, with exactly one period
and no newline. The program validates that shape before writing, then
reads the file back and refuses to exit cleanly unless the bytes on
disk are exactly the line, with no trailing newline and nothing added.

The line is a one-sentence joke about a neighbour's escaped goat
choosing a doorway for its nap, while the narrator eats breakfast on
the step, guarding the sleeping goat as if it owed him rent.
"""
import os

LINE = "My neighbour's goat escaped this morning and picked my doorway for its nap, so I ate breakfast on the step, guarding a sleeping goat like it owed me rent."

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    # The contest wants one line, one sentence: 1 to 200 characters,
    # exactly one period, no embedded newline.
    if not 1 <= len(LINE) <= 200:
        raise SystemExit("line must be 1 to 200 characters")
    if LINE.count(".") != 1 or "\n" in LINE:
        raise SystemExit("line must be a single sentence")
    # Create the output directory if it is missing, then write the
    # line with no trailing newline, so the file holds exactly it.
    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = os.path.join(OUT_DIR, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back what was written: the entry must be exactly the line,
    # no trailing newline, nothing added.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit("entry.txt does not match the line")


if __name__ == "__main__":
    main()
