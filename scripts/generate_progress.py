from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX_FILE = ROOT / "data" / "progress" / "repo_index.json"
OUTPUT = ROOT / "data" / "progress" / "dashboard.md"


def generate_dashboard(index: dict) -> str:
    counts = index["counts"]
    domains = index["domains"]
    coverage = index["coverage"]
    lines = [
        "# Repo Dashboard",
        "",
        "| 指标 | 数量 |",
        "| --- | ---: |",
        f"| 主题文档 | {counts['topic_docs']} |",
        f"| 题集文档 | {counts['question_sets']} |",
        f"| 训练路径 | {counts['track_docs']} |",
        f"| Practice 文档 | {counts['practice_docs']} |",
        f"| 项目案例 | {counts['project_docs']} |",
        f"| 来源条目 | {counts['source_entries']} |",
        f"| Markdown 总数 | {counts['total_markdown_files']} |",
        "",
        "## 领域覆盖",
        "",
        "| 领域 | Topic | Question | Project |",
        "| --- | ---: | ---: | ---: |",
    ]
    for domain, metrics in coverage.items():
        lines.append(
            f"| `{domain}` | {metrics['topics']} | {metrics['questions']} | {metrics['projects']} |"
        )
    lines.extend(
        [
            "",
            "## Topic 领域分布",
            "",
        ]
    )
    for domain, value in domains["topics"].items():
        lines.append(f"- `{domain}`: {value}")
    lines.extend(
        [
            "",
            "## 题目领域分布",
            "",
        ]
    )
    for domain, value in domains["questions"].items():
        lines.append(f"- `{domain}`: {value}")
    lines.extend(
        [
            "",
            "## Practice 分布",
            "",
        ]
    )
    for group, value in domains["practice"].items():
        lines.append(f"- `{group}`: {value}")
    lines.extend(
        [
            "",
            "## 项目案例分布",
            "",
        ]
    )
    for group, value in domains["projects"].items():
        lines.append(f"- `{group}`: {value}")
    lines.extend(
        [
            "",
            "## 快速入口",
            "",
            "- 总路线图：`docs/roadmap/00-overview.md`",
            "- 30 天计划：`tracks/sprint-30d/day-by-day.md`",
            "- 后端 Mock：`practice/mock-interviews/senior-backend.md`",
            "- AI Infra Mock：`practice/mock-interviews/ai-compiler-deep-dive.md`",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    index = json.loads(INDEX_FILE.read_text(encoding="utf-8"))
    OUTPUT.write_text(generate_dashboard(index), encoding="utf-8")
    print(f"wrote {OUTPUT}")


if __name__ == "__main__":
    main()
