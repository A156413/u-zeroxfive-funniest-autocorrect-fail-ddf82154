#!/usr/bin/env python3
"""Funniest Autocorrect Fail - make.fun entry.

Writes one line, a single autocorrect fail under 200 characters,
to /output/entry.txt and prints it to stdout.
"""

import os

ENTRY = "Mom, great news, I passed my drug test! I mean my driving test. My DRIVING test. Please call me back, I'm begging you."


def main():
    # The gate requires 1 to 199 characters; fail loudly instead of
    # submitting an invalid entry if the line is ever edited past it.
    assert 1 <= len(ENTRY) <= 199, f"entry is {len(ENTRY)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)
    print(ENTRY)


if __name__ == "__main__":
    main()
