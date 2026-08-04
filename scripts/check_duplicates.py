#!/usr/bin/env python3
"""Check README resource entries for duplicate names and URLs."""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

# Resource entries use the repository's required list format. Restricting the
# parser to that format naturally excludes badges, TOC links, and prose links.
RESOURCE_RE = re.compile(
    r"^\s*-\s+\[(?P<name>[^\]]+)\]\((?P<url>[^)\s]+)(?:\s+['\"][^)]*['\"])?\)\s+—"
)


def normalize_url(url: str) -> str:
    """Return a stable URL form for duplicate detection."""
    parts = urlsplit(url)
    query = [
        (key, value)
        for key, value in parse_qsl(parts.query, keep_blank_values=True)
        if not key.lower().startswith("utm_")
        and key.lower() not in {"fbclid", "gclid", "mc_cid", "mc_eid"}
    ]
    path = parts.path or "/"
    if path != "/":
        path = path.rstrip("/")
    return urlunsplit(
        (
            parts.scheme.lower(),
            parts.netloc.lower(),
            path,
            urlencode(sorted(query)),
            "",
        )
    )


def resource_entries() -> list[tuple[str, str, int]]:
    """Read resource name, URL, and line number triples from README.md."""
    entries: list[tuple[str, str, int]] = []
    for line_number, line in enumerate(README.read_text(encoding="utf-8").splitlines(), 1):
        match = RESOURCE_RE.match(line)
        if match:
            entries.append((match.group("name").strip(), match.group("url"), line_number))
    return entries


def duplicates_by_key(entries: list[tuple[str, str, int]], key_function):
    grouped = defaultdict(list)
    for entry in entries:
        grouped[key_function(entry)].append(entry)
    return {key: values for key, values in grouped.items() if len(values) > 1}


def describe(entry: tuple[str, str, int]) -> str:
    name, url, line_number = entry
    return f"line {line_number}: [{name}]({url})"


def main() -> int:
    if not README.exists():
        print(f"ERROR: README.md not found at {README}", file=sys.stderr)
        return 1

    entries = resource_entries()
    duplicate_names = duplicates_by_key(entries, lambda entry: entry[0].casefold())
    duplicate_urls = duplicates_by_key(entries, lambda entry: normalize_url(entry[1]))

    if not duplicate_names and not duplicate_urls:
        print(f"No duplicate resources found ({len(entries)} resource entries checked).")
        return 0

    if duplicate_names:
        print("Duplicate resource names found:", file=sys.stderr)
        for name, matches in duplicate_names.items():
            print(f"  {name!r}", file=sys.stderr)
            for entry in matches:
                print(f"    - {describe(entry)}", file=sys.stderr)

    if duplicate_urls:
        print("Duplicate resource URLs found:", file=sys.stderr)
        for url, matches in duplicate_urls.items():
            print(f"  {url}", file=sys.stderr)
            for entry in matches:
                print(f"    - {describe(entry)}", file=sys.stderr)

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
