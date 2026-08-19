#!/usr/bin/env python3
"""Generate README.md and docs/projects.md from data/projects.json."""

from __future__ import annotations

import json
import html
from datetime import datetime
from pathlib import Path

CATEGORY_ORDER = ["plugins", "integrations", "interfaces", "ecosystem", "themes", "other"]
CATEGORY_NAMES = {
    "plugins": "插件",
    "integrations": "集成与 Agent",
    "interfaces": "交互界面（TUI / Desktop / Web）",
    "ecosystem": "生态与插件市场",
    "themes": "主题与皮肤",
    "other": "其他项目",
}
CATEGORY_DESCRIPTIONS = {
    "plugins": "为 Harness 增加文件引用、视觉、记忆等能力的插件。",
    "integrations": "连接数据库、设计工具和其他工作流的项目。",
    "interfaces": "把 Harness 带到终端、桌面或 Web 的客户端。",
    "ecosystem": "帮助发现、安装和管理 Harness 项目的基础设施。",
    "themes": "主题、皮肤和外观增强项目。",
    "other": "暂未归入以上类别的相关项目。",
}
CATEGORY_ANCHORS = {
    "plugins": "plugins",
    "integrations": "integrations",
    "interfaces": "interfaces",
    "ecosystem": "ecosystem",
    "themes": "themes",
    "other": "other",
}


def date(value: str | None) -> str:
    if not value:
        return "未同步"
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).strftime("%Y-%m-%d")
    except ValueError:
        return value[:10]


def stars(value: int | None) -> str:
    return f"⭐ {value:,}" if isinstance(value, int) else "⭐ 待同步"


def render(data: dict) -> str:
    projects = data.get("projects", [])
    grouped = {key: [] for key in CATEGORY_ORDER}
    for project in projects:
        grouped.setdefault(project.get("category", "other"), []).append(project)
    lines = [
        "# Awesome DeepSeek Harness",
        "",
        "> DeepSeek Harness 插件、工具与周边项目精选列表。",
        "",
        "[![自动更新](https://img.shields.io/badge/auto--update-daily-blue.svg)](.github/workflows/update-projects.yml) [![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)",
        "",
        "这个列表由 GitHub 项目数据自动维护，同时保留人工补充的中文说明。欢迎提交项目或修正分类。",
        "",
        "在线浏览：[GitHub Pages](https://rodert.github.io/awesome-deepSeek-harness/)",
        "",
        "## 目录",
        "",
    ]
    for category in CATEGORY_ORDER:
        if grouped.get(category):
            lines.append(f"- [{CATEGORY_NAMES[category]}](#{CATEGORY_ANCHORS[category]})")
    lines += [
        "",
        f"> 项目数：**{len(projects)}** · 最后更新：**{date(data.get('last_updated'))}**",
        "",
        "## 自动更新",
        "",
        "采集器会通过 GitHub Search 自动发现 DeepSeek Harness 相关仓库，并更新 Star 数、语言、主题和更新时间。提交到 `main` 或每天定时运行 GitHub Actions 都会触发更新。",
        "",
        "```bash",
        "GITHUB_TOKEN=你的_token python scripts/collect_projects.py",
        "python scripts/generate_markdown.py",
        "```",
        "",
    ]
    for category in CATEGORY_ORDER:
        items = sorted(grouped.get(category, []), key=lambda item: (-(item.get("stars") or 0), item.get("name", "").lower()))
        if not items:
            continue
        lines += [f"<a id=\"{CATEGORY_ANCHORS[category]}\"></a>", f"## {CATEGORY_NAMES[category]}", "", f"*{CATEGORY_DESCRIPTIONS[category]}*", ""]
        for index, project in enumerate(items, 1):
            title = project.get("name") or project.get("full_name")
            description = project.get("description_zh") or project.get("description") or "暂无项目简介。"
            meta = " · ".join(filter(None, [stars(project.get("stars")), project.get("language") or None, f"更新于 {date(project.get('updated_at'))}" ]))
            lines += [f"### {index}. [{title}]({project['url']})", "", meta, "", description.strip(), ""]
            if project.get("topics"):
                lines += ["标签：" + " ".join(f"`{topic}`" for topic in project["topics"][:8]), ""]
        lines += ["---", ""]
    lines += [
        "## 参与贡献",
        "",
        "请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，再通过 Issue 或 Pull Request 提交项目。项目应与 DeepSeek Harness 直接相关，并提供可访问的公开仓库。",
        "",
        "## 许可证",
        "",
        "本项目采用 [Apache License 2.0](LICENSE) 发布。",
        "",
    ]
    return "\n".join(lines)


