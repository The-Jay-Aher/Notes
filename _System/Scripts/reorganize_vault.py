#!/usr/bin/env python3
"""Perform the August 2026 subject-based vault reorganization.

The migration is intentionally idempotent: an item already at its destination is
accepted, while a source/destination collision stops the run. Markdown and
Obsidian links are rewritten from their old locations to their new locations.
"""

from __future__ import annotations

import os
import posixpath
import re
import shutil
from pathlib import Path, PurePosixPath
from urllib.parse import quote, unquote


ROOT = Path(__file__).resolve().parents[2]

MOVES = {
    # Cloud, DevOps, and platform engineering.
    "AWS Cloud Practitioner": "notes/devops-cloud/aws-cloud-practitioner",
    "AWS Solution Architect": "notes/devops-cloud/aws-solutions-architect-associate",
    "AWS Solutions Architect Professional": "notes/devops-cloud/aws-solutions-architect-professional",
    "Ansible": "notes/devops-cloud/ansible",
    "ArgoCD": "notes/devops-cloud/argocd",
    "Certified Kubernetes Administrator": "notes/devops-cloud/cka",
    "Certified Kubernetes Application Developer": "notes/devops-cloud/ckad",
    "Docker": "notes/devops-cloud/docker",
    "Introduction to DevSecOps for Cloud": "notes/devops-cloud/devsecops",
    "Jenkins": "notes/devops-cloud/jenkins",
    "Kubernetes Architecture": "notes/devops-cloud/kubernetes",
    "Terraform": "notes/devops-cloud/terraform",
    "Learning GitHub Actions.md": "notes/devops-cloud/github-actions/Learning GitHub Actions.md",
    "CKA Exam.md": "notes/devops-cloud/cka/12 - Exam Experience.md",
    # Programming and computer science.
    "C++": "notes/programming/cpp",
    "Competitive Programming": "notes/programming/competitive-programming",
    "Java": "notes/programming/java",
    "Low Level Design": "notes/programming/low-level-design",
    "Python": "notes/programming/python",
    # Competitive examinations.
    "MPSC": "notes/competitive-exams/mpsc",
    "RBI Assistant": "notes/competitive-exams/rbi-assistant",
    "RBI Grade B": "notes/competitive-exams/rbi-grade-b",
    "SEBI Grade A": "notes/competitive-exams/sebi-grade-a",
    "UPSC": "notes/competitive-exams/upsc",
    # Shared foundations and references.
    "Networking Fundamentals": "notes/shared-foundations/networking",
    "Bash.md": "notes/shared-foundations/linux/Bash.md",
    "Markdown Cheatsheet.md": "notes/shared-foundations/tools/Markdown Cheatsheet.md",
    # Finance and trading study material.
    "Financial Jargon Glossary.md": "notes/finance-trading/foundations/Financial Jargon Glossary.md",
    "Fundamental Analysis.md": "notes/finance-trading/foundations/Fundamental Analysis.md",
    "Positional Trader.md": "notes/finance-trading/strategies/Positional Trader.md",
    "Probabilistic Trading Guide.md": "notes/finance-trading/strategies/Probabilistic Trading Guide.md",
    "pro_trading_workbook_template.md": "notes/finance-trading/workbooks/pro_trading_workbook_template.md",
    "professional_trading_workbook_methodology.md": "notes/finance-trading/workbooks/professional_trading_workbook_methodology.md",
    "action_plan.md": "notes/finance-trading/governance/action_plan.md",
    "misunderstanding_register.md": "notes/finance-trading/governance/misunderstanding_register.md",
    "trading_notes_audit_report.md": "notes/finance-trading/governance/trading_notes_audit_report.md",
    "aws_saa_trading_bot_plan_checklist.md": "notes/finance-trading/study-plans/aws_saa_trading_bot_plan_checklist.md",
    "aws_saa_trading_bot_plan_checklist_v2.md": "notes/finance-trading/study-plans/aws_saa_trading_bot_plan_checklist_v2.md",
    # Personal material that should not be mixed with subject notes.
    "About Me.md": "personal/astrology/About Me.md",
    "What I should do.md": "personal/astrology/What I should do.md",
    "Mentor Meet.md": "personal/career/Mentor Meet.md",
    "Todo's.md": "personal/planning/Todo's.md",
    "AWS Solution Architect/Opening a Bag lock.md": "personal/reference/Opening a Bag Lock.md",
    # Repository instructions and coverage records.
    "everything": "_System/Instructions/master-subject-prompts.md",
    "instructions": "_System/Instructions/upsc-note-generation-instructions.md",
    "00 - Everything Master Coverage and Source Backbone.md": "_System/Repository/00 - Master Coverage and Source Backbone.md",
}

INLINE_LINK_RE = re.compile(r"(!?\[[^\]\n]*\]\()(<[^>\n]+>|[^)\n]+)(\))")
WIKI_LINK_RE = re.compile(r"\[\[([^\]|#\n]+)(#[^\]|\n]+)?(\|[^\]\n]+)?\]\]")
CODE_PATH_RE = re.compile(r"`([^`\n]+)`")


def normalize(relative: str | PurePosixPath) -> str:
    return posixpath.normpath(str(PurePosixPath(relative)))


