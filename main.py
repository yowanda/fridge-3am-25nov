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
    # Runtime validation: exactly one line of UTF-8 text, 1-140 chars,
    # not whitespace-only. Raises before writing anything.
    if "\n" in TEXT or "\r" in TEXT:
        raise ValueError("entry text must be a single line")
    if not TEXT.strip():
        raise ValueError("entry text must not be whitespace-only")
    if not 1 <= len(TEXT) <= 140:
        raise ValueError(f"entry text length {len(TEXT)} outside 1-140 chars")
    data = TEXT.encode("utf-8")  # raises UnicodeEncodeError if not UTF-8
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
