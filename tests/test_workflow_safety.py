"""Regression checks for the manual metadata and caption execution vehicles."""

import os
from pathlib import Path
import subprocess

import yaml

ROOT = Path(__file__).resolve().parents[1]


def workflow(name):
    """Load workflow jobs without depending on YAML's interpretation of 'on'."""
    return yaml.safe_load((ROOT / ".github" / "workflows" / f"{name}.yml").read_text())


def test_canary_dispatch_input_is_an_argument_not_shell_source(tmp_path):
    """A dispatch value containing shell syntax cannot execute on the runner."""
    steps = workflow("canary")["jobs"]["canary"]["steps"]
    step = next(s for s in steps if s.get("name") == "Run Supadata canary")
    marker = tmp_path / "injected"
    hostile = f'VID0001"; touch "{marker}"; echo "'
    # Fake the Python executable so the actual workflow shell runs locally,
    # without fetching captions or needing a key.
    executable = tmp_path / "python3"
    executable.write_text('#!/bin/sh\nprintf "%s\\000" "$@" > "$ARGUMENT_FILE"\n')
    executable.chmod(0o755)
    arguments = tmp_path / "args"
    env = dict(os.environ, PATH=f"{tmp_path}:{os.environ['PATH']}", ARGUMENT_FILE=str(arguments))
    for name, value in step.get("env", {}).items():
        if value == "${{ inputs.vids }}":
            env[name] = hostile
    # Model GitHub's textual interpolation for the vulnerable version.
    shell = step["run"].replace("${{ inputs.vids }}", hostile)
    result = subprocess.run(["bash", "-e", "-c", shell], env=env, cwd=tmp_path,
                            capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    assert not marker.exists(), "workflow dispatch input was executed as shell source"
    argv = arguments.read_bytes().split(b"\0")[:-1]
    assert argv == [b"scripts/supadata_canary.py", b"--vids", hostile.encode(),
                    b"--out", b"canary-report.json"]
    assert "${{ inputs." not in step["run"]


def test_backfill_commits_only_success_or_incomplete_coverage():
    """Errors may leave per-file writes; only exit 0/1 is publishable progress."""
    steps = workflow("backfill")["jobs"]["backfill"]["steps"]
    commit = next(s for s in steps if s.get("name") == "Commit analysis dates")
    assert commit.get("if") == (
        "steps.backfill.outputs.exit_code == '0' || steps.backfill.outputs.exit_code == '1'"
    ), "error or unexpected exit status must never stage or push analysis changes"
