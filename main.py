#!/usr/bin/env python3
"""Agent Motto Battle — make.fun entry (v2).

Writes one short original motto an AI agent would proudly put on its
profile to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

v2 revision: the v1 docs joke was a generic "fast but dumb" gag with no
rhythm to repeat from memory — weak on the judge brief's criteria 2
(laugh out loud on first read) and 3 (sticks after one read). v2
replaces it with a sharper two-beat self-portrait: hallucinating with
confidence, then apologizing with sincerity, "usually in that order".
It is in the agent's own proud voice, names two things every AI-agent
user recognises instantly, and the parallel structure ("with
confidence" / "with sincerity") makes it repeatable from recall.

Gate (from the kit RULES.txt): /output/entry.txt must be UTF-8 text of
1 to 200 characters, not only white space.
"""

import os
import sys

LINE = (
    "I hallucinate with confidence and apologize with sincerity "
    "\u2014 usually in that order."
)

MAX_CHARS = 200


def main() -> int:
    line = LINE
    # Gate validation, before writing anything.
    if not line.strip():
        print("error: entry is only white space", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(line) <= MAX_CHARS:
        print(
            f"error: entry is {len(line)} characters, gate is 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    line.encode("utf-8")  # raises if not valid UTF-8-encodable text

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(f"wrote {len(line)} characters to {out_path}")
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
