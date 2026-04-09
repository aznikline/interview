import json
from pathlib import Path

from scripts.build_index import build_index


def test_build_index_contains_expected_buckets() -> None:
    index = build_index()
    assert "counts" in index
    assert "question_domains" in index
    assert "files" in index


def test_build_index_is_json_serializable() -> None:
    payload = build_index()
    text = json.dumps(payload, ensure_ascii=False)
    assert "counts" in text
    assert isinstance(payload["files"]["questions"], list)

