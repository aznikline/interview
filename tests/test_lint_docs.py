from pathlib import Path

from scripts.lint_docs import validate_file


def test_validate_file_reports_missing_sections(tmp_path: Path) -> None:
    target = tmp_path / "doc.md"
    target.write_text("# demo\n\n## 核心机制\n", encoding="utf-8")
    missing = validate_file(target, ["## 1 分钟速答", "## 核心机制"])
    assert missing == ["## 1 分钟速答"]


def test_validate_file_returns_empty_for_complete_document(tmp_path: Path) -> None:
    target = tmp_path / "doc.md"
    target.write_text(
        "## 1 分钟速答\n\n## 核心机制\n\n## 高频问法\n\n## 深挖与误区\n",
        encoding="utf-8",
    )
    missing = validate_file(target, ["## 1 分钟速答", "## 核心机制", "## 高频问法", "## 深挖与误区"])
    assert missing == []