def remap(relative: str) -> str:
    """Map an old vault-relative path to its new vault-relative path."""
    relative = normalize(relative)
    for old, new in sorted(MOVES.items(), key=lambda item: len(item[0]), reverse=True):
        if relative == old:
            return new
        prefix = old + "/"
        if relative.startswith(prefix):
            return new + relative[len(old) :]
    return relative


def inverse_remap(relative: str) -> str:
    """Recover the pre-migration path for a migrated file."""
    relative = normalize(relative)
    for old, new in sorted(MOVES.items(), key=lambda item: len(item[1]), reverse=True):
        if relative == new:
            return old
        prefix = new + "/"
        if relative.startswith(prefix):
            return old + relative[len(new) :]
    return relative


def collect_old_targets() -> set[str]:
    targets: set[str] = set()
    for old, new in MOVES.items():
        old_path = ROOT / old
        new_path = ROOT / new
        active = old_path if old_path.exists() else new_path
        if not active.exists():
            continue
        if active.is_file():
            targets.add(old)
            continue
        targets.add(old)
        for item in active.rglob("*"):
            relative_tail = item.relative_to(active).as_posix()
            targets.add(f"{old}/{relative_tail}")
    for item in ROOT.rglob("*"):
        if any(part in {".git", ".obsidian", ".trash"} for part in item.parts):
            continue
        try:
            current = item.relative_to(ROOT).as_posix()
        except ValueError:
            continue
        targets.add(inverse_remap(current))
    return targets


def move_items() -> None:
    # Nested exceptions must move before their parent topic directories.
    for old, new in sorted(MOVES.items(), key=lambda item: len(item[0]), reverse=True):
        source = ROOT / old
        destination = ROOT / new
        if source == destination:
            continue
        if source.exists() and destination.exists():
            raise RuntimeError(f"Both source and destination exist: {old!r} -> {new!r}")
        if not source.exists():
            if destination.exists():
                continue
            raise FileNotFoundError(f"Migration source is missing: {old}")
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(source), str(destination))


def split_anchor(value: str) -> tuple[str, str]:
    if "#" not in value:
        return value, ""
    path, fragment = value.split("#", 1)
    return path, "#" + fragment


def rewrite_markdown_link(match: re.Match[str], old_source: str, new_source: str, old_targets: set[str]) -> str:
    opening, raw_href, closing = match.groups()
    angled = raw_href.startswith("<") and raw_href.endswith(">")
    href = raw_href[1:-1] if angled else raw_href
    if not href or href.startswith("#") or re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", href):
        return match.group(0)
    if " \"" in href or " '" in href:
        return match.group(0)  # Leave uncommon title syntax untouched for manual audit.

    encoded_path, anchor = split_anchor(href)
    decoded_path = unquote(encoded_path)
    old_parent = PurePosixPath(old_source).parent
    old_target = normalize(old_parent / PurePosixPath(decoded_path))
    if old_target not in old_targets:
        return match.group(0)

    new_target = remap(old_target)
    new_parent = PurePosixPath(new_source).parent
    relative_target = os.path.relpath(new_target, start=str(new_parent)).replace(os.sep, "/")
    encoded_target = quote(relative_target, safe="/%:@?&=+$,;~*'!%") + anchor
    if angled:
        encoded_target = f"<{encoded_target}>"
    return opening + encoded_target + closing


def rewrite_wiki_link(match: re.Match[str], old_targets: set[str]) -> str:
    target, anchor, alias = match.groups()
    candidate = normalize(target.strip())
    candidates = [candidate]
    if not candidate.endswith(".md"):
        candidates.append(candidate + ".md")
    matched = next((item for item in candidates if item in old_targets), None)
    if matched is None:
        return match.group(0)
    mapped = remap(matched)
    if not candidate.endswith(".md") and mapped.endswith(".md"):
        mapped = mapped[:-3]
    return f"[[{mapped}{anchor or ''}{alias or ''}]]"


def rewrite_code_path(match: re.Match[str], old_targets: set[str]) -> str:
    value = match.group(1)
    normalized = normalize(value.rstrip("/"))
    if normalized in old_targets:
        mapped = remap(normalized)
        if value.endswith("/"):
            mapped += "/"
        return f"`{mapped}`"
    return match.group(0)


def rewrite_links(old_targets: set[str]) -> int:
    changed = 0
    for path in ROOT.rglob("*.md"):
        if any(part in {".git", ".obsidian", ".trash"} for part in path.parts):
            continue
        new_source = path.relative_to(ROOT).as_posix()
        old_source = inverse_remap(new_source)
        original = path.read_bytes().decode("utf-8")
        updated = INLINE_LINK_RE.sub(
            lambda match: rewrite_markdown_link(match, old_source, new_source, old_targets),
            original,
        )
        updated = WIKI_LINK_RE.sub(lambda match: rewrite_wiki_link(match, old_targets), updated)
        updated = CODE_PATH_RE.sub(lambda match: rewrite_code_path(match, old_targets), updated)
        if updated != original:
            path.write_bytes(updated.encode("utf-8"))
            changed += 1
    return changed


def main() -> None:
    old_targets = collect_old_targets()
    move_items()
    changed = rewrite_links(old_targets)
    print(f"Reorganization complete; links updated in {changed} Markdown files.")


if __name__ == "__main__":
    main()
