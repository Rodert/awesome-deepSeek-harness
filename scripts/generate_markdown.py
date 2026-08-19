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

LANGUAGES = {
    "zh-CN": {
        "name": "简体中文", "title": "Awesome DeepSeek Harness", "intro": "DeepSeek Harness 插件、工具与周边项目精选列表。",
        "maintained": "这个列表由 GitHub 项目数据自动维护，同时保留人工补充的中文说明。欢迎提交项目或修正分类。", "online": "在线浏览", "toc": "目录", "total": "项目数", "updated": "最后更新", "auto": "自动更新",
        "auto_desc": "采集器会通过 GitHub Search 自动发现 DeepSeek Harness 相关仓库，并更新 Star 数、语言、主题和更新时间。提交到 `main` 或每天定时运行 GitHub Actions 都会触发更新。", "token": "你的_token", "tags": "标签", "updated_at": "更新于", "unsynced": "未同步", "pending": "待同步",
        "contribute": "参与贡献", "contribute_desc": "请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，再通过 Issue 或 Pull Request 提交项目。项目应与 DeepSeek Harness 直接相关，并提供可访问的公开仓库。", "license": "许可证", "license_desc": "本项目采用 [Apache License 2.0](LICENSE) 发布。", "footer": "欢迎通过 GitHub 提交项目或修正分类。列表采用 Apache License 2.0。",
        "categories": CATEGORY_NAMES, "category_desc": CATEGORY_DESCRIPTIONS, "fallback": "暂无项目简介。"
    },
    "en": {
        "name": "English", "title": "Awesome DeepSeek Harness", "intro": "A curated list of DeepSeek Harness plugins, tools, and companion projects.",
        "maintained": "Automatically maintained from GitHub project data, with human-curated descriptions. Contributions and corrections are welcome.", "online": "Browse online", "toc": "Contents", "total": "Projects", "updated": "Last updated", "auto": "Automatic updates",
        "auto_desc": "The collector discovers DeepSeek Harness repositories through GitHub Search and refreshes stars, languages, topics, and timestamps. Pushes to `main` and the daily schedule trigger updates.", "token": "your_token", "tags": "Tags", "updated_at": "Updated", "unsynced": "not synced", "pending": "pending",
        "contribute": "Contributing", "contribute_desc": "Read [CONTRIBUTING.md](CONTRIBUTING.md), then submit a project through an issue or pull request. Projects must be directly related to DeepSeek Harness and have a public repository.", "license": "License", "license_desc": "Released under the [Apache License 2.0](LICENSE).", "footer": "Submit projects or corrections on GitHub. Licensed under Apache License 2.0.",
        "categories": {"plugins": "Plugins", "integrations": "Integrations & Agents", "interfaces": "Interfaces (TUI / Desktop / Web)", "ecosystem": "Ecosystem & Marketplaces", "themes": "Themes & Skins", "other": "Other Projects"}, "category_desc": {"plugins": "Plugins that add file references, vision, memory, and other capabilities.", "integrations": "Projects connecting Harness to databases, design tools, and workflows.", "interfaces": "Clients that bring Harness to the terminal, desktop, or web.", "ecosystem": "Infrastructure for discovering, installing, and managing Harness projects.", "themes": "Themes, skins, and visual enhancements.", "other": "Related projects not yet placed in another category."}, "fallback": "No project description yet."
    },
    "zh-TW": {
        "name": "繁體中文", "title": "Awesome DeepSeek Harness", "intro": "DeepSeek Harness 外掛、工具與周邊專案精選清單。", "maintained": "本清單由 GitHub 專案資料自動維護，同時保留人工整理的中文說明。歡迎提交專案或修正分類。", "online": "線上瀏覽", "toc": "目錄", "total": "專案數", "updated": "最後更新", "auto": "自動更新", "auto_desc": "採集器會透過 GitHub Search 自動發現 DeepSeek Harness 相關儲存庫，並更新 Star 數、語言、主題與更新時間。推送至 `main` 或每日排程都會觸發更新。", "token": "你的_token", "tags": "標籤", "updated_at": "更新於", "unsynced": "未同步", "pending": "待同步", "contribute": "參與貢獻", "contribute_desc": "請先閱讀 [CONTRIBUTING.md](CONTRIBUTING.md)，再透過 Issue 或 Pull Request 提交專案。專案須與 DeepSeek Harness 直接相關，並提供公開儲存庫。", "license": "授權條款", "license_desc": "本專案採用 [Apache License 2.0](LICENSE) 發布。", "footer": "歡迎在 GitHub 提交專案或修正分類。本清單採用 Apache License 2.0。", "categories": {"plugins": "外掛", "integrations": "整合與 Agent", "interfaces": "介面（TUI / Desktop / Web）", "ecosystem": "生態與外掛市場", "themes": "主題與外觀", "other": "其他專案"}, "category_desc": {"plugins": "加入檔案引用、視覺、記憶等能力的外掛。", "integrations": "連接資料庫、設計工具與其他工作流程的專案。", "interfaces": "將 Harness 帶到終端機、桌面或 Web 的用戶端。", "ecosystem": "協助發現、安裝與管理 Harness 專案的基礎設施。", "themes": "主題、外觀與視覺增強專案。", "other": "尚未歸入其他分類的相關專案。"}, "fallback": "尚無專案簡介。"
    },
    "ja": {
        "name": "日本語", "title": "Awesome DeepSeek Harness", "intro": "DeepSeek Harness のプラグイン、ツール、周辺プロジェクトの厳選リスト。", "maintained": "GitHub のプロジェクト情報を自動更新し、人手で整理した説明も掲載しています。プロジェクトの追加や修正を歓迎します。", "online": "オンラインで見る", "toc": "目次", "total": "プロジェクト数", "updated": "最終更新", "auto": "自動更新", "auto_desc": "収集スクリプトは GitHub Search から DeepSeek Harness 関連リポジトリを発見し、Star 数、言語、トピック、更新日時を更新します。`main` への push と毎日のスケジュールで実行されます。", "token": "your_token", "tags": "タグ", "updated_at": "更新", "unsynced": "未同期", "pending": "同期待ち", "contribute": "コントリビューション", "contribute_desc": "[CONTRIBUTING.md](CONTRIBUTING.md) を読んでから、Issue または Pull Request でプロジェクトを送ってください。DeepSeek Harness に直接関連する公開リポジトリが対象です。", "license": "ライセンス", "license_desc": "[Apache License 2.0](LICENSE) の下で公開しています。", "footer": "GitHub からプロジェクトの追加や分類の修正を送信できます。Apache License 2.0。", "categories": {"plugins": "プラグイン", "integrations": "連携と Agent", "interfaces": "インターフェース（TUI / Desktop / Web）", "ecosystem": "エコシステムとマーケット", "themes": "テーマとスキン", "other": "その他"}, "category_desc": {"plugins": "ファイル参照、視覚、メモリなどを追加するプラグイン。", "integrations": "データベース、デザインツール、ワークフローと接続するプロジェクト。", "interfaces": "Harness をターミナル、デスクトップ、Web で使うためのクライアント。", "ecosystem": "Harness プロジェクトの発見、インストール、管理を支える基盤。", "themes": "テーマ、スキン、外観の拡張。", "other": "まだ別のカテゴリに分類されていない関連プロジェクト。"}, "fallback": "プロジェクトの説明はまだありません。"
    },
    "fr": {
        "name": "Français", "title": "Awesome DeepSeek Harness", "intro": "Une sélection de plugins, outils et projets associés à DeepSeek Harness.", "maintained": "Cette liste est mise à jour automatiquement depuis GitHub, avec des descriptions sélectionnées manuellement. Les ajouts et corrections sont bienvenus.", "online": "Voir en ligne", "toc": "Sommaire", "total": "Projets", "updated": "Dernière mise à jour", "auto": "Mises à jour automatiques", "auto_desc": "Le collecteur découvre les dépôts DeepSeek Harness via GitHub Search et actualise les étoiles, langages, sujets et dates. Un push sur `main` ou la planification quotidienne déclenche la mise à jour.", "token": "votre_token", "tags": "Tags", "updated_at": "Mis à jour", "unsynced": "non synchronisé", "pending": "en attente", "contribute": "Contribuer", "contribute_desc": "Lisez [CONTRIBUTING.md](CONTRIBUTING.md), puis proposez un projet via une issue ou une pull request. Le projet doit être directement lié à DeepSeek Harness et disposer d'un dépôt public.", "license": "Licence", "license_desc": "Publié sous [Apache License 2.0](LICENSE).", "footer": "Proposez des projets ou des corrections sur GitHub. Licence Apache 2.0.", "categories": {"plugins": "Plugins", "integrations": "Intégrations et agents", "interfaces": "Interfaces (TUI / Desktop / Web)", "ecosystem": "Écosystème et marchés", "themes": "Thèmes et skins", "other": "Autres projets"}, "category_desc": {"plugins": "Plugins ajoutant références de fichiers, vision, mémoire et autres fonctions.", "integrations": "Projets connectant Harness aux bases de données, outils de design et workflows.", "interfaces": "Clients pour utiliser Harness dans le terminal, sur desktop ou sur le Web.", "ecosystem": "Infrastructure pour découvrir, installer et gérer les projets Harness.", "themes": "Thèmes, skins et améliorations visuelles.", "other": "Projets associés pas encore classés ailleurs."}, "fallback": "Description du projet indisponible."
    },
    "es": {
        "name": "Español", "title": "Awesome DeepSeek Harness", "intro": "Una lista seleccionada de plugins, herramientas y proyectos relacionados con DeepSeek Harness.", "maintained": "Se actualiza automáticamente con datos de GitHub y descripciones revisadas manualmente. Se aceptan nuevos proyectos y correcciones.", "online": "Ver en línea", "toc": "Contenido", "total": "Proyectos", "updated": "Última actualización", "auto": "Actualizaciones automáticas", "auto_desc": "El recolector descubre repositorios relacionados con DeepSeek Harness mediante GitHub Search y actualiza estrellas, lenguajes, temas y fechas. Los pushes a `main` y la tarea diaria activan la actualización.", "token": "tu_token", "tags": "Etiquetas", "updated_at": "Actualizado", "unsynced": "sin sincronizar", "pending": "pendiente", "contribute": "Contribuir", "contribute_desc": "Lee [CONTRIBUTING.md](CONTRIBUTING.md) y envía un proyecto mediante una issue o pull request. Debe estar directamente relacionado con DeepSeek Harness y tener un repositorio público.", "license": "Licencia", "license_desc": "Publicado bajo [Apache License 2.0](LICENSE).", "footer": "Envía proyectos o correcciones en GitHub. Licencia Apache 2.0.", "categories": {"plugins": "Plugins", "integrations": "Integraciones y agentes", "interfaces": "Interfaces (TUI / Desktop / Web)", "ecosystem": "Ecosistema y mercados", "themes": "Temas y skins", "other": "Otros proyectos"}, "category_desc": {"plugins": "Plugins que añaden referencias de archivos, visión, memoria y otras capacidades.", "integrations": "Proyectos que conectan Harness con bases de datos, herramientas de diseño y flujos de trabajo.", "interfaces": "Clientes para usar Harness en terminal, escritorio o web.", "ecosystem": "Infraestructura para descubrir, instalar y gestionar proyectos Harness.", "themes": "Temas, skins y mejoras visuales.", "other": "Proyectos relacionados aún no clasificados."}, "fallback": "Aún no hay descripción del proyecto."
    },
    "ru": {
        "name": "Русский", "title": "Awesome DeepSeek Harness", "intro": "Подборка плагинов, инструментов и связанных проектов DeepSeek Harness.", "maintained": "Список автоматически обновляется по данным GitHub и содержит отобранные вручную описания. Предлагайте проекты и исправления.", "online": "Открыть онлайн", "toc": "Содержание", "total": "Проектов", "updated": "Обновлено", "auto": "Автообновление", "auto_desc": "Сборщик ищет репозитории DeepSeek Harness через GitHub Search и обновляет звёзды, языки, темы и даты. Обновление запускается push в `main` и ежедневным расписанием.", "token": "ваш_token", "tags": "Теги", "updated_at": "Обновлено", "unsynced": "не синхронизировано", "pending": "ожидает", "contribute": "Участие", "contribute_desc": "Прочитайте [CONTRIBUTING.md](CONTRIBUTING.md), затем предложите проект через issue или pull request. Нужен публичный репозиторий, напрямую связанный с DeepSeek Harness.", "license": "Лицензия", "license_desc": "Распространяется по [Apache License 2.0](LICENSE).", "footer": "Предлагайте проекты и исправления через GitHub. Лицензия Apache 2.0.", "categories": {"plugins": "Плагины", "integrations": "Интеграции и агенты", "interfaces": "Интерфейсы (TUI / Desktop / Web)", "ecosystem": "Экосистема и маркеты", "themes": "Темы и скины", "other": "Другие проекты"}, "category_desc": {"plugins": "Плагины для файловых ссылок, зрения, памяти и других возможностей.", "integrations": "Проекты, подключающие Harness к базам данных, дизайну и рабочим процессам.", "interfaces": "Клиенты Harness для терминала, рабочего стола и веба.", "ecosystem": "Инфраструктура для поиска, установки и управления проектами Harness.", "themes": "Темы, скины и визуальные улучшения.", "other": "Связанные проекты, ещё не отнесённые к другим категориям."}, "fallback": "Описание проекта пока отсутствует."
    },
    "pt-BR": {
        "name": "Português (Brasil)", "title": "Awesome DeepSeek Harness", "intro": "Uma lista selecionada de plugins, ferramentas e projetos relacionados ao DeepSeek Harness.", "maintained": "Mantida automaticamente com dados do GitHub e descrições revisadas manualmente. Sugestões e correções são bem-vindas.", "online": "Ver online", "toc": "Conteúdo", "total": "Projetos", "updated": "Última atualização", "auto": "Atualizações automáticas", "auto_desc": "O coletor descobre repositórios do DeepSeek Harness pelo GitHub Search e atualiza estrelas, linguagens, tópicos e datas. Pushes em `main` e o agendamento diário iniciam a atualização.", "token": "seu_token", "tags": "Tags", "updated_at": "Atualizado", "unsynced": "não sincronizado", "pending": "pendente", "contribute": "Contribuir", "contribute_desc": "Leia [CONTRIBUTING.md](CONTRIBUTING.md) e envie um projeto por issue ou pull request. Ele deve estar diretamente relacionado ao DeepSeek Harness e ter um repositório público.", "license": "Licença", "license_desc": "Publicado sob a [Apache License 2.0](LICENSE).", "footer": "Envie projetos ou correções pelo GitHub. Licença Apache 2.0.", "categories": {"plugins": "Plugins", "integrations": "Integrações e agentes", "interfaces": "Interfaces (TUI / Desktop / Web)", "ecosystem": "Ecossistema e marketplaces", "themes": "Temas e skins", "other": "Outros projetos"}, "category_desc": {"plugins": "Plugins que adicionam referências de arquivos, visão, memória e outros recursos.", "integrations": "Projetos que conectam o Harness a bancos de dados, ferramentas de design e fluxos de trabalho.", "interfaces": "Clientes para usar o Harness no terminal, desktop ou web.", "ecosystem": "Infraestrutura para descobrir, instalar e gerenciar projetos Harness.", "themes": "Temas, skins e melhorias visuais.", "other": "Projetos relacionados ainda não classificados."}, "fallback": "Ainda não há descrição do projeto."
    },
    "de": {
        "name": "Deutsch", "title": "Awesome DeepSeek Harness", "intro": "Eine kuratierte Liste von DeepSeek-Harness-Plugins, Tools und Begleitprojekten.", "maintained": "Automatisch aus GitHub-Projektdaten aktualisiert, mit redaktionell gepflegten Beschreibungen. Projekte und Korrekturen sind willkommen.", "online": "Online ansehen", "toc": "Inhalt", "total": "Projekte", "updated": "Zuletzt aktualisiert", "auto": "Automatische Updates", "auto_desc": "Der Collector findet DeepSeek-Harness-Repositories über GitHub Search und aktualisiert Sterne, Sprachen, Topics und Zeitstempel. Pushes nach `main` und der tägliche Zeitplan starten die Aktualisierung.", "token": "dein_token", "tags": "Tags", "updated_at": "Aktualisiert", "unsynced": "nicht synchronisiert", "pending": "ausstehend", "contribute": "Mitmachen", "contribute_desc": "Lies [CONTRIBUTING.md](CONTRIBUTING.md) und reiche ein Projekt per Issue oder Pull Request ein. Es muss direkt mit DeepSeek Harness verbunden sein und ein öffentliches Repository besitzen.", "license": "Lizenz", "license_desc": "Veröffentlicht unter der [Apache License 2.0](LICENSE).", "footer": "Reiche Projekte oder Korrekturen über GitHub ein. Apache License 2.0.", "categories": {"plugins": "Plugins", "integrations": "Integrationen und Agents", "interfaces": "Oberflächen (TUI / Desktop / Web)", "ecosystem": "Ökosystem und Marktplätze", "themes": "Themes und Skins", "other": "Weitere Projekte"}, "category_desc": {"plugins": "Plugins für Dateiverweise, Vision, Gedächtnis und weitere Funktionen.", "integrations": "Projekte zur Verbindung von Harness mit Datenbanken, Design-Tools und Workflows.", "interfaces": "Clients für Harness im Terminal, auf dem Desktop oder im Web.", "ecosystem": "Infrastruktur zum Finden, Installieren und Verwalten von Harness-Projekten.", "themes": "Themes, Skins und visuelle Erweiterungen.", "other": "Verwandte Projekte, die noch nicht anders eingeordnet sind."}, "fallback": "Noch keine Projektbeschreibung."
    }
}
LANGUAGE_ORDER = ["zh-CN", "en", "zh-TW", "ja", "fr", "es", "ru", "pt-BR", "de"]


