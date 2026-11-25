"""Write a one-line excuse for a missed deadline to /output/entry.txt."""

from pathlib import Path

LINE = "The deadline and I had a race condition: we both arrived, just never at the same time."


def main() -> None:
    # The excuse must stay a single line so the entry passes the gate.
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
