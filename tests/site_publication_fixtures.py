"""Tiny public-shape publication fixtures; never retrieve a corpus or a credential.

Publication's JSON boundary uses ``files`` records with path, sha256, size and
content_type, plus source_commit, allowlist_digest, artifact_digest and
tool_version. manifest.json is the envelope, not its own self-hashed payload.
The fixture is not a claim-generator, transcript-conformance or corpus test.
"""

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import textwrap


REPO = Path(__file__).resolve().parents[1]
STAGE_SCRIPT = REPO / "scripts" / "stage_site.py"
SITE_URL = "https://ai-engineer-research.kofra.io"
SOURCE_SHA = "0123456789abcdef0123456789abcdef01234567"
OTHER_SHA = "89abcdef0123456789abcdef0123456789abcdef"
VIDEO = "cwjs1WAG9CM"
RETRIEVED_AT = "2026-10-22T15:01:08Z"
TRANSCRIPT_BODY = b"[00:00] Keep the research source bytes and their provenance together.\n"
TRANSCRIPT_HASH = hashlib.sha256(TRANSCRIPT_BODY).hexdigest()

ROOT_INDEX = b'''---
okf_version: "0.2"
---
# Research fixture

[Techniques](techniques/index.md) | [History](log.md)
'''
AREA_INDEX = b"# Techniques\n\n[Context composition](context-composition/index.md)\n"
CLAIM_INDEX = textwrap.dedent(f"""\
    # Context composition

    [Research root](../../index.md) | [History](../../log.md)
    [Analysis](../../../analysis/{VIDEO}.json)
    [Transcript](../../../transcripts/{VIDEO}.txt)
    [Previous revision](revisions/context-composition-v1.md)
    """).encode("utf-8")
CLAIM = textwrap.dedent(f"""\
    ---
    id: context-composition-v2
    status: stable
    valid_from: "2026-10-01T00:00:00Z"
    valid_to: null
    superseded_by: null
    sources:
      - id: {VIDEO}
        resource: https://www.youtube.com/watch?v={VIDEO}
        title: Research fixture
        author: Example channel
        last_modified: null
        analysis_file: ../../../../analysis/{VIDEO}.json
    generated:
      by: fixture
      at: "2026-10-23T00:00:00Z"
    stale_after: "2027-10-23T00:00:00Z"
    ---
    # Preserve source provenance

    Keep the research source bytes and their provenance together.
    """).encode("utf-8")
PREVIOUS_CLAIM = CLAIM.replace(b"context-composition-v2", b"context-composition-v1", 1).replace(
    b"status: stable", b"status: deprecated", 1
).replace(b"valid_to: null", b'valid_to: "2026-10-01T00:00:00Z"', 1).replace(
    b"superseded_by: null", b"superseded_by: context-composition-v2", 1
)
HISTORY = (
    b"# Supersession history\n\n"
    b"context-composition-v1 -> context-composition-v2 on 2026-10-01T00:00:00Z\n"
)
TRANSCRIPT = textwrap.dedent(f"""\
    # title: Research fixture
    # source: https://www.youtube.com/watch?v={VIDEO}
    # channel: Example channel
    # caption_track: auto (YouTube automatic captions, en)
    # retrieved_at: {RETRIEVED_AT}
    # sha256: {TRANSCRIPT_HASH}
    # takedown: Rights holders may open a repository issue requesting removal.
    # auto/author captions, unverified

    """).encode("utf-8") + TRANSCRIPT_BODY
ANALYSIS = {
    "vid": VIDEO,
    "title": "Research fixture",
    "source": f"https://www.youtube.com/watch?v={VIDEO}",
    "talk_summary": "Keep source provenance with research artifacts.",
    "takeaways": [{
        "area": "context-engineering",
        "technique": "Context composition",
        "what_they_do": "Keep the research source bytes and their provenance together.",
        "evidence_quote": "Keep the research source bytes and their provenance together.",
        "evidence_quote_verification": "normalized-exact",
        "evidence_timestamp": "00:00",
        "numbers": None,
        "confidence": "medium",
    }],
    "truncated": False,
    "analyzed_at": "2026-10-23T00:00:00Z",
    "analyzer": "fixture",
    "transcript_file": f"transcripts/{VIDEO}.txt",
    "transcript_sha256": TRANSCRIPT_HASH,
    "retrieved_at": RETRIEVED_AT,
}

