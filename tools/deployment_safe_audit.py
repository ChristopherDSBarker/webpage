#!/usr/bin/env python3
"""Audit local HTML references against deployable Git-tracked files.

Scope boundary: this is an existence/deployment check only. A passing result
does not approve reel readability, crop quality, focal hierarchy, semantic
strength, recruiter scan quality, or visual composition.
"""

from __future__ import annotations

import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urldefrag


ROOT = Path(__file__).resolve().parents[1]


class RefParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.refs: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        for key in ("href", "src"):
            value = data.get(key)
            if value:
                self.refs.append((key, value))


def git_lines(*args: str) -> set[str]:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        raise SystemExit(result.stderr.strip() or f"git {' '.join(args)} failed")
    return {line for line in result.stdout.splitlines() if line}


def main() -> int:
    tracked = git_lines("ls-files")
    ignored = git_lines("ls-files", "--others", "--ignored", "--exclude-standard")
    missing: list[tuple[str, str, str]] = []
    ignored_refs: list[tuple[str, str, str]] = []
    untracked_refs: list[tuple[str, str, str]] = []

    for html in sorted(ROOT.rglob("*.html")):
        if ".git" in html.parts:
            continue
        parser = RefParser()
        parser.feed(html.read_text(errors="ignore"))
        page = str(html.relative_to(ROOT))

        for kind, raw in parser.refs:
            if raw.startswith(("http://", "https://", "mailto:", "tel:", "#", "data:")):
                continue
            href, _fragment = urldefrag(raw)
            if not href:
                continue

            target = (html.parent / href).resolve()
            try:
                rel = str(target.relative_to(ROOT))
            except ValueError:
                continue

            if not target.exists():
                missing.append((page, kind, raw))
            elif rel in ignored:
                ignored_refs.append((page, kind, raw))
            elif rel not in tracked:
                untracked_refs.append((page, kind, raw))

    print(f"HTML files checked: {len(list(ROOT.rglob('*.html')))}")
    print(f"Missing references: {len(missing)}")
    print(f"Ignored-file references: {len(ignored_refs)}")
    print(f"Untracked references: {len(untracked_refs)}")
    print("Scope: deployment/path safety only; not a reel-readability approval.")

    for label, rows in (
        ("MISSING", missing),
        ("IGNORED", ignored_refs),
        ("UNTRACKED", untracked_refs),
    ):
        for page, kind, raw in rows:
            print(f"{label}|{page}|{kind}|{raw}")

    return 1 if missing or ignored_refs or untracked_refs else 0


if __name__ == "__main__":
    sys.exit(main())
