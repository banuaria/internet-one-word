"""The Internet in One Word.

Writes a single word describing the whole internet to entry.txt in the
output directory ($MAKEFUN_OUTPUT_DIR, default /output). Standard library
only, no network, same output every run.
"""

import os

WORD = "Pantsless"


def validate(word: str) -> str:
    """Return word if it is 1-30 characters and not only white space."""
    if not 1 <= len(word) <= 30:
        raise ValueError(f"word must be 1-30 characters, got {len(word)}")
    if not word.strip():
        raise ValueError("word must not be blank")
    return word


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(validate(WORD))


if __name__ == "__main__":
    main()
