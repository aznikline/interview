from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TOPIC_REQUIRED = ["## 1 分钟速答", "## 核心机制", "## 高频问法", "## 深挖与误区"]
QUESTION_REQUIRED = ["## 题目", "## 一句话回答", "## 展开回答", "## 面试官追问"]


def validate_file(path: Path, required_sections: list[str]) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return [section for section in required_sections if section not in text]


def lint() -> list[str]:
    errors: list[str] = []

    for path in sorted((ROOT / "docs" / "topics").rglob("*.md")):
        missing = validate_file(path, TOPIC_REQUIRED)
        if missing:
            errors.append(f"{path.relative_to(ROOT)} missing sections: {', '.join(missing)}")

    for path in sorted((ROOT / "questions").rglob("*.md")):
        missing = validate_file(path, QUESTION_REQUIRED)
        if missing:
            errors.append(f"{path.relative_to(ROOT)} missing sections: {', '.join(missing)}")

    return errors


def main() -> None:
    errors = lint()
    if errors:
        for error in errors:
            print(error)
        raise SystemExit(1)
    print("docs lint passed")


if __name__ == "__main__":
    main()

