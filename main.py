"""One-line entry for u-coral-404-one-line-big-laugh-328fb857.

Writes a single hilarious line to entry.txt in the output directory
given by MAKEFUN_OUTPUT_DIR (default "/output").
"""

import hashlib
import os

# The joke: deadpan setup ("called me brave") -> ironic twist -> one
# absurdly specific detail, with a digit ("4 hours") as the concrete
# second beat, so the number hits harder than the spelled-out word.
JOKE_LINE = (
    "My phone's screen-time report called me brave, then showed I spent "
    "4 hours watching a man restore a rusty shovel in complete silence."
)

MAX_LINE_CHARS = 200


def build_output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    line = JOKE_LINE
    if not line.strip():
        raise ValueError("line must not be empty or only whitespace")
    if len(line) > MAX_LINE_CHARS:
        raise ValueError(
            f"line is {len(line)} chars, over the {MAX_LINE_CHARS} limit"
        )
    target = build_output_path()
    os.makedirs(os.path.dirname(target) or ".", exist_ok=True)
    # No trailing newline: write exactly the line bytes, UTF-8.
    with open(target, "wb") as handle:
        handle.write(line.encode("utf-8"))
    print(f"wrote {len(line)} chars to {target}")


if __name__ == "__main__":
    main()
