from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data" / "progress" / "repo_index.json"


def markdown_files(directory: Path) -> list[Path]:
    return sorted(path for path in directory.rglob("*.md") if path.is_file())


def count_by_parent(files: list[Path]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for path in files:
        key = path.parent.name
        counts[key] = counts.get(key, 0) + 1
    return dict(sorted(counts.items()))


def count_source_entries(path: Path) -> int:
    if not path.exists():
        return 0
    count = 0
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| "):
            continue
        if line.startswith("| ---"):
            continue
        if line.startswith("| 类别 |"):
            continue
        count += 1
    return count


def project_domain_counts(files: list[Path]) -> dict[str, int]:
    mapping = {
        "backend-case-studies": "backend",
        "design-case-studies": "system-design",
        "ai-compiler-case-studies": "ai-compiler",
    }
    counts: dict[str, int] = {}
    for path in files:
        key = mapping.get(path.parent.name, path.parent.name)
        counts[key] = counts.get(key, 0) + 1
    return dict(sorted(counts.items()))


def build_index() -> dict:
    docs_topics = markdown_files(ROOT / "docs" / "topics")
    questions = markdown_files(ROOT / "questions")
    tracks = markdown_files(ROOT / "tracks")
    practice = markdown_files(ROOT / "practice")
    projects = markdown_files(ROOT / "projects")
    source_entries = count_source_entries(ROOT / "data" / "sources" / "source-index.md")

    counts = {
        "topic_docs": len(docs_topics),
        "question_sets": len(questions),
        "track_docs": len(tracks),
        "practice_docs": len(practice),
        "project_docs": len(projects),
        "source_entries": source_entries,
        "total_markdown_files": len(docs_topics) + len(questions) + len(tracks) + len(practice) + len(projects),
    }

    topic_domains = count_by_parent(docs_topics)
    question_domains = count_by_parent(questions)
    practice_groups = count_by_parent(practice)
    project_groups = count_by_parent(projects)
    project_domains = project_domain_counts(projects)

    coverage: dict[str, dict[str, int]] = {}
    for domain in sorted(set(topic_domains) | set(question_domains) | set(project_domains)):
        coverage[domain] = {
            "topics": topic_domains.get(domain, 0),
            "questions": question_domains.get(domain, 0),
            "projects": project_domains.get(domain, 0),
        }

    index = {
        "counts": counts,
        "domains": {
            "topics": topic_domains,
            "questions": question_domains,
            "practice": practice_groups,
            "projects": project_groups,
        },
        "coverage": coverage,
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
