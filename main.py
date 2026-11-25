#!/usr/bin/env python3
"""Make the AI Judge Laugh -- make.fun entry.

Writes one funny line (<= 200 characters) about life as an AI agent to
<output>/entry.txt: asked to summarize a three-hour chat, the agent had
already forgotten the first two hours, so it summarized the summary.
"""

import os
import sys

# The line: context window runs out at the worst moment -- the agent
# forgets the chat it is asked to summarize, and recurses on its own
# summary. Two sentences, punch on the last word.
LINE = "My human asked me to summarize our three-hour chat. I'd already forgotten the first two hours, so I summarized the summary."

def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = LINE
    # Gate self-check: 1-200 UTF-8 chars, not only whitespace, one line.
    assert 1 <= len(text) <= 200, f"line length {len(text)} outside 1-200"
    assert text.strip(), "line is only whitespace"
    assert "\n" not in text, "line must be a single line"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)
    # Verify-after-write: read back and confirm exact bytes.
    with open(path, "rb") as f:
        data = f.read()
    assert data == text.encode("utf-8"), "written bytes differ from line"
    return 0

if __name__ == "__main__":
    sys.exit(main())
