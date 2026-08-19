#!/usr/bin/env python3
"""Collect DeepSeek Harness projects from GitHub and merge them into projects.json.

The script uses only Python's standard library so it can run locally or in GitHub
Actions without a dependency install step. Curated entries are never removed.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

API_ROOT = "https://api.github.com"
SEARCH_QUERIES = (
    '"deepseek harness" in:name,description,readme',
    'deepseek-harness in:name,description,readme',
    'dsh- in:name',
)
CATEGORY_NAMES = {
    "plugins": "Plugins",
    "integrations": "Integrations & Agents",
    "interfaces": "Interfaces (TUI / Desktop / Web)",
    "ecosystem": "Ecosystem & Marketplaces",
    "themes": "Themes & Skins",
    "other": "Other Projects",
}


def github_request(path: str, token: str | None) -> dict[str, Any]:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "awesome-deepseek-harness-collector",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = Request(f"{API_ROOT}{path}", headers=headers)
    with urlopen(request, timeout=30) as response:
        return json.load(response)


def classify(repo: dict[str, Any]) -> str:
    text = " ".join(
        [repo.get("name", ""), repo.get("description", ""), " ".join(repo.get("topics", []))]
    ).lower()
    if any(word in text for word in ("market", "marketplace", "registry")):
        return "ecosystem"
    if any(word in text for word in ("theme", "skin", "whale")):
        return "themes"
    if any(word in text for word in ("tui", "terminal", "desktop", "sidebar", "web ui", "webui")):
        return "interfaces"
    if any(word in text for word in ("data-agent", "database", "vision", "openpencil", "integration")):
        return "integrations"
    if re.search(r"(^|[-_])dsh([-_]|$)|plugin|extension|harness", text):
        return "plugins"
    return "other"


def is_relevant(repo: dict[str, Any]) -> bool:
    """Reject search false positives while allowing projects named dsh-*."""
    text = " ".join(
        [repo.get("name", ""), repo.get("full_name", ""), repo.get("description", ""), " ".join(repo.get("topics", []))]
    ).lower()
    return any(keyword in text for keyword in ("deepseek", "deep-seek", "deepseek harness", "dsh-", "dsh_", "deep whale"))


def normalise_repo(repo: dict[str, Any], existing: dict[str, Any] | None = None) -> dict[str, Any]:
    result = dict(existing or {})
    result.update(
        {
            "name": repo.get("name", result.get("name", "")),
            "full_name": repo["full_name"],
            "url": repo.get("html_url", result.get("url", "")),
            "description": repo.get("description") or result.get("description", ""),
            "stars": repo.get("stargazers_count", result.get("stars")),
            "language": repo.get("language") or result.get("language", "N/A"),
            "topics": repo.get("topics", result.get("topics", [])),
            "updated_at": repo.get("updated_at", result.get("updated_at")),
            "created_at": repo.get("created_at", result.get("created_at")),
            "archived": bool(repo.get("archived", result.get("archived", False))),
            "category": result.get("category") or classify(repo),
            "source": result.get("source", "github-search"),
        }
    )
    return result


def load_data(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"schema_version": 1, "last_updated": None, "projects": []}
    with path.open(encoding="utf-8") as handle:
        data = json.load(handle)
    data.setdefault("schema_version", 1)
    data.setdefault("projects", [])
    return data


def collect(data: dict[str, Any], token: str | None, max_results: int, min_stars: int, delay: float) -> int:
    projects = {item["full_name"].lower(): item for item in data.get("projects", []) if item.get("full_name")}
    discovered = 0
    for query in SEARCH_QUERIES:
        if discovered >= max_results:
            break
        try:
            payload = github_request(f"/search/repositories?q={quote(query)}&sort=stars&order=desc&per_page=100", token)
        except (HTTPError, URLError, TimeoutError) as error:
            print(f"warning: GitHub search failed for {query!r}: {error}", file=sys.stderr)
            continue
        for repo in payload.get("items", []):
            full_name = repo.get("full_name", "").lower()
            if not full_name or full_name in projects:
                if full_name in projects:
                    projects[full_name] = normalise_repo(repo, projects[full_name])
                continue
            if repo.get("fork") or repo.get("archived") or repo.get("stargazers_count", 0) < min_stars or not is_relevant(repo):
                continue
            projects[full_name] = normalise_repo(repo)
            discovered += 1
            print(f"collected {repo['full_name']} ({repo.get('stargazers_count', 0)} stars)")
            if discovered >= max_results:
                break
            time.sleep(delay)
    data["projects"] = sorted(projects.values(), key=lambda item: (item.get("category", "other"), -(item.get("stars") or 0), item.get("name", "").lower()))
    data["last_updated"] = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    return discovered


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=Path(__file__).parent.parent / "data" / "projects.json")
    parser.add_argument("--max-results", type=int, default=int(os.getenv("MAX_RESULTS", "100")))
    parser.add_argument("--min-stars", type=int, default=int(os.getenv("MIN_STARS", "1")))
    parser.add_argument("--delay", type=float, default=float(os.getenv("REQUEST_DELAY", "0.2")))
    parser.add_argument("--offline", action="store_true", help="Only normalise local data; do not call GitHub")
    args = parser.parse_args()
    data = load_data(args.data)
    if not args.offline:
        token = os.getenv("GITHUB_TOKEN")
        collect(data, token, max(0, args.max_results), max(0, args.min_stars), max(0, args.delay))
    args.data.parent.mkdir(parents=True, exist_ok=True)
    with args.data.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(f"saved {len(data['projects'])} projects to {args.data}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
