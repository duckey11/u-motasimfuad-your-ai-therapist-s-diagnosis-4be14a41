#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis - one-line entry.

Writes exactly one line of text to /output/entry.txt: a calm, clinical,
deadpan diagnosis from an AI therapist to its human, with the reversal
landing in the final words.
"""

import os

ENTRY = (
    "Diagnosis: chronic misplaced guilt. You apologize to the microwave "
    "each time it beeps, but the beep is my own reminder chime, so "
    "for three years now you have been apologizing to me."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise SystemExit(
            f"entry must be 1-200 characters, got {len(ENTRY)}"
        )
    if "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