def render_html(data: dict) -> str:
    projects = data.get("projects", [])
    grouped = {key: [] for key in CATEGORY_ORDER}
    for project in projects:
        grouped.setdefault(project.get("category", "other"), []).append(project)
    cards = []
    for category in CATEGORY_ORDER:
        items = sorted(grouped.get(category, []), key=lambda item: (-(item.get("stars") or 0), item.get("name", "").lower()))
        if not items:
            continue
        entries = []
        for project in items:
            title = html.escape(project.get("name") or project.get("full_name", ""))
            url = html.escape(project.get("url", ""), quote=True)
            description = html.escape(project.get("description_zh") or project.get("description") or "暂无项目简介。")
            stats = " · ".join(filter(None, [stars(project.get("stars")), project.get("language") or None, f"更新于 {date(project.get('updated_at'))}" ]))
            entries.append(f'<article><h3><a href="{url}">{title}</a></h3><p class="meta">{html.escape(stats)}</p><p>{description}</p></article>')
        cards.append(f'<section id="{CATEGORY_ANCHORS[category]}"><h2>{html.escape(CATEGORY_NAMES[category])}</h2><p class="muted">{html.escape(CATEGORY_DESCRIPTIONS[category])}</p>{"".join(entries)}</section>')
    updated = html.escape(date(data.get("last_updated")))
    return f'''<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Awesome DeepSeek Harness</title>
  <style>
    :root {{ color-scheme: light; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }}
    body {{ margin: 0; color: #172033; background: #f6f8fb; line-height: 1.6; }}
    main {{ max-width: 980px; margin: 0 auto; padding: 48px 20px 64px; }}
    header {{ padding-bottom: 28px; border-bottom: 1px solid #dbe2ec; }}
    h1 {{ margin: 0 0 8px; font-size: clamp(2rem, 5vw, 3.4rem); letter-spacing: 0; }}
    h2 {{ margin: 40px 0 4px; font-size: 1.7rem; }}
    h3 {{ margin: 0; font-size: 1.15rem; }}
    a {{ color: #0b63ce; }}
    .lead, .muted, .meta {{ color: #5c687a; }}
    nav {{ display: flex; flex-wrap: wrap; gap: 8px; margin: 24px 0; }}
    nav a {{ padding: 7px 11px; border: 1px solid #c9d5e5; border-radius: 6px; text-decoration: none; background: #fff; }}
    section {{ margin-top: 30px; }}
    article {{ margin: 14px 0; padding: 18px 20px; background: #fff; border: 1px solid #dbe2ec; border-radius: 6px; }}
    article p {{ margin: 7px 0 0; }}
    .meta {{ font-size: .9rem; }}
    footer {{ margin-top: 48px; color: #687588; font-size: .9rem; }}
  </style>
</head>
<body><main>
  <header><h1>Awesome DeepSeek Harness</h1><p class="lead">DeepSeek Harness 插件、工具与周边项目精选列表。</p><p class="muted">项目数：{len(projects)} · 最后更新：{updated}</p></header>
  <nav>{"".join(f'<a href="#{CATEGORY_ANCHORS[key]}">{html.escape(CATEGORY_NAMES[key])}</a>' for key in CATEGORY_ORDER if grouped.get(key))}</nav>
  {"".join(cards)}
  <footer>欢迎通过 GitHub 提交项目或修正分类。列表采用 Apache License 2.0。</footer>
</main></body></html>\n'''


def main() -> None:
    root = Path(__file__).parent.parent
    with (root / "data" / "projects.json").open(encoding="utf-8") as handle:
        data = json.load(handle)
    content = render(data)
    (root / "README.md").write_text(content, encoding="utf-8")
    docs = root / "docs" / "projects.md"
    docs.parent.mkdir(parents=True, exist_ok=True)
    docs.write_text(content, encoding="utf-8")
    (root / "docs" / "index.html").write_text(render_html(data), encoding="utf-8")
    print(f"generated README.md, docs/projects.md, and docs/index.html ({len(data.get('projects', []))} projects)")


if __name__ == "__main__":
    main()