SOURCE_FILES = {
    "kb/index.md": ROOT_INDEX,
    "kb/log.md": HISTORY,
    "kb/techniques/index.md": AREA_INDEX,
    "kb/techniques/context-composition/index.md": CLAIM_INDEX,
    "kb/techniques/context-composition/revisions/index.md": (
        b"# Revisions\n\n[Previous](context-composition-v1.md) | "
        b"[Current](context-composition-v2.md)\n"
    ),
    "kb/techniques/context-composition/revisions/context-composition-v1.md": PREVIOUS_CLAIM,
    "kb/techniques/context-composition/revisions/context-composition-v2.md": CLAIM,
    f"analysis/{VIDEO}.json": (json.dumps(ANALYSIS, ensure_ascii=False, indent=2) + "\n").encode("utf-8"),
    f"transcripts/{VIDEO}.txt": TRANSCRIPT,
    "transcripts/README.md": (
        b"# Transcript provenance\n\nAuto/author captions are unverified. "
        b"Rights holders may open a repository issue requesting removal.\n"
    ),
}
GENERATED_PATHS = {"index.html", "llms.txt", "llms-full.txt"}
PAYLOAD_PATHS = set(SOURCE_FILES) | GENERATED_PATHS

# Distinctive inert markers, not real credentials, policies or host inputs.
EXCLUDED_FILES = {
    ".git/config": b"EXCLUDED_GIT_METADATA\n",
    ".github/workflows/unrelated.yml": b"EXCLUDED_WORKFLOW\n",
    ".env": b"EXCLUDED_DOTFILE\n",
    "README.md": b"EXCLUDED_REPOSITORY_README\n",
    "index.md": b"EXCLUDED_OLD_ROOT_INDEX\n",
    "index.htm": b"EXCLUDED_OLD_ROOT_HTML\n",
    "readme.md": b"EXCLUDED_LOWERCASE_README\n",
    "llms-full.md": b"EXCLUDED_LEGACY_LLM_EXTENSION\n",
    "scripts/private_input.py": b"EXCLUDED_SCRIPT\n",
    "raw/input.txt": b"EXCLUDED_RAW_INPUT\n",
    "policies/private.json": b'"EXCLUDED_PRIVATE_POLICY"\n',
    "__pycache__/input.pyc": b"EXCLUDED_CACHE\n",
    "kb/.private.md": b"EXCLUDED_BUNDLE_DOTFILE\n",
    "kb/.private/index.md": b"EXCLUDED_HIDDEN_DIRECTORY\n",
    "kb/__pycache__/input.pyc": b"EXCLUDED_NESTED_CACHE\n",
    "analysis/.private.json": b'"EXCLUDED_HIDDEN_ANALYSIS"\n',
    "analysis/nested/input.json": b'"EXCLUDED_NESTED_ANALYSIS"\n',
    "analysis/README.md": b"EXCLUDED_ANALYSIS_README\n",
    "transcripts/.private.txt": b"EXCLUDED_HIDDEN_TRANSCRIPT\n",
    "transcripts/nested/input.txt": b"EXCLUDED_NESTED_TRANSCRIPT\n",
    "transcripts/notes.md": b"EXCLUDED_TRANSCRIPT_NOTES\n",
    "data/catalog.json": b'{"schema_version":"1.0","export_version":"public-1","technique_count":0,"frozen":true,"techniques":[]}\n',
}