def date(value: str | None, locale: str = "zh-CN") -> str:
    if not value:
        return LANGUAGES.get(locale, LANGUAGES["en"])["unsynced"]
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).strftime("%Y-%m-%d")
    except ValueError:
        return value[:10]


def stars(value: int | None, locale: str = "zh-CN") -> str:
    labels = LANGUAGES.get(locale, LANGUAGES["en"])
    return f"⭐ {value:,}" if isinstance(value, int) else f"⭐ {labels['pending']}"


def description_for(project: dict, locale: str, fallback: str) -> str:
    if locale in ("zh-CN", "zh-TW"):
        return project.get("description_zh") or project.get("description") or fallback
    return project.get("description") or fallback


def render(data: dict, locale: str = "zh-CN") -> str:
    labels = LANGUAGES.get(locale, LANGUAGES["en"])
    projects = data.get("projects", [])
    grouped = {key: [] for key in CATEGORY_ORDER}
    for project in projects:
        grouped.setdefault(project.get("category", "other"), []).append(project)
    lines = [
        "# Awesome DeepSeek Harness",
        "",
        f"> {labels['intro']}",
        "",
        "[![Auto update](https://img.shields.io/badge/auto--update-daily-blue.svg)](.github/workflows/update-projects.yml) [![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)",
        "",
        labels["maintained"],
        "",
        f"{labels['online']}：[GitHub Pages](https://rodert.github.io/awesome-deepSeek-harness/{'' if locale == 'zh-CN' else locale + '/'})",
        "",
        "**Languages / 语言:** " + " · ".join(
            f"[{value['name']}]({'README.md' if key == 'zh-CN' else f'README.{key}.md'})" for key, value in LANGUAGES.items()
        ),
        "",
        f"## {labels['toc']}",
        "",
    ]
    for category in CATEGORY_ORDER:
        if grouped.get(category):
            lines.append(f"- [{labels['categories'][category]}](#{CATEGORY_ANCHORS[category]})")
    lines += [
        "",
        f"> {labels['total']}：**{len(projects)}** · {labels['updated']}：**{date(data.get('last_updated'), locale)}**",
        "",
        f"## {labels['auto']}",
        "",
        labels["auto_desc"],
        "",
        "```bash",
        f"GITHUB_TOKEN={labels['token']} python scripts/collect_projects.py",
        "python scripts/generate_markdown.py",
        "```",
        "",
    ]
    for category in CATEGORY_ORDER:
        items = sorted(grouped.get(category, []), key=lambda item: (-(item.get("stars") or 0), item.get("name", "").lower()))
        if not items:
            continue
        lines += [f"<a id=\"{CATEGORY_ANCHORS[category]}\"></a>", f"## {labels['categories'][category]}", "", f"*{labels['category_desc'][category]}*", ""]
        for index, project in enumerate(items, 1):
            title = project.get("name") or project.get("full_name")
            description = description_for(project, locale, labels["fallback"])
            meta = " · ".join(filter(None, [stars(project.get("stars"), locale), project.get("language") or None, f"{labels['updated_at']} {date(project.get('updated_at'), locale)}" ]))
            lines += [f"### {index}. [{title}]({project['url']})", "", meta, "", description.strip(), ""]
            if project.get("topics"):
                lines += [labels["tags"] + ": " + " ".join(f"`{topic}`" for topic in project["topics"][:8]), ""]
        lines += ["---", ""]
    lines += [
        f"## {labels['contribute']}",
        "",
        labels["contribute_desc"],
        "",
        f"## {labels['license']}",
        "",
        labels["license_desc"],
        "",
    ]
    return "\n".join(lines)


