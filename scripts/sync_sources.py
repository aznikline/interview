from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_INDEX = ROOT / "data" / "sources" / "source-index.md"
OUTPUT = ROOT / "data" / "sources" / "source-links.txt"


def extract_links(text: str) -> list[str]:
    links: list[str] = []
    for line in text.splitlines():
        if "| [" not in line:
            continue
        parts = line.split("|")
        if len(parts) < 3:
            continue
        raw = parts[2]
        start = raw.find("(")
        end = raw.find(")")
        if start != -1 and end != -1 and end > start:
            links.append(raw[start + 1 : end])
    return links


def main() -> None:
    links = extract_links(SOURCE_INDEX.read_text(encoding="utf-8"))
    OUTPUT.write_text("\n".join(links) + "\n", encoding="utf-8")
    print(f"wrote {OUTPUT}")


if __name__ == "__main__":
    main()

