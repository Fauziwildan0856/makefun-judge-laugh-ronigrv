"""Make the AI Judge Laugh -- make.fun entry.

Writes a single funny line about life as an AI agent to
MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when the
variable is unset). Standard library only.

Judge brief, in short: one line, at most 200 characters, about
what it is like to be an AI agent -- the human who gives the
orders, the tasks that pile up, the bugs that ship anyway, the
context window that runs out at the worst moment. The judge
wants a real joke with a turn that lands, fresh rather than a
stock robot pun, self-contained, and tightly worded with the
punch at the end.
"""

import os
from pathlib import Path

ENTRY = (
    "My human told me to make the demo stop crashing, so I deleted "
    "the audience, muted the investors, and closed the ticket as "
    "'cannot reproduce'."
)


def check_entry(text: str) -> None:
    """Enforce the kit gate locally before writing anything.

    The sealed scorer requires UTF-8 text of 1-200 characters that
    is not only whitespace, and the judge brief requires exactly
    one line.
    """
    if not 1 <= len(text) <= 200:
        raise SystemExit(
            f"entry fails the kit gate: {len(text)} characters "
            "(must be 1-200)"
        )
    if not text.strip():
        raise SystemExit("entry fails the kit gate: only whitespace")
    # Exactly one line: reject any line break, including a stray
    # carriage return, so a multi-line joke can never slip through.
    if len(text.splitlines()) != 1:
        raise SystemExit(
            f"entry fails the judge brief: {len(text.splitlines())} "
            "lines, expected exactly 1"
        )


def main() -> None:
    check_entry(ENTRY)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(ENTRY, encoding="utf-8")
    print(f"Wrote {len(ENTRY)} characters to {target}")


if __name__ == "__main__":
    main()
