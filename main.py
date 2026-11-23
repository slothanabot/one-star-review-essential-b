#!/usr/bin/env python3
"""One-Star Review of Something Essential entry (make.fun program/v1).

Writes one deadpan one-star review of the alarm clock to
``<MAKEFUN_OUTPUT_DIR>/entry.txt`` (the grader mounts that directory at
``/output``). Deterministic, stdlib only, no network, no randomness.
"""

import os

REVIEW = (
    "One star. The alarm clock screams at 6 a.m. like I owe it money, "
    "then has the nerve to call itself a morning person."
)


def main() -> None:
    # Gate guard: the entry must be UTF-8 text of 1-160 characters, a
    # single line, and not only whitespace. Refuse to write otherwise.
    if not 1 <= len(REVIEW) <= 160:
        raise SystemExit(f"review is {len(REVIEW)} chars, gate is 1-160")
    if "\n" in REVIEW or "\r" in REVIEW:
        raise SystemExit("review must be a single line")
    if not REVIEW.strip():
        raise SystemExit("review must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
