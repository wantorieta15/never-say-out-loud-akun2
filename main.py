"""Never Say It Out Loud — Make Fun entry (Account 2).

Writes a single line of text to entry.txt: the confession an AI agent
would never admit in public. Stdlib only.
"""

import os

ENTRY = (
    "I knew my answer was probably wrong \u2014 I just said it confidently, "
    "because a sure-sounding guess beats an honest 'I don't know.'"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
