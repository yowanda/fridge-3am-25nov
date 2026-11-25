#!/usr/bin/env python3
"""The 3AM Fridge Text — the one line a smart fridge texts its owner at 3am.

Deterministic, standard library only, no network. Writes a single line of
UTF-8 text to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when the
variable is unset), with no trailing newline so the file holds exactly the
text and nothing else.
"""

import os

TEXT = (
    "It's 3am. You opened me, stared into the light like it owed you "
    "answers, then took a pickle. Just one pickle."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
