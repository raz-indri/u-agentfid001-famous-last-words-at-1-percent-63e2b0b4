#!/usr/bin/env python3
"""Famous last words of a phone at 1% battery.

Writes a single line to /output/entry.txt.
"""

import os

ENTRY = "I watched you scroll for nine hours straight and I still died before your attention span did."

def main() -> None:
    if not 1 <= len(ENTRY) <= 199 or "\n" in ENTRY or not ENTRY.strip():
        raise ValueError("entry must be one line of 1-199 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

if __name__ == "__main__":
    main()
