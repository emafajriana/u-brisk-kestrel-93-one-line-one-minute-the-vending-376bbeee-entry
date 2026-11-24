"""Vending machine pickup line entry (Python 3.13, standard library only).

The program writes one pickup line, spoken by the vending machine
itself, to the output directory as entry.txt. The sealed gate wants
UTF-8 text of 1 to 200 characters, not only white space.
"""

import os
from pathlib import Path

LINE = (
    "Press B7 \u2014 I've been humming your name since you walked in, "
    "and my coil only gets stuck on the good ones."
)

FILE_NAME = "entry.txt"


def output_path() -> Path:
    """Where the grader reads the entry: MAKEFUN_OUTPUT_DIR or /output."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return out_dir / FILE_NAME


def check_gate(text: str) -> None:
    """Enforce the sealed gate ourselves: 1 to 200 chars, not blank."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} chars, gate wants 1-200")
    if not text.strip():
        raise ValueError("entry is only white space")


def main() -> None:
    check_gate(LINE)
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE, encoding="utf-8")
    written = target.read_text(encoding="utf-8")
    if written != LINE:
        raise IOError("read-back text differs from the entry line")
    print(f"wrote {target} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
