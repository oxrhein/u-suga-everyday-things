"""Everyday Things, Two Lines, Longer Run - make.fun entry.

Writes a two-line explanation of a toaster to entry.txt: line 1 explains
it to a 10-year-old through one vivid analogy, line 2 says honestly what
that analogy maps and what it leaves out.
Stdlib only, no network, deterministic.
"""

import os

# Two lines, 251 characters total. The gate (RULES.txt) allows 1-400.
LINE_1 = "A toaster is a tiny lift that drops your bread into a hot basement and brings it back up brown and crunchy."
LINE_2 = "The lift explains the ride down and back up, but it leaves out the glowing wires that do the cooking \u2014 a real lift never toasts its passengers."

ENTRY = LINE_1 + "\n" + LINE_2 + "\n"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