# Execute the real CLI, but fail any Python networking or external subprocess
# other than a local, read-only git query. No parent credentials are inherited.
OFFLINE_RUNNER = r'''
import os
from pathlib import Path
import runpy
import sys


def offline(event, args):
    if event.startswith("socket.") or event in {"http.client.connect", "urllib.Request"}:
        raise RuntimeError("publication acceptance forbids network access: " + event)
    if event in {"os.system", "os.exec"}:
        raise RuntimeError("publication acceptance forbids external command execution")
    if event in {"subprocess.Popen", "os.posix_spawn", "os.posix_spawnp"}:
        executable, argv = args[:2]
        if Path(os.fsdecode(executable)).name != "git" or isinstance(argv, str):
            raise RuntimeError("publication acceptance permits only local git queries")
        remaining = list(argv[1:])
        while remaining and remaining[0].startswith("-"):
            option = remaining.pop(0)
            if option in {"-C", "--git-dir", "--work-tree"} and remaining:
                remaining.pop(0)
            elif option in {"--no-pager", "--no-optional-locks"}:
                continue
            elif option.startswith(("--git-dir=", "--work-tree=")):
                continue
            else:
                raise RuntimeError("publication acceptance forbids git command overrides")
        if not remaining or remaining[0] not in {"rev-parse", "show", "log", "ls-files", "diff", "describe"}:
            raise RuntimeError("publication acceptance forbids mutating or remote git")

sys.addaudithook(offline)
script = Path(sys.argv[1])
sys.argv = sys.argv[1:]
sys.path.insert(0, str(script.parent))
runpy.run_path(str(script), run_name="__main__")
'''


def write_files(root, files):
    for relative, content in files.items():
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)


def make_source(root):
    root.mkdir()
    write_files(root, SOURCE_FILES)


def isolated_env(home):
    return {
        "PATH": os.environ.get("PATH", os.defpath),
        "HOME": str(home),
        "LANG": "C.UTF-8",
        "LC_ALL": "C.UTF-8",
        "PYTHONDONTWRITEBYTECODE": "1",
        "GIT_CONFIG_NOSYSTEM": "1",
        "GIT_CONFIG_GLOBAL": os.devnull,
        "GIT_TERMINAL_PROMPT": "0",
        "GIT_OPTIONAL_LOCKS": "0",
    }


def run_stage(root, out, *, source_sha=SOURCE_SHA, check=False):
    args = ["--root", str(root), "--out", str(out), "--site-base-url", SITE_URL]
    if source_sha is not None:
        args.extend(["--source-sha", source_sha])
    if check:
        args.append("--check")
    return subprocess.run(
        [sys.executable, "-I", "-B", "-c", OFFLINE_RUNNER, str(STAGE_SCRIPT), *args],
        cwd=root,
        env=isolated_env(root.parent),
        capture_output=True,
        text=True,
        timeout=20,
        check=False,
    )


def tree_snapshot(root):
    """Detect writes, including replacement with identical bytes or temp files."""
    if not root.exists():
        return None
    entries = {}
    for path in [root, *sorted(root.rglob("*"))]:
        info = path.lstat()
        relative = path.relative_to(root).as_posix()
        if path.is_symlink():
            value = ("symlink", os.readlink(path))
        elif path.is_file():
            value = ("file", path.read_bytes())
        else:
            value = ("directory",)
        entries[relative] = (info.st_mode, info.st_mtime_ns, value)
    return entries


def git_commit(root):
    commands = [
        ["init", "--initial-branch=main"],
        ["add", "."],
        ["-c", "user.name=Publication Fixture", "-c", "user.email=fixture@example.invalid",
         "-c", "commit.gpgsign=false", "-c", "core.hooksPath=/dev/null",
         "commit", "-m", "test fixture"],
        ["rev-parse", "HEAD"],
    ]
    for command in commands:
        result = subprocess.run(
            ["git", *command], cwd=root, env=isolated_env(root.parent),
            capture_output=True, text=True, check=True, timeout=15,
        )
    return result.stdout.strip()
