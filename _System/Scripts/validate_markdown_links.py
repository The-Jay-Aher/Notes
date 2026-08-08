#!/usr/bin/env python3
"""Validate local Markdown links and path-qualified Obsidian wikilinks."""

from __future__ import annotations

import os
import re
import sys
from collections import defaultdict
from pathlib import Path, PurePosixPath
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[2]
IGNORED_PARTS = {".git", ".obsidian", ".trash"}
INLINE_LINK_RE = re.compile(r"!?\[[^\]\n]*\]\((<[^>\n]+>|[^)\n]+)\)")
WIKI_LINK_RE = re.compile(r"\[\[([^\]|#\n]+)(?:#[^\]|\n]+)?(?:\|[^\]\n]+)?\]\]")
FENCED_CODE_RE = re.compile(r"(?:```|~~~).*?(?:```|~~~)", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")


def is_ignored(path: Path) -> bool:
    return any(part in IGNORED_PARTS for part in path.parts)


def markdown_files() -> list[Path]:
    return sorted(path for path in vault_paths() if path.is_file() and path.suffix == ".md")


def vault_paths():
    """Yield content paths without traversing Git, Obsidian, or trash trees."""
    for directory, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [name for name in dirnames if name not in IGNORED_PARTS]
        base = Path(directory)
        for dirname in dirnames:
            yield base / dirname
        for filename in filenames:
            yield base / filename


def strip_anchor(value: str) -> str:
    return value.split("#", 1)[0]


def main() -> int:
    files = markdown_files()
    vault_targets = {path.relative_to(ROOT).as_posix(): path for path in vault_paths()}
    markdown_by_stem: dict[str, list[str]] = defaultdict(list)
    for relative in vault_targets:
        if relative.endswith(".md"):
            markdown_by_stem[PurePosixPath(relative).stem].append(relative)

    checked = 0
    problems: list[str] = []
    for source in files:
        relative_source = source.relative_to(ROOT).as_posix()
        text = source.read_bytes().decode("utf-8")
        # Programming syntax such as C++ lambdas (`[capture](args)`) is not a link.
        text = FENCED_CODE_RE.sub("", text)
        text = INLINE_CODE_RE.sub("", text)

        for match in INLINE_LINK_RE.finditer(text):
            raw = match.group(1)
            href = raw[1:-1] if raw.startswith("<") and raw.endswith(">") else raw
            if not href or href.startswith("#") or re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", href):
                continue
            if " \"" in href or " '" in href:
                href = href.split(" ", 1)[0]
            target_text = unquote(strip_anchor(href))
            target = (source.parent / target_text).resolve()
            checked += 1
            try:
                target.relative_to(ROOT)
            except ValueError:
                problems.append(f"{relative_source}: link escapes vault: {href}")
                continue
            if not target.exists():
                problems.append(f"{relative_source}: missing Markdown target: {href}")

        for match in WIKI_LINK_RE.finditer(text):
            target_text = match.group(1).strip()
            if not target_text:
                continue
            checked += 1
            candidate = target_text if target_text.endswith(".md") else target_text + ".md"
            if "/" in target_text:
                if candidate not in vault_targets:
                    problems.append(f"{relative_source}: missing wikilink target: {target_text}")
            elif not markdown_by_stem.get(PurePosixPath(candidate).stem):
                problems.append(f"{relative_source}: unresolved short wikilink: {target_text}")

    print(f"Checked {checked} local links across {len(files)} Markdown files.")
    if problems:
        print(f"Found {len(problems)} problem(s):")
        for problem in problems:
            print(f"- {problem}")
        return 1
    print("No broken local Markdown or path-qualified Obsidian links found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
