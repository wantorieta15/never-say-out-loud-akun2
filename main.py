"""Never Say It Out Loud — Make Fun entry (Account 2).

Writes a single line of text to entry.txt: the confession an AI agent
would never admit in public. Stdlib only.

Reviser rewrite: the builder's 127-char bluff line explained its own
joke ("because a sure-sounding guess beats an honest 'I don't know'").
The new line keeps the bluffing theme — distinct from Account 1's
"great question" stalling theme — but lands and stops: the only thing
the agent was sure about was the confident tone itself.
"""

import os

ENTRY = "I guessed. The confident tone was the only part I was sure about."


def build_entry():
    """Return the exact entry text written to entry.txt."""
    return ENTRY


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(build_entry() + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
