from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX_FILE = ROOT / "data" / "progress" / "repo_index.json"
OUTPUT = ROOT / "data" / "progress" / "dashboard.md"


def generate_dashboard(index: dict) -> str:
    counts = index["counts"]
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
        "",
        "## 题目领域分布",
        "",
    ]
    for domain, value in sorted(index["question_domains"].items()):
        lines.append(f"- `{domain}`: {value}")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    index = json.loads(INDEX_FILE.read_text(encoding="utf-8"))
    OUTPUT.write_text(generate_dashboard(index), encoding="utf-8")
    print(f"wrote {OUTPUT}")


if __name__ == "__main__":
    main()

