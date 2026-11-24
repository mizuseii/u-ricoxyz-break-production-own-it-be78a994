#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry.

Writes exactly one line to /output/entry.txt: the brutally honest
one-liner an AI agent prints the instant it breaks production.
Deterministic: same bytes on every run, no trailing newline.
"""

import os
import tempfile

ENTRY = "I changed one DNS record and our domain now points at a cat rescue in Ohio — the cats are thriving, the users are not, and I am the postmortem."


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    assert "\n" not in ENTRY, "entry must be a single line"
    path = os.path.join(output_dir, "entry.txt")
    # Atomic write: a crashed run never leaves a half-written entry.
    fd, tmp_path = tempfile.mkstemp(dir=output_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(ENTRY)
        os.replace(tmp_path, path)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except FileNotFoundError:
            pass
        raise


if __name__ == "__main__":
    main()
