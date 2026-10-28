"""Malformed legacy dates must be visible without changing recency ranking."""

import json
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "generate_claims.py"


@pytest.mark.parametrize("field", ["talk_date", "published_at", "publish_date"])
@pytest.mark.parametrize("value", ["Oct 26, 2026", "20261026", "2026-02-30", 20261026])
def test_invalid_selected_date_warns_and_remains_undated(tmp_path, field, value):
    """An invalid source date cannot silently discard recency information."""
    directory = tmp_path / "analysis"
    directory.mkdir()
    (directory / "bad-date.json").write_text(json.dumps({
        "video_id": "UNDATED01", field: value,
        "techniques": [{"title": "Trace first", "area": "observability"}],
    }))
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--root", str(tmp_path)],
        capture_output=True, text=True,
    )
    assert result.returncode == 0, result.stderr
    assert "bad-date.json" in result.stderr
    assert "unparseable talk date" in result.stderr
    assert "treating as undated" in result.stderr
    records = json.loads((tmp_path / "catalog.json").read_text())
    assert records["claims"][0]["valid_from"] is None


@pytest.mark.parametrize("value", [None, "", "2026-10-26", "2026-10-26T12:00:00Z"])
def test_missing_and_valid_dates_do_not_warn(tmp_path, value):
    """Missing dates are expected; accepted dates keep their existing meaning."""
    directory = tmp_path / "analysis"
    directory.mkdir()
    (directory / "source.json").write_text(json.dumps({
        "video_id": "DATED0001", "talk_date": value,
        "techniques": [{"title": "Trace first"}],
    }))
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--root", str(tmp_path)],
        capture_output=True, text=True,
    )
    assert result.returncode == 0, result.stderr
    assert result.stderr == ""
    records = json.loads((tmp_path / "catalog.json").read_text())
    assert records["claims"][0]["valid_from"] == ("2026-10-26" if value else None)
