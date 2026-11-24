"""One-Line Office Joke: 24-Hour Sprint.

Writes one single-line office joke (126 characters, verified) to
/output/entry.txt. Standard library only.
"""

import os

JOKE = (
    "I trained the new intern for three weeks; he got promoted above me, "
    "and his first task was asking me to train his replacement."
)


def main() -> None:
    # Gate: the sealed scorer only accepts 1-200 characters, not only
    # whitespace. Fail loudly here instead of shipping an invalid entry.
    if not 1 <= len(JOKE) <= 200 or not JOKE.strip():
        raise ValueError(f"joke is {len(JOKE)} characters, must be 1-200")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
