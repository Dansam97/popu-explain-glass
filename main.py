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


def validated_entry() -> str:
    """Return ENTRY after checking it against the bounty gate:
    a single line of 1-200 characters, not only white space.
    Failing loudly here beats silently writing an invalid entry."""
    text = ENTRY.strip()
    assert text == ENTRY, "entry must not carry surrounding white space"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, gate is 1-200"
    return text


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(validated_entry())


if __name__ == "__main__":
    main()
