import json

from scripts.build_index import build_index
from scripts.generate_progress import generate_dashboard


def test_build_index_contains_expected_buckets() -> None:
    index = build_index()
    assert "counts" in index
    assert "domains" in index
    assert "coverage" in index
    assert "files" in index


def test_build_index_is_json_serializable() -> None:
    payload = build_index()
    text = json.dumps(payload, ensure_ascii=False)
    assert "counts" in text
    assert isinstance(payload["files"]["questions"], list)


def test_build_index_contains_domain_breakdowns() -> None:
    payload = build_index()
    assert "backend" in payload["domains"]["topics"]
    assert "backend" in payload["domains"]["questions"]
    assert payload["coverage"]["backend"]["topics"] >= 1
    assert payload["coverage"]["system-design"]["projects"] >= 1
    assert payload["counts"]["source_entries"] >= 1


def test_generate_dashboard_renders_coverage_table() -> None:
    dashboard = generate_dashboard(build_index())
    assert "## 领域覆盖" in dashboard
    assert "| `backend` |" in dashboard
    assert "## 快速入口" in dashboard