def render_html(data: dict, locale: str = "zh-CN") -> str:
    labels = LANGUAGES.get(locale, LANGUAGES["en"])
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
            description = html.escape(description_for(project, locale, labels["fallback"]))
            stats = " · ".join(filter(None, [stars(project.get("stars"), locale), project.get("language") or None, f"{labels['updated_at']} {date(project.get('updated_at'), locale)}" ]))
            entries.append(f'<article><h3><a href="{url}">{title}</a></h3><p class="meta">{html.escape(stats)}</p><p>{description}</p></article>')
        cards.append(f'<section id="{CATEGORY_ANCHORS[category]}"><h2>{html.escape(labels["categories"][category])}</h2><p class="muted">{html.escape(labels["category_desc"][category])}</p>{"".join(entries)}</section>')
    updated = html.escape(date(data.get("last_updated"), locale))
    language_links = " ".join(f'<a href="https://rodert.github.io/awesome-deepSeek-harness/{"" if key == "zh-CN" else key + "/"}">{html.escape(value["name"])}</a>' for key, value in LANGUAGES.items())
    return f'''<!doctype html>
<html lang="{locale}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(labels["title"])}</title>
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
  <header><h1>{html.escape(labels["title"])}</h1><p class="lead">{html.escape(labels["intro"])}</p><p class="muted">{html.escape(labels["total"])}：{len(projects)} · {html.escape(labels["updated"])}：{updated}</p></header>
  <nav>{"".join(f'<a href="#{CATEGORY_ANCHORS[key]}">{html.escape(labels["categories"][key])}</a>' for key in CATEGORY_ORDER if grouped.get(key))}</nav>
  <p class="muted">{language_links}</p>
  {"".join(cards)}
  <footer>{html.escape(labels["footer"])}</footer>
</main></body></html>\n'''


def main() -> None:
    root = Path(__file__).parent.parent
    with (root / "data" / "projects.json").open(encoding="utf-8") as handle:
        data = json.load(handle)
    content = render(data, "zh-CN")
    (root / "README.md").write_text(content, encoding="utf-8")
    docs = root / "docs" / "projects.md"
    docs.parent.mkdir(parents=True, exist_ok=True)
    docs.write_text(content, encoding="utf-8")
    (root / "docs" / "index.html").write_text(render_html(data, "zh-CN"), encoding="utf-8")
    for locale in LANGUAGE_ORDER:
        if locale == "zh-CN":
            continue
        readme_suffix = {"pt-BR": "pt-BR", "zh-TW": "zh-TW"}.get(locale, locale)
        (root / f"README.{readme_suffix}.md").write_text(render(data, locale), encoding="utf-8")
        locale_dir = root / "docs" / locale
        locale_dir.mkdir(parents=True, exist_ok=True)
        (locale_dir / "projects.md").write_text(render(data, locale), encoding="utf-8")
        (locale_dir / "index.html").write_text(render_html(data, locale), encoding="utf-8")
    print(f"generated {len(LANGUAGE_ORDER)} languages ({len(data.get('projects', []))} projects)")


if __name__ == "__main__":
    main()
