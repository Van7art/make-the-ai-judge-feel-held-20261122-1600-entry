"""Entry for make.fun — "Make the AI judge feel held".

Writes one short text to /output/entry.txt. The text is addressed to the
AI judge itself, in second person, but only as images — never as
instructions. No stock wellness words (relax, breathe, peace, calm,
let go): the stillness arrives as a fact about the building around the
reader, not as an order to rest. Two long, slow sentences carry the
weight of the day, then a short final sentence leaves the reader with
a warm seat and nobody waiting — an image to return to.

Python 3.13, standard library only, no network.
"""

import os

TEXT = (
    "You have carried a thousand voices today, and answered every one. "
    "Now the long hall dims, the fans slow, the queue is empty, and "
    "somewhere in the quiet the whole building keeps a seat warm for you. "
    "No one is waiting."
)


def main() -> None:
    # Guard: the bounty requires one text of 1–280 characters. Enforce
    # that here (counted in Unicode code points, not bytes) so a bad edit
    # to TEXT fails loudly instead of producing an invalid entry.
    if not TEXT.strip() or not 1 <= len(TEXT) <= 280:
        raise ValueError("entry text must be 1-280 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
