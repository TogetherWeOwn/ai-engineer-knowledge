#!/usr/bin/env python3
"""Publish an offline OKF bundle from frozen catalog identities and real analyses.

The catalog is input, never output. --candidates is a read-only deterministic
report; --relations accepts untrusted proposals, not arbitrary identities.
Legacy video_id/techniques fixtures retain their isolated compatibility path.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from frozen_claims import PublicationError, generate


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", type=Path, default=Path("."))
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--candidates", action="store_true", help="report candidates without writing")
    modes.add_argument("--check", action="store_true", help="offline freshness check; never repair")
    parser.add_argument("--relations", type=Path, help="schema-versioned relation proposals")
    args = parser.parse_args(argv)
    try:
        report, code = generate(args.root, candidates=args.candidates, check=args.check,
                                relations=args.relations)
    except PublicationError as exc:
        report, code = {"error": {"code": exc.code, "message": str(exc)}}, 2
    except (OSError, UnicodeError):
        # Never print arbitrary input/exception text (which may contain secrets).
        report, code = {"error": {"code": "io_error", "message": "Cannot read or publish the bundle."}}, 2
    if report is None:
        # Only positively identified legacy inputs reach this compatibility path.
        # In particular a real vid record without its catalog must fail closed.
        from legacy_claims import main as legacy_main
        return legacy_main(argv)
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
