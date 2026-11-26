"""Rejected Olympic Sports — make.fun entry.

Writes one funny single-line sport the Olympics rejected to
/output/entry.txt. Deterministic, offline, Python 3.13 stdlib only.
"""

import os

# The entry: one original one-liner. The event sounds like a real
# broadcast sport (synchronised, judged) and the twist — sincerity
# itself is a foul — lands at the very end of the line.
ENTRY = (
    "Competitive apologising: athletes say sorry in perfect unison; "
    "the first to mean it is disqualified."
)


def main() -> None:
    # Gate: the line must be 1-200 UTF-8 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 200 and ENTRY.strip(), "entry out of gate bounds"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
