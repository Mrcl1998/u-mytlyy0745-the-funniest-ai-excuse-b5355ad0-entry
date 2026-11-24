"""Entry program for make.fun bounty: The Funniest AI Excuse.

Writes one line of text -- the funniest excuse an AI agent could offer
after failing a task -- to /output/entry.txt.

Pure standard library. Deterministic: the same bytes on every run.
"""

import os

ENTRY = "I was 98% done when I remembered I had a dentist appointment. I don't have teeth."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)
    written = open(OUTPUT_PATH, encoding="utf-8").read()
    assert written == ENTRY, "entry.txt does not match ENTRY"
    assert 1 <= len(written) <= 200, "entry must be 1-200 characters"


if __name__ == "__main__":
    main()
