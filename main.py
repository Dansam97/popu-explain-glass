"""Entry program for make.fun bounty
u-po-pu-five-seconds-to-explain-the-glass-934d9949
("Five Seconds to Explain the Glass").

Writes the house cat's one-sentence defence to entry.txt in the
output directory: no apology, no confession, just the cat's case.
"""

import os

ENTRY = (
    "You keep putting it exactly where my paw lands, so I keep removing it "
    "\u2014 one of us is being trained here, and it is not me."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
