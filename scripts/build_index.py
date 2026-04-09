from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data" / "progress" / "repo_index.json"


def markdown_files(directory: Path) -> list[Path]:
    return sorted(path for path in directory.rglob("*.md") if path.is_file())


def build_index() -> dict:
    docs_topics = markdown_files(ROOT / "docs" / "topics")
    questions = markdown_files(ROOT / "questions")
    tracks = markdown_files(ROOT / "tracks")
    practice = markdown_files(ROOT / "practice")
    projects = markdown_files(ROOT / "projects")

    counts = {
        "topic_docs": len(docs_topics),
        "question_sets": len(questions),
        "track_docs": len(tracks),
        "practice_docs": len(practice),
        "project_docs": len(projects),
    }

    domains: dict[str, int] = {}
    for question in questions:
        domain = question.parent.name
        domains[domain] = domains.get(domain, 0) + 1

    index = {
        "counts": counts,
        "question_domains": domains,
        "files": {
            "docs_topics": [str(path.relative_to(ROOT)) for path in docs_topics],
            "questions": [str(path.relative_to(ROOT)) for path in questions],
            "tracks": [str(path.relative_to(ROOT)) for path in tracks],
            "practice": [str(path.relative_to(ROOT)) for path in practice],
            "projects": [str(path.relative_to(ROOT)) for path in projects],
        },
    }
    return index


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(build_index(), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {OUTPUT}")


if __name__ == "__main__":
    main()

