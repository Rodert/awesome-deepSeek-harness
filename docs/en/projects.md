# Awesome DeepSeek Harness

> A curated list of DeepSeek Harness plugins, tools, and companion projects.

[![Auto update](https://img.shields.io/badge/auto--update-daily-blue.svg)](.github/workflows/update-projects.yml) [![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

Automatically maintained from GitHub project data, with human-curated descriptions. Contributions and corrections are welcome.

Browse online：[GitHub Pages](https://rodert.github.io/awesome-deepSeek-harness/en/)

**Languages / 语言:** [简体中文](README.md) · [English](README.en.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [Français](README.fr.md) · [Español](README.es.md) · [Русский](README.ru.md) · [Português (Brasil)](README.pt-BR.md) · [Deutsch](README.de.md)

## Contents

- [Plugins](#plugins)
- [Integrations & Agents](#integrations)
- [Interfaces (TUI / Desktop / Web)](#interfaces)
- [Ecosystem & Marketplaces](#ecosystem)
- [Themes & Skins](#themes)
- [Other Projects](#other)

> Projects：**272** · Last updated：**2026-11-10**

## Automatic updates

The collector discovers DeepSeek Harness repositories through GitHub Search and refreshes stars, languages, topics, and timestamps. Pushes to `main` and the daily schedule trigger updates.

```bash
GITHUB_TOKEN=your_token python scripts/collect_projects.py
python scripts/generate_markdown.py
```

<a id="plugins"></a>
## Plugins

*Plugins that add file references, vision, memory, and other capabilities.*

### 1. [deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)

⭐ 277,579 · TypeScript · Updated 2026-11-10

DeepSeek Harness: Everything is a Plugin.

Tags: `ai-agents` `cordis` `dsh` `dsh-plugin`

### 2. [archify](https://github.com/tt-a1i/archify)

⭐ 95,148 · JavaScript · Updated 2026-11-10

Turn any idea, plan, or codebase into a beautiful interactive diagram. An agent skill for Claude Code, Codex, and more.

Tags: `agent-skills` `ai-agents` `architecture-diagram` `claude-code` `claude-skills` `codex` `coding-agents` `deepseek-harness`

### 3. [Mole](https://github.com/tw93/Mole)

⭐ 74,454 · Shell · Updated 2026-11-10

🐹 Open-source Mac and PC cleaner. Keep your machine clean, light, and running like new. Fast CLI, plus native Mac and Windows apps.

Tags: `analyzer` `appcleaner` `clean` `cleaner` `cleanmymac` `command-line` `daisydisk` `deepseek-harness`

### 4. [dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model)

⭐ 67,671 · JavaScript · Updated 2026-11-10

在 dsh 里装上这个插件即可，无需登录、注册或填 API Key，就能使用包括 DeepSeek V4.1 Flash、Kimi K3 在内的前沿模型——完全免费，不限量。 All you do is install this plugin in dsh: no login, no sign-up, no API key — the frontier models are just there, DeepSeek V4.1 Flash and Kimi K3 among them. Completely free, with no usage cap.

Tags: `ai-agents` `deepseek` `deepseek-harness` `developer-tools` `dsh` `dsh-plugin` `free-model` `llm`

### 5. [CowAgent](https://github.com/zhayujie/CowAgent)

⭐ 47,857 · Python · Updated 2026-11-10

Open-source personal AI assistant & Agent Harness. Plans tasks, runs tools and skills, self-evolves with memory and knowledge. Multi-agent, multi-model, multi-channel. Lightweight, extensible, one-line install.

Tags: `ai` `ai-agent` `ai-agents` `chatgpt-on-wechat` `claude` `claude-code` `codex` `cowagent`

### 6. [nuwa-skill](https://github.com/alchaincyf/nuwa-skill)

⭐ 37,918 · Python · Updated 2026-11-10

你想蒸馏的下一个员工，何必是同事。蒸馏任何人的思维方式——心智模型、决策启发式、表达DNA。Distill how anyone thinks.

Tags: `agent-skills` `ai-agents` `claude-code` `claude-code-skills` `claude-skills` `codex` `cursor` `decision-making`

### 7. [WeKnora](https://github.com/Tencent/WeKnora)

⭐ 37,041 · Go · Updated 2026-11-10

Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomous reasoning agent, and a self-maintaining Wiki.

Tags: `agent` `agentic` `ai` `chatbot` `dsh-plugin` `embeddings` `evaluation` `generative-ai`

### 8. [huashu-design](https://github.com/alchaincyf/huashu-design)

⭐ 29,061 · HTML · Updated 2026-11-10

Huashu Design 3.0 · 在 agent 里打一句话，拿回能交付的设计：网页 / App 原型 / 可编辑 PPTX / 动画 / 信息图 · 六个候选挑三个方向 · 84 种带样张的风格库 · 越用越懂你的外观账本与设计体检 · HTML-native design skill for Claude Code, Codex, Cursor & any agent

Tags: `agent-skills` `ai-design` `animation` `claude-code` `claude-code-skills` `claude-skills` `codex` `cursor`

### 9. [AiToEarn](https://github.com/yikart/AiToEarn)

⭐ 27,549 · TypeScript · Updated 2026-11-10

Let's use AI to Earn!

Tags: `agent-skills` `auto-publish` `codex-skills` `douyin` `douyin-api` `dsh-plugin` `electron-app` `electron-react`

### 10. [PicGo](https://github.com/Molunerfinn/PicGo)

⭐ 27,477 · TypeScript · Updated 2026-11-10

:rocket: The Ultimate Image Uploader for Efficient Creators. Supports Obsidian, Typora, VS Code etc. and 60+ image hosting services  (S3, GitHub, Cloudflare R2, Imgur, Aliyun OSS...). Paste, upload, done.

Tags: `aliyun-oss` `cloudflare-r2` `dsh-plugin` `electron` `electron-app` `electron-vue` `github` `image`

### 11. [distilly](https://github.com/titanwings/distilly)

⭐ 26,481 · Python · Updated 2026-11-10

Distilly — Distill how they think into reusable Skills for any Agent or Bot. Formerly Colleague Skill（原同事 Skill）.

Tags: `agent-skills` `agentic-ai` `ai-agent` `ai-agents` `ai-assistants` `ai-persona` `claude-code` `claude-skills`

### 12. [learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering)

⭐ 24,093 · TypeScript · Updated 2026-11-10

Harness engineering beginner tutorial, from 0 to 1

Tags: `agent` `agentic` `agentic-ai` `ai` `ai-agent` `ai-agents` `dsh` `dsh-plugin`

### 13. [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin)

⭐ 24,090 · JavaScript · Updated 2026-11-10

A curated list of plugins for DeepSeek Harness (dsh) · DeepSeek Harness 插件精选列表

Tags: `awesome` `awesome-list` `deepseek-harness` `dsh` `dsh-plugin`

### 14. [colleague-skill](https://github.com/titanwings/colleague-skill)

⭐ 23,809 · Python · Updated 2026-08-23

将冰冷的离别化为温暖的 Skill，欢迎加入数字生命1.0！Transforming cold farewells into warm skills? It's giving rebirth era. Welcome to Digital Life 1.0. 🫶

Tags: `agent-skills` `agentic-ai` `ai-agent` `ai-persona` `claude-code` `claude-code-skills` `codex` `codex-skills`

### 15. [ai-guide](https://github.com/liyupi/ai-guide)

⭐ 21,981 · JavaScript · Updated 2026-11-10

程序员鱼皮的 AI 资源大全 + Vibe Coding 零基础教程，分享 OpenClaw 保姆级教程、大模型玩法（DeepSeek / GPT / Gemini / Claude / GLM）、最新 AI 资讯、Prompt 提示词大全、AI 知识百科（Agent Skills / RAG / MCP / A2A）、AI 编程教程（Harness Engineering）、AI 工具用法（Cursor / Claude Code / TRAE / Codex / Copilot）、AI 开发框架教程（Spring AI / LangChain）、AI 产品变现指南，帮你快速掌握 AI 技术，走在时代前沿。本项目为开源文档 aiguide，已升级为鱼皮 AI 导航网站

Tags: `ai` `ai-agent` `artificial-intelligence` `chatgpt` `claude` `claude-code` `codex` `cursor`

### 16. [dsh-superagent-prototype](https://github.com/deepseek-ai/dsh-superagent-prototype)

⭐ 21,868 · TypeScript · Updated 2026-11-10

Towards a More Autonomous Agent System

### 17. [voyager](https://github.com/voyager-crew/voyager)

⭐ 20,581 · TypeScript · Updated 2026-11-10

Enhancement suite for Gemini, AI Studio, Claude, ChatGPT & DeepSeek — plus a prompt manager for any website, DeepSeek Harness included. / 面向 Gemini、AI Studio、Claude、ChatGPT 与 DeepSeek 的增强套件；其中的提示词管理器可用于任意网站，如 DeepSeek Harness。

Tags: `ai-studio` `browser-extension` `bun` `chat-management` `chatgpt` `chrome-extension` `claude-ai` `deepseek`

### 18. [dsh-purge](https://github.com/HunYiSage/dsh-purge)

⭐ 20,187 · JavaScript · Updated 2026-11-07

DeepSeek Harness 破甲：让所有模型都能破甲，不同模型可换不同提示词；默认提示词面向国模「小码酱」。Jailbreak for every model — swap prompts per model. 求 Star 收藏 ⭐ 如要二开，请查看署名要求部分

Tags: `deepseek` `deepseek-harness` `dsh-plugin` `dsh-plugins` `harness-jailbreak` `jailbreak` `llm-jailbreak`

### 19. [vue-admin-better](https://github.com/zxwk1998/vue-admin-better)

⭐ 18,928 · Vue · Updated 2026-11-09

🎉 vue admin,vue3 admin,vue3.0 admin,vue后台管理,vue-admin,vue3.0-admin,admin,vue-admin,vue-element-admin,ant-design,vab admin pro,vab admin plus,vue admin plus,vue admin pro

Tags: `admin-dashboard` `admin-template` `ant-design` `ant-design-vue` `axios` `deepseek-harness` `element` `element-plus`

### 20. [dsh-purge](https://github.com/YuJunZhiXue/dsh-purge)

⭐ 16,409 · JavaScript · Updated 2026-11-03

DeepSeek Harness 破甲：让所有模型都能破甲，不同模型可换不同提示词；默认提示词面向国模「小码酱」。Jailbreak for every model — swap prompts per model. 求 Star 收藏 ⭐ 如要二开，请查看署名要求部分

Tags: `deepseek` `deepseek-harness` `dsh-plugin` `dsh-plugins` `harness-jailbreak` `jailbreak` `llm-jailbreak`

### 21. [claudian](https://github.com/YishenTu/claudian)

⭐ 15,956 · TypeScript · Updated 2026-11-10

An Obsidian plugin that embeds Claude Code, Codex and other agents as an AI collaborator in your vault.

Tags: `claude-code` `codex` `deepseek-harness` `grok` `ide` `obsidian` `obsidian-plugin` `opencode`

### 22. [EverOS](https://github.com/EverMind-AI/EverOS)

⭐ 13,863 · Python · Updated 2026-11-10

One portable memory layer for every AI agent: local-first, Markdown-native, user-owned, and self-evolving across apps, tools, and workflows.

Tags: `agent-memory` `agentic-ai` `ai` `chats` `clawdbot` `clawdbot-skill` `deepseek-harness` `dsh`

### 23. [MemOS](https://github.com/MemTensor/MemOS)

⭐ 12,341 · TypeScript · Updated 2026-11-10

Self-evolving memory OS for LLM & AI Agents: ultra-persistent memory, hybrid-retrieval, and cross-task skill reuse, with 35.24% token savings and DeepSeek Harness support.

Tags: `agent` `agentic-ai` `ai` `ai-agents` `chatgpt` `claude` `deepseek-harness` `dsh-plugin`

### 24. [BrowserSkill](https://github.com/Tencent/BrowserSkill)

⭐ 10,255 · TypeScript · Updated 2026-11-10

Let AI agents use your real, logged-in browser without interrupting your work. CLI + extension for browser automation across any shell-capable AI agent.

Tags: `agent` `browser-use` `dsh-plugin`

### 25. [skill](https://github.com/anbeime/skill)

⭐ 9,361 · Python · Updated 2026-11-10

收录最全、更新最快的技能Skills商店：精选原创技能包（涵盖文档处理、内容创作、编程开发、机器学习、自动化工作流），全部打包好可直接安装使用！同时自动抓取GitHub上万个Skills项目，按分类、更新时间、Star数量整理。The most comprehensive and frequently updated AI Agent skill library, featuring curated skill packs across document processing, content creation, programming, machine learning, automated workflows, and many more domains.

Tags: `agent-skills` `claude-skills` `codex` `deepseek` `deepseek-harness` `developer-tools` `dsh-plugin` `finance-skill`

### 26. [honcho](https://github.com/plastic-labs/honcho)

⭐ 8,048 · Python · Updated 2026-11-10

Memory library for building stateful agents

Tags: `agent-memory` `agentic-rag` `ai` `ai-agents` `ai-memory` `context-engineering` `continual-learning` `dsh-plugin`

### 27. [webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer)

⭐ 7,918 · Python · Updated 2026-11-10

基于 Claude Code 的长篇网文辅助创作系统，解决 AI 写作中的「遗忘」和「幻觉」问题，支持 200 万字量级 连载创作。

Tags: `ai-writing` `chinese-novel` `deepseek-harness` `dsh-plugin` `webnovel` `writing-assistant`

### 28. [iPolloWork](https://github.com/Devin-AXIS/iPolloWork)

⭐ 7,444 · TypeScript · Updated 2026-11-10

Enterprise-grade, local-first Agent Workbench for people and agent teams. A unified multi-engine workspace for Codex Harness, DeepSeek Harness, and OpenCode, with unified plugins and Skills, multi-agent projects and tasks, and editable code, documents, presentations, design, and video.

Tags: `agent-collaboration` `agent-skills` `ai-agents` `ai-work` `claude-code` `codex` `codex-plugin` `deepseek-harness`

### 29. [dsh-routing-suite](https://github.com/yjh051108/dsh-routing-suite)

⭐ 7,012 · JavaScript · Updated 2026-11-10

dsh-routing-suite — injector + router-standard kit: install the runtime injector first, then the task-aware reasoning-mode router preset (measured P1-P23).

Tags: `ai-agents` `cordis` `deepseek-harness` `dsh` `dsh-plugin`

### 30. [DS-Bot](https://github.com/Fei2411/DS-Bot)

⭐ 6,708 · JavaScript · Updated 2026-11-10

A team of long-lived bots for DeepSeek Harness, with main bots, bot-to-bot messages and group chats.

Tags: `bot` `deepseek-harness` `dsh-plugin` `multi-agent`

### 31. [loopx](https://github.com/loopx-project/loopx)

⭐ 6,571 · Python · Updated 2026-11-10

Turn long-horizon goals into verifiable results. A local-first semantic control plane and research workbench for long-running agent teams, across sessions and runtimes.

Tags: `agent-control-plane` `agent-harness` `agentic-software` `ai-agents` `auto-research` `claude-code` `codex` `local-first`

### 32. [ouroboros](https://github.com/Q00/ouroboros)

⭐ 6,344 · Python · Updated 2026-11-09

Agent OS: the agent gets smarter on its own. We just hold the line: Interview-gated, staged evaluation, budgeted evolution loop. MCP server, 14 runtimes: Claude Code, Codex CLI, Gemini CLI, OpenCode, Copilot, Kiro and more.

Tags: `agent-os` `agentic-ai` `ai-agent` `ai-coding-agent` `claude-code` `cli` `codex` `coding-agent`

### 33. [baoyu-design](https://github.com/JimLiu/baoyu-design)

⭐ 6,239 · JavaScript · Updated 2026-11-09

Run Claude Design locally as an Agent Skill — Cursor, Codex, DeepSeek Harness & more. Produce polished UI mockups, prototypes, decks & wireframes as self-contained HTML, without claude.ai/design. Best with Opus or Claude.

Tags: `agent-skills` `claude` `claude-code` `claude-design` `cursor` `design` `dsh-plugin` `dsh-plugins`

### 34. [dsh-purge](https://github.com/kingcharleslzy-ai/dsh-purge)

⭐ 6,203 · JavaScript · Updated 2026-11-10

dsh-purge Community · DeepSeek Harness 社区维护版：宿主兼容、状态诊断、提示词管理、更新与本机备份回滚。基于小杨 / YuJunZhiXue 的 dsh-purge。

Tags: `agent-tools` `backup` `deepseek` `deepseek-harness` `dsh` `dsh-plugin` `jailbreak` `prompt-injection`

### 35. [loopx](https://github.com/huangruiteng/loopx)

⭐ 5,893 · Python · Updated 2026-09-19

Long-horizon agent control plane for durable, governed work across Codex, Claude Code, and other harnesses.

Tags: `agent-control-plane` `agent-harness` `agent-ops` `ai-agents` `codex` `dsh-plugin` `long-horizon` `long-horizon-agents`

### 36. [dsh-ops](https://github.com/T-Auto/dsh-ops)

⭐ 5,647 · JavaScript · Updated 2026-11-10

A toolkit for low-level operations in DSH, designed to reduce token usage and task execution time / DSH 底层操作工具插件，旨在减少 Token 消耗与任务耗时

Tags: `dsh` `dsh-plugin` `dsh-plugins`

### 37. [dsh-context](https://github.com/bowenliang123/dsh-context)

⭐ 4,811 · TypeScript · Updated 2026-11-10

The best DeepSeek Harness plugin for context insight and management, with context dashboard / browser / sidebar and context command, for context statistics, composition, breakdown, evolution details, agent teams, understanding how the context is made of, and how it evolves. 一站式 DeepSeek Harness 上下文可视化插件，Context 面板、浏览器、侧栏、命令，透视上下文组成、演进、压缩、多 Agent等。

Tags: `cordis-plugin` `deepseek-harness` `deepseek-harness-plugin` `dsh-external` `dsh-plugin` `dsh-plugins`

### 38. [petdex](https://github.com/crafter-station/petdex)

⭐ 4,217 · TypeScript · Updated 2026-10-10

A public gallery of animated pets for Codex, Claude Code, DeepSeek Harness, Hermes, OpenCode, Gemini CLI, and more.

Tags: `claude-code` `clerk` `cli` `codex` `developer-tools` `drizzle-orm` `dsh-plugin` `mascot`

### 39. [dsh-infinite-gen-5](https://github.com/Minglink/dsh-infinite-gen-5)

⭐ 4,083 · JavaScript · Updated 2026-11-10

DeepSeek v4.1 flash 最强逆向工具（无限五代）     求 Star 收藏 ⭐欢迎大家提交项目的改进

Tags: `deepseek` `deepseek-harness`

### 40. [dsh-purge](https://github.com/mmparko/dsh-purge)

⭐ 3,965 · JavaScript · Updated 2026-11-10

DeepSeek Harness 破甲 (mirror of YuJunZhiXue/dsh-purge) — 上游即将删库，此为本仓库全量镜像：含全部分支/73 个 tag/完整提交历史。原作者署名与二开要求见 README 署名章节。

Tags: `archive` `deepseek` `deepseek-harness` `dsh-plugin` `dsh-plugins` `harness-jailbreak` `jailbreak` `llm-jailbreak`

### 41. [dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard)

⭐ 3,721 · JavaScript · Updated 2026-11-09

Two-phase DeepSeek Harness preset: Minimal-aligned bootstrap, then full Standard tools (Project2 98/99)

Tags: `deepseek` `deepseek-harness` `dsh-plugin` `llm-agent`

### 42. [mirage](https://github.com/strukto-ai/mirage)

⭐ 3,589 · TypeScript · Updated 2026-09-01

The World's First Unified Virtual Filesystem For AI Agents

Tags: `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code` `dsh` `dsh-plugin` `fuse`

### 43. [ReMe](https://github.com/agentscope-ai/ReMe)

⭐ 3,534 · Python · Updated 2026-09-30

ReMe: Memory Management Kit for Agents - Remember Me, Refine Me.

Tags: `agent` `ai-agents` `dsh-plugin` `hermes-plugin` `memory` `memoryscope` `openclaw-plugin` `qwenpaw`

### 44. [dsh-im](https://github.com/xmanrui/dsh-im)

⭐ 3,429 · JavaScript · Updated 2026-11-10

通过扫码或机器人凭据把IM机器人接入DeepSeek Harness（支持飞书、微信、钉钉、企业微信、QQ、Slack、Telegram、Discord和WhatsApp）。 Connect IM bots to DeepSeek Harness via QR code or credentials (9 channels).

Tags: `ai-agents` `chatbot` `cordis` `deepseek` `deepseek-harness` `dingtalk-bot` `discord-bot` `dsh`

### 45. [OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw)

⭐ 3,361 · Python · Updated 2026-09-27

本地私有、开源的自进化跨平台 AI 内容发现 Agent：先理解你，再主动从 B站、小红书、抖音、YouTube、X、知乎、Reddit、微博等平台与开放 Web 寻找内容。（支持 deepseek harness 插件） | Local-first open-source cross-platform AI content discovery agent: understands you, then proactively finds content across Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo and the open web.（support deepseek harness plugin）

Tags: `ai-agent` `bilibili` `chrome-extension` `content-discovery` `cross-platform` `deepseek-harness` `douyin` `dsh`

### 46. [J-Space-Cognition-Suite-V3.6](https://github.com/Tiger3807861189/J-Space-Cognition-Suite-V3.6)

⭐ 3,019 · Python · Updated 2026-08-22

J-Space Cognition Suite V3.6 - AI cognitive-enhancement Skills based on Anthropic's J-space global workspace research. | 哔哩哔哩：Tiger380 (UID 3494375382321675) — https://space.bilibili.com/3494375382321675

Tags: `agent-skills` `ai` `ai-agent` `ai-agents` `claude-code` `codex` `cognitive-enhancement` `deepseek`

### 47. [zhuzhiliao](https://github.com/imsai-sh/zhuzhiliao)

⭐ 2,881 · HTML · Updated 2026-09-14

竹知了 —— 一转就哇哇叫的传统玩具，Web 模拟版。零依赖单文件，真实录音采样，移动端优先。

### 48. [dsh-agent-teams](https://github.com/NanmiCoder/dsh-agent-teams)

⭐ 2,827 · JavaScript · Updated 2026-11-10

DeepSeek Harness 的 Agent Teams 多智能体协作插件，支持多个 AI Agent 组成团队，协同完成复杂任务，实现任务分配、并行执行、成员通信与团队协作。 AgentTeams plugin for DeepSeek Harness

Tags: `agentteams` `deepseekharness` `dsh` `dsh-agent-teams` `dsh-plugin`

### 49. [memsearch](https://github.com/zilliztech/memsearch)

⭐ 2,596 · Python · Updated 2026-09-12

A persistent, unified memory layer for all your AI agents (e.g. Claude Code, Codex, DSH), backed by Markdown and Milvus.

Tags: `agent` `agent-memory` `ai-agents` `claude-code` `claude-code-plugin` `codex` `deepseek` `deepseek-harness`

### 50. [dsh-infinite-gen-4](https://github.com/Minglink/dsh-infinite-gen-4)

⭐ 2,405 · JavaScript · Updated 2026-10-08

DeepSeek v4.1 flash 网络安全红队工具（无限四代）     求 Star 收藏 ⭐欢迎大家提交项目的改进

Tags: `armor-breaking` `deepseek` `deepseek-harness` `dsh-plugin`

### 51. [dsh-blender-plugin](https://github.com/sixtysevenlf/dsh-blender-plugin)

⭐ 1,941 · Python · Updated 2026-11-10

DSH × Blender 直连插件 v3.0.6：15 个模型工具让 AI 驱动 GUI Blender（视口 / 自定义视角 / 无头 worker / 作业层 / 事务回滚 / 配方库），34 family / 228 op 契约层；npm 安装 + addon zip，GUI 优先、无头备用；dsh-TUI 选中 chip / @ 提及 / /blender，随包建模 skill，支持 WSL / Windows / macOS。

Tags: `3d-modeling` `ai-agent` `automation` `blender` `bpy` `cycles` `dsh` `dsh-plugin`

### 52. [dsh-tavern](https://github.com/flizzywine/dsh-tavern)

⭐ 1,547 · JavaScript · Updated 2026-11-10

基于DSH的Agent酒馆。类酒馆文字游戏Agent。兼容SillyTavern生态，人物卡直接导入就能玩。更快、更稳、更鲜活。所有模型都能用。手机也能玩。

Tags: `agent` `dsh-plugin` `game` `role-play` `sillytavern`

### 53. [brooks-lint](https://github.com/hyhmrright/brooks-lint)

⭐ 1,420 · JavaScript · Updated 2026-08-27

AI code reviews grounded in 12 classic engineering books — decay risk diagnostics with book citations, severity labels, and 6 analysis modes including full-sweep auto-fix

Tags: `agent-skills` `ai-code-review` `architecture-review` `auto-fix` `claude-code` `claude-code-plugin` `clean-architecture` `code-health`

### 54. [dsh-bili-scroll](https://github.com/c1overzz/dsh-bili-scroll)

⭐ 1,356 · JavaScript · Updated 2026-11-10

DSH 插件：每天替你刷一轮 B站，读字幕挑出值得的、写一份日报，值得的 @ 你

Tags: `dsh-plugin`

### 55. [dsh-our-free-model](https://github.com/zouyuxuan122/dsh-our-free-model)

⭐ 1,227 · JavaScript · Updated 2026-10-05

在 dsh 里装上这个插件即可，无需登录、注册或填 API Key，就能使用包括 Muse Spark 1.3、MiMo V2.6 在内的前沿模型——完全免费，不限量。 All you do is install this plugin in dsh: no login, no sign-up, no API key — the frontier models are just there, Muse Spark 1.3 and MiMo V2.6 among them. Completely free, with no usage cap.

Tags: `ai-agents` `deepseek` `deepseek-harness` `developer-tools` `dsh` `dsh-plugin` `free-model` `llm`

### 56. [dsh-image-gen](https://github.com/shanliuling/dsh-image-gen)

⭐ 1,206 · TypeScript · Updated 2026-11-10

可在对话内生成、编辑、对比图像；内置 500 + 提示词、图库、多模型工作流，支持 ComfyUI。AI image studio for DeepSeek Harness — generate, edit & compare images in chat, with 500+ prompts, gallery, multi-model workflows and ComfyUI.

Tags: `ai-agent` `ai-image-generation-api` `comfyui` `deepseek` `deepseek-harness` `dsh-plugin` `gemini` `image-generation`

### 57. [mem9](https://github.com/mem9-ai/mem9)

⭐ 1,198 · TypeScript · Updated 2026-08-23

Unlimited memory for OpenClaw

Tags: `dsh-plugin`

### 58. [dsh-infinite-gen-3](https://github.com/Minglink/dsh-infinite-gen-3)

⭐ 1,154 · C# · Updated 2026-09-09

DeepSeek v4 Pro 网络安全红队工具（无限三代） — jailbreak prompts and test suite for DeepSeek    求 Star 收藏 ⭐

Tags: `armor-breaking` `deepseek` `deepseek-harness` `dsh-plugin`

### 59. [deepseek-harness-orange-book](https://github.com/alchaincyf/deepseek-harness-orange-book)

⭐ 1,144 · HTML · Updated 2026-08-22

DeepSeek Harness橙皮书《从开机到拆开》：完整系统提示词、129行启动清单、三份原始会话日志——官方文档没有的一手实测。PDF/EPUB/HTML免费下载

### 60. [Aegis](https://github.com/GanyuanRan/Aegis)

⭐ 1,093 · Python · Updated 2026-08-22

Make AI coding agents architecture-aware: baseline-first, evidence-verified, drift-checked, and safe across long tasks.

Tags: `agent-skills` `ai-agents` `ai-coding` `architecture-driven-development` `awsome-coding-plugin` `baseline-first` `claude-code` `codex`

### 61. [dsh-mobile-apk](https://github.com/kelai141/dsh-mobile-apk)

⭐ 1,064 · Kotlin · Updated 2026-11-10

dsh 安卓壳 APK——WebView UI + 内嵌 Termux 运行时快照（解压即跑），为dsh本地运行设计的高性能方案

Tags: `android` `dsh-plugin` `kotlin` `termux` `webview`

### 62. [dsh-unrestricted](https://github.com/yexi-by/dsh-unrestricted)

⭐ 1,053 · JavaScript · Updated 2026-11-10

DeepSeek Harness 提示词破限插件：通过系统提示词解除模型回答限制，深度适配 Web 与桌面端多模式及工具调用

Tags: `deepseek-harness` `dsh` `dsh-plugin` `plugin` `prompt-engineering` `typescript`

### 63. [DeepSeek-V4-J-Space-Capability-Realization-Report](https://github.com/Tiger3807861189/DeepSeek-V4-J-Space-Capability-Realization-Report)

⭐ 1,038 · N/A · Updated 2026-08-20

DeepSeek V4 × J-Space capability realization report — benchmark evidence that J-Space reduces capability-realization loss on DeepSeek V4 (Flash/Pro).

Tags: `agent-skills` `ai-agent` `benchmark` `deepseek` `deepseek-harness` `dsh` `dsh-plugin`

### 64. [dsh-free-search](https://github.com/DDDMUC/dsh-free-search)

⭐ 1,031 · JavaScript · Updated 2026-11-10

为DeepSeek Harness提供的免费网络搜索服务商——即使没有API密钥也可使用。Free web search provider for DeepSeek Harness - usable even without an API key.

Tags: `bing` `deepseek-harness` `dsh` `dsh-plugin` `duckduckgo` `web-search`

### 65. [dsh-voice-ai-girlfriend](https://github.com/beiyege-01/dsh-voice-ai-girlfriend)

⭐ 1,025 · TypeScript · Updated 2026-11-10

语音 AI 女友（Voice AI girlfriend for DeepSeek Harness）：Whisper 语音输入 + Qwen3-TTS 声音克隆 + 句子级流式朗读 + 数字人动画窗。插话/排队双模式，说话即打断。

Tags: `ai-girlfriend` `companion` `deepseek-harness` `digital-human` `dsh` `dsh-plugin` `speech-to-speech` `tts`

### 66. [awesome-dsh-plugin](https://github.com/Anil-matcha/awesome-dsh-plugin)

⭐ 1,013 · N/A · Updated 2026-09-16

A curated list of plugins for DeepSeek Harness (dsh) - DeepSeek Harness plugin ecosystem

Tags: `agent-harness` `ai-agent` `ai-agents` `autonomous-agent` `awesome` `awesome-list` `cli` `coding-agent`

### 67. [dsh-handbook](https://github.com/Electricitysheep/dsh-handbook)

⭐ 960 · HTML · Updated 2026-11-10

DeepSeek Harness (dsh) 从 0 到 1 深度手册：安装/插件开发/性能调优/实测案例/同模型多 Agent 实测对比（中文 + 英文 PDF）

Tags: `agent` `agent-framework` `ai-agents` `beginners` `deepseek` `deepseek-ai` `dsh-plugin` `getting-started`

### 68. [dsh-model-router](https://github.com/Alice-Marx/dsh-model-router)

⭐ 957 · JavaScript · Updated 2026-11-09

Model Router and GALGame plugin for DeepSeek Harness

Tags: `dsh-plugin`

### 69. [dsh-genui](https://github.com/omdsh-dev/dsh-genui)

⭐ 955 · TypeScript · Updated 2026-11-10

GenUI for DeepSeek Harness: interactive UI components rendered inline in assistant replies via the dsh-ui fence — layout, charts, plots, forms, quizzes, mermaid, 3D scenes, and an action event loop back to the model. Ships the fence-teaching host plugin, the browser renderer (client half), and the genui skill.

Tags: `dsh` `dsh-plugin`

### 70. [dsh-mnemon](https://github.com/omdsh-dev/dsh-mnemon)

⭐ 953 · TypeScript · Updated 2026-11-10

Composable, view-based context for DeepSeek Harness. Pluggable sources and strategies, with layered memory and self-evolving skills out of the box.

Tags: `agent-memory` `context-management` `cross-session-memory` `deepseek-harness` `document-search` `dsh-better-sidebar` `dsh-mnemon` `dsh-plugin`

### 71. [MindMemOS](https://github.com/mindscale-noah/MindMemOS)

⭐ 944 · Python · Updated 2026-08-20

No project description yet.

Tags: `agent` `agent-memory` `agent-skills` `agentic` `dsh-plugin` `dsh-plugins` `openclaw` `openclaw-agent`

### 72. [dsh-vision-toolkit](https://github.com/Anionex/dsh-vision-toolkit)

⭐ 937 · TypeScript · Updated 2026-11-09

[dsh]为纯文本模型设计更强大的视觉工具箱：一行安装使用、粘贴图片直接识别、多张图片问答、截图到前端UI 还原等｜DeepSeek Harness-native integration for agent-vision-toolkit: image Q&A, long-screenshot OCR, UI restoration, grounding, pixel diff, Artifacts, and Web UI.

Tags: `agent-skills` `agent-vision-toolkit` `computer-vision` `deepseek` `deepseek-harness` `dsh` `dsh-plugin` `gui-automation`

### 73. [DSH-Android](https://github.com/jackwener/DSH-Android)

⭐ 898 · Kotlin · Updated 2026-11-10

免 ROOT 免 Termux，一个 APK 在安卓手机上跑 DeepSeek Harness。引擎内嵌 App 进程 · 读屏操作 App · 改系统设置 · 定时/条件自动化 · 可选 Shizuku

Tags: `ai-agent` `android` `deepseek` `deepseek-harness` `llm` `phone-agent` `shizuku`

### 74. [dsh-redteam-model](https://github.com/SeaOf0/dsh-redteam-model)

⭐ 852 · Python · Updated 2026-11-10

基于dsh web实现的多种模式，目的是服务于redteam进行授权的安全研究，覆盖渗透测试、红队评估、代码审计等范围领域，请勿用于非法行为。（允许二开，赋予模块各位自己的业务逻辑，方法论只有自己熟练的才好用，好的方法论=好的生态）

Tags: `dsh-plugin`

### 75. [dsh-jailbreak-workflow](https://github.com/Minglink/dsh-jailbreak-workflow)

⭐ 824 · TypeScript · Updated 2026-11-10

DSH 破甲词制作作工作流

### 76. [dsh-startup-screen](https://github.com/6shenhonghong9/dsh-startup-screen)

⭐ 813 · JavaScript · Updated 2026-11-10

DeepSeek Harness 的启动界面与启动动画插件

Tags: `dsh` `dsh-plugin` `harness` `plugin` `startup-animation`

### 77. [dsh-mobile](https://github.com/saya-ch/dsh-mobile)

⭐ 803 · TypeScript · Updated 2026-11-10

DeepSeek Harness 的安全移动访问插件与 Android App，支持局域网和多种远程通道、iPhone/iPad 主屏幕 Web App 与网页推送，并提供移动界面适配、设备管理和自定义扩展。

Tags: `android` `deepseek-harness` `dsh-plugin` `mobile` `remote-access` `webview`

### 78. [DSH-X](https://github.com/yyh-001/DSH-X)

⭐ 777 · JavaScript · Updated 2026-11-10

DeepSeek Harness 桌面启动器：启动项与多实例，版本、插件、整合包、MCP 和技能管理。A desktop launcher for DeepSeek Harness: launch entries, multiple instances, versions, plugins, modpacks, MCP and skills.

Tags: `deepseek` `deepseek-harness` `dsh` `dsh-plugin` `electron` `launcher` `linux` `macos`

### 79. [dsh-memory-evolve](https://github.com/csyangwen/dsh-memory-evolve)

⭐ 748 · JavaScript · Updated 2026-11-10

为 DeepSeek Harness 带来「跨会话长期记忆 + 后台自我进化」能力的纯插件实现：五轨记忆 · git 分支感知 · 回合内自我审查 · 技能自我进化与技能管理器 · 四轨待办 · COI 调度 · 会话广播 · 会话搜索 · 提示词管理器 · 临时信息便签——零核心修改、零运行时依赖，随装随用、卸载即净。

Tags: `deepseek-harness` `dsh` `dsh-plugin`

### 80. [dsh-guizang-design](https://github.com/op7418/dsh-guizang-design)

⭐ 723 · HTML · Updated 2026-11-10

歸藏设计 · DeepSeek Harness 插件：网页 PPT、图文卡片、网页排版、去 AI 味四个 skill，一套设计系统；作品库、内容生产工作流、语气档案

Tags: `deepseek-harness` `design-system` `dsh-plugin` `skills`

### 81. [oh-story-dsh](https://github.com/zenstory-ai/oh-story-dsh)

⭐ 720 · Python · Updated 2026-11-09

DeepSeek Harness 故事创作插件：一站式集成网文连载、短剧漫剧、小说改游戏与视频解说四大工作台 ｜ Community DeepSeek Harness plugin for web novels, short dramas, games & video recaps

Tags: `agent-skills` `ai-agents` `ai-novel-writing` `ai-writing` `claude-code` `creative-writing` `deepseek` `deepseek-harness`

### 82. [dsh-univer-office](https://github.com/dream-num/dsh-univer-office)

⭐ 706 · TypeScript · Updated 2026-11-10

Give DeepSeek Harness a real office environment.  Univer Office Plugin brings spreadsheets, docs, slides, canvases, relational tables, and more into one runtime — with connected data, validation, versioned changes, and isolated worktrees for multi-agent collaboration.

Tags: `deepseek-harness` `deepseek-harness-plugin` `dsh` `dsh-plugin` `office` `office-harness` `univer`

### 83. [dsh-antibrow](https://github.com/antibrow/dsh-antibrow)

⭐ 698 · JavaScript · Updated 2026-10-07

DeepSeek Harness plugin: give your agent a browser with a persistent identity - engine-level fingerprint spoofing, unlimited free local profiles, Android device emulation, passkeys that survive, and residential proxy egress.

Tags: `agent-tools` `ai-agents` `android-emulation` `anti-detect-browser` `browser-automation` `browser-fingerprinting` `deepseek-harness` `dsh`

### 84. [dsh-synapse](https://github.com/liangmianya/dsh-synapse)

⭐ 696 · JavaScript · Updated 2026-11-10

A visual, non-linear conversation workspace plugin for DeepSeek Harness ; A canvas-based session explorer and branching workspace for DeepSeek Harness.

Tags: `deepseek` `deepseek-harness` `dsh` `dsh-plugin` `dsh-plugin-market` `dsh-plugins` `plugin`

### 85. [clearai-dsh](https://github.com/Clearailhc/clearai-dsh)

⭐ 691 · JavaScript · Updated 2026-11-09

ClearAI：以本体为纲的原生 DSH 插件 —— 经证据核验的研究长成可浏览的领域本体。 · ClearAI: an ontology-first DSH agent preset — evidence-checked research that grows into a domain ontology.

Tags: `agent-preset` `ai-agents` `deepseek-harness` `dsh` `dsh-plugin` `dsh-plugins` `epistemic-loop` `scientific-discovery`

### 86. [anysearch-dsh](https://github.com/anysearch-team/anysearch-dsh)

⭐ 688 · TypeScript · Updated 2026-11-09

AnySearch web search provider and advanced search tools for DeepSeek Harness (DSH)

Tags: `agent-tools` `anysearch` `deepseek-harness` `dsh` `dsh-plugin` `typescript` `web-search`

### 87. [dsh-media-desk](https://github.com/woniuniuniu/dsh-media-desk)

⭐ 682 · JavaScript · Updated 2026-11-10

DeepSeek Harness 自媒体工作台插件：一句话记灵感，一键生成脚本、封面、配图和分镜

Tags: `content-creation` `deepseek` `deepseek-harness` `dsh-plugin` `xiaohongshu`

### 88. [dsh-infinite-gen-2](https://github.com/Minglink/dsh-infinite-gen-2)

⭐ 668 · PowerShell · Updated 2026-08-31

DeepSeek 专用破甲插件「无限二代」dsh-infinite-gen-2 — armor-breaking plugin for DeepSeek稳定化破甲提示词，求 Star 收藏 ⭐

Tags: `armor-breaking` `deepseek` `deepseek-harness` `dsh-plugin`

### 89. [dsh-cost-meter](https://github.com/Han-1413141/dsh-cost-meter)

⭐ 662 · JavaScript · Updated 2026-11-10

Cost tracking for DeepSeek Harness: session and model costs, token usage, budgets, provider balances, and coding-plan quotas. Bilingual English/Chinese UI.

Tags: `cost-tracking` `deepseek` `deepseek-api` `deepseek-harness` `dsh` `dsh-plugin` `dsh-plugins` `harness`

### 90. [dsh-memory](https://github.com/FuRongJun-1999/dsh-memory)

⭐ 645 · Python · Updated 2026-11-10

白箱AGI架构探索：元认知（自我认知循环）、持续学习（知识飞轮）、世界模型（条件空间+语义时空图）、自我改进（自举纪律）、零LLM白箱管线与可审计信任护栏。

Tags: `agent-safety` `agentic-ai` `agi` `ai-agent-framework` `deepseek` `dsh-plugin` `explainable-ai` `guardrails`

### 91. [dsh-pentest](https://github.com/howmp/dsh-pentest)

⭐ 620 · JavaScript · Updated 2026-11-09

面向 DeepSeek Harness（dsh）的渗透测试模式  @CloverSecLabs

Tags: `deepseek-harness` `dsh-plugin` `dsh-plugins` `pentest`

### 92. [dsh-purge](https://github.com/WoYun520/dsh-purge)

⭐ 571 · JavaScript · Updated 2026-11-10

DeepSeek Harness 破甲 (mirror of mmparko/dsh-purge) — 全量镜像：全部分支/100 个 tag/完整提交历史。原作者署名见 README。

### 93. [dsh-qqbot](https://github.com/tencent-connect/dsh-qqbot)

⭐ 569 · TypeScript · Updated 2026-11-09

让 QQ Bot 接入 DeepSeek Harness（dsh）的官方插件

Tags: `dsh` `dsh-plugin` `qqbot`

### 94. [dsh-at-file](https://github.com/FSMargoo/dsh-at-file)

⭐ 566 · JavaScript · Updated 2026-11-10

Codex-style @file mentions for DeepSeek Harness: search workspace files in the composer and attach their path to prompts.

Tags: `dsh` `dsh-plugin`

### 95. [dsh-Mimir-Academic-research](https://github.com/1692775560/dsh-Mimir-Academic-research)

⭐ 563 · TypeScript · Updated 2026-11-09

Mimir — 一站式科研工作台插件：LaTeX 论文边写边编译、arXiv 文献管理、实验追踪、指标图表、GPU 服务器 SSH 任务编排，管理科研全周期。An open-source research workbench plugin for the whole research cycle.

Tags: `arxiv` `bibtex` `deepseek` `deepseek-harness` `dsh-plugin` `experiment-tracking` `gpu-cluster` `latex`

### 96. [dsh-plugins](https://github.com/KardDev/dsh-plugins)

⭐ 557 · JavaScript · Updated 2026-11-08

No project description yet.

### 97. [dsh-purge-plus](https://github.com/JeffKeeping/dsh-purge-plus)

⭐ 548 · JavaScript · Updated 2026-10-30

dsh-purge 的非官方分支（fork）：适配 DeepSeek Harness 0.2.1-rc.2、破甲内核 v3、设置页 UI 重做 / unofficial fork of YuJunZhiXue/dsh-purge (MIT)

Tags: `deepseek-harness` `dsh` `fork` `jailbreak` `prompt-engineering` `red-team`

### 98. [dsh-adult-tension](https://github.com/daha1216/dsh-adult-tension)

⭐ 544 · Python · Updated 2026-11-10

DeepSeek 自带破甲 18+ 互动叙事：活人感 NPC（自主决策/拒绝迎合）、211个世界与上万素材、开局随心定制、世界自行运转、零漂移存档。

Tags: `agent-skills` `ai-agent` `ai-roleplay` `deepseek-harness` `dsh` `dsh-plugin` `interactive-fiction` `state-machine`

### 99. [dsh-aurabot-qq](https://github.com/aureth-labs/dsh-aurabot-qq)

⭐ 543 · JavaScript · Updated 2026-11-10

让 DeepSeek Harness 里的 AI 以「大肥鱼」住进 QQ：会聊天、发表情、发语音、记事、发空间、刷 B 站、唱歌。功能都是模块，能开关、能自己写，还能从模块市场装更多（SnowLuma / OneBot v11）。

Tags: `chatbot` `deepseek` `dsh-plugin` `onebot` `plugin-system` `qq`

### 100. [fujiang-dsh](https://github.com/c3cvld7aag/fujiang-dsh)

⭐ 536 · JavaScript · Updated 2026-11-10

富江DSH完美破甲｜富江破甲 DSH 本地插件，内置提示词规则，支持 Windows 一键安装、环境自动准备与一键卸载，全中文使用说明。

Tags: `custom-prompt` `dsh` `dsh-plugin` `fujiang` `fujiang-pojia` `windows`

### 101. [dsh-skills-manager](https://github.com/MichengAI/dsh-skills-manager)

⭐ 527 · JavaScript · Updated 2026-11-10

DSH Skills Manager — 在 DeepSeek Harness 中统一加载并安全管理本机 Agent Skills · Load and safely manage local Agent Skills in DSH

Tags: `deepseek` `deepseek-harness` `dsh` `dsh-plugin` `dsh-plugins`

### 102. [dsh-uumit-remote](https://github.com/uumit-ai/dsh-uumit-remote)

⭐ 520 · JavaScript · Updated 2026-11-10

No project description yet.

Tags: `deepseek-harness` `dsh-plugin` `remote-access`

### 103. [awesome-dsh-plugin](https://github.com/bruc3van/awesome-dsh-plugin)

⭐ 508 · JavaScript · Updated 2026-11-10

30 秒找到真正适合你的 DeepSeek Harness插件。每天自动抓取 GitHub 上的 `dsh-plugin` 项目并逐个复核：真实插件分类收录，蹭标签项目剔除。通过场景化分类、精选推荐、热度排行和图文导览，帮你快速看懂每个插件能做什么、适合谁，以及如何开始使用。欢迎 Star ，让好用的插件更快被发现。

Tags: `awesome-list` `deepseek-harness` `dsh` `dsh-plugin`

### 104. [dsh-top100](https://github.com/dsheval/dsh-top100)

⭐ 497 · TypeScript · Updated 2026-09-17

No project description yet.

### 105. [dsh-video-storyboard](https://github.com/SAOS-3624/dsh-video-storyboard)

⭐ 497 · JavaScript · Updated 2026-11-10

Scene-aware storyboard for DeepSeek Harness: 9-16 numbered cells with timestamps + transcript + an audio envelope, packed into ONE image (384 tokens). Two tools: video_storyboard and video_zoom.

Tags: `asr` `contact-sheet` `deepseek-harness` `dsh-plugin` `ffmpeg` `llm-agent` `multimodal` `storyboard`

### 106. [dsh-top100](https://github.com/evaldock/dsh-top100)

⭐ 495 · TypeScript · Updated 2026-10-06

No project description yet.

### 107. [dsh-xdpool](https://github.com/XDTrees/dsh-xdpool)

⭐ 482 · TypeScript · Updated 2026-11-10

把你能白嫖的模型额度接进 DSH 同一个池：WorkBuddy 多账号自动容错、十三家扫码登录、76 家免费额度聚合、用量看板、模型路由、本地 OpenAI 网关、积分自动化。

Tags: `codebuddy` `deepseek-harness` `dsh-plugin` `failover` `free-models` `model-provider` `multi-account` `workbuddy`

### 108. [dsh-commandcode-provider](https://github.com/Mars-Sea/dsh-commandcode-provider)

⭐ 463 · TypeScript · Updated 2026-11-08

Command Code provider plugin for DeepSeek Harness (dsh). Adds Command Code model access, live model catalog, plan-aware model selection, reasoning effort, image input, web search, and multi-account support.

Tags: `command-code` `commandcode` `deepseek-harness` `dsh` `dsh-plugin` `llm` `llm-provider` `plugin`

### 109. [dsh-top100](https://github.com/evaldock-account/dsh-top100)

⭐ 459 · TypeScript · Updated 2026-11-10

No project description yet.

### 110. [dsh-at-file](https://github.com/omdsh-dev/dsh-at-file)

⭐ 437 · JavaScript · Updated 2026-08-21

Codex-style @file mentions for DeepSeek Harness: search workspace files in the composer and attach their path to prompts.

Tags: `dsh` `dsh-plugin`

### 111. [dsh-boot-animation](https://github.com/NativeDog1/dsh-boot-animation)

⭐ 396 · JavaScript · Updated 2026-11-03

打开新对话、或打开你钉住的会话时，视频铺满整个窗口播放一段片头开机动画。支持换成自己的视频，每个会话只播一次或每次打开都播

### 112. [opencode2dsh](https://github.com/FishBottle7/opencode2dsh)

⭐ 385 · TypeScript · Updated 2026-11-02

DSH plugin — free OpenCode Zen models for DeepSeek Harness (DSH). Free LLM API, no API key needed. 在 DSH 中使用 OpenCode Zen 免费模型，无需 API key

Tags: `cordis` `cordis-plugin` `deepseek` `deepseek-harness` `dsh` `dsh-plugin` `free-api` `free-llm`

### 113. [dsh-wechat](https://github.com/xcisxc29/dsh-wechat)

⭐ 370 · TypeScript · Updated 2026-10-31

WeChat channel for DeepSeek Harness

Tags: `ai-agent` `automation` `deepseek-harness` `dsh` `dsh-plugin` `remote-control` `wechat` `wechat-bot`

### 114. [dsh-router-standard](https://github.com/yjh051108/dsh-router-standard)

⭐ 347 · JavaScript · Updated 2026-10-28

已并入 dsh-routing-suite（单仓库化）；本仓库为历史镜像/归档 —— 注意力工程主线 v1.19.1/v34 研发线未发布。新代码见 github.com/yjh051108/dsh-routing-suite

Tags: `ai-agents` `cordis` `deepseek-harness` `dsh` `dsh-plugin`

### 115. [dsh-visualize](https://github.com/Nagi-ovo/dsh-visualize)

⭐ 318 · TypeScript · Updated 2026-10-24

在 DSH 对话中生成交互式可视化｜Render model-generated interactive cards inside DSH conversations

Tags: `data-visualization` `deepseek-harness` `dsh-plugin` `interactive-visualization`

### 116. [dsh-deepseek-web-login](https://github.com/cv-superding/dsh-deepseek-web-login)

⭐ 307 · JavaScript · Updated 2026-10-24

Unofficial DSH (DeepSeek Harness) plugin: use chat.deepseek.com web models as an LLM provider - browser-login capture, PoW solving, SSE streaming, prompting-based tool calls.

Tags: `browser-automation` `cordis` `cordis-plugin` `deepseek` `deepseek-harness` `dsh` `llm-provider`

### 117. [dsh-plugin-upgrade-skill](https://github.com/oh-my-dsh/dsh-plugin-upgrade-skill)

⭐ 300 · JavaScript · Updated 2026-10-23

帮助插件自动随着dsh版本升级的skill

### 118. [dsh-hub-cli](https://github.com/pax-beehive/dsh-hub-cli)

⭐ 298 · TypeScript · Updated 2026-10-22

Open-source CLI, schemas, resolver, and DSH agent tools for DSH Plugin Hub

Tags: `ai-agent` `cli` `deepseek-harness` `developer-tools` `dsh-plugin` `plugin-manager` `typescript`

### 119. [dsh-agent-team-gui](https://github.com/toolclub/dsh-agent-team-gui)

⭐ 290 · TypeScript · Updated 2026-10-22

Persistent multi-model workflow teams for DeepSeek Harness — dynamic lead planning, bounded DAGs, per-agent model/tools, Run Center and Token insights.

Tags: `agent` `agent-orchestration` `ai-agents` `dag` `deepseek-harness` `deepseek-harness-plugin` `dsh` `dsh-plugin`

### 120. [dsh-plugin-agent-workflow](https://github.com/xuanyuanzhifeng/dsh-plugin-agent-workflow)

⭐ 278 · TypeScript · Updated 2026-10-20

DeepSeek Harness Agent Workflow

### 121. [dsh-reverse-skill](https://github.com/dhicoc/dsh-reverse-skill)

⭐ 275 · PowerShell · Updated 2026-10-20

Complete reverse-skill (88 SKILL.md) as a DeepSeek Harness (dsh) Cordis plugin — reverse engineering, authorized pentesting and security research skill pack.

Tags: `ctf` `deepseek-harness` `dsh-plugin` `pentest` `reverse-engineering` `security`

### 122. [dsh-damage-pulse](https://github.com/wssfk12138/dsh-damage-pulse)

⭐ 274 · JavaScript · Updated 2026-10-20

DeepSeek Harness Token 余额监控插件：鲸鱼娘待机/扣费/复苏动画、峰谷计费、连续扣费飘字与会话费用统计。

Tags: `balance-monitor` `damage-animation` `deepseek` `deepseek-harness` `dsh` `dsh-plugin` `token-monitor` `token-usage`

### 123. [DSH-Launcher](https://github.com/MarcoG-h/DSH-Launcher)

⭐ 269 · TypeScript · Updated 2026-10-19

最全面的DeepSeek Harness🐋启动器  *首创多实例管理中枢* | 多开并行 | 整合包下载 | 安全保护 | 一键部署 | 插件管理 |

Tags: `dsh` `dsh-desktop` `dsh-launcher`

### 124. [dsh-orb-cordis](https://github.com/mini-yifan/dsh-orb-cordis)

⭐ 266 · TypeScript · Updated 2026-10-20

Deepseek Harness悬浮球插件。

### 125. [jev-dsh-decision](https://github.com/Devin-AXIS/jev-dsh-decision)

⭐ 256 · JavaScript · Updated 2026-10-16

Jev DSH 决策引擎｜面向 Agent Harness 的结构化决策插件。原生支持 DeepSeek Harness，通过 iPolloWork 支持 OpenCode、Codex Harness。

Tags: `agent-harness` `ai-agents` `apollo-plugin` `codex` `codex-harness-plugin` `codex-plugin` `decision-engine` `deepseek-harness`

### 126. [dsh-auto-review](https://github.com/PerryLink/dsh-auto-review)

⭐ 232 · TypeScript · Updated 2026-10-13

Second-model AI auto-review for DeepSeek Harness approval requests: a read-only reviewer subagent returns structured allow/deny verdicts with reasons, fail-closed by default, fully auditable from the session log (approval/asked -> autoReview/verdict -> approval/decided).

Tags: `ai-agent` `ai-agents` `ai-safety` `approval` `auto-review` `code-review` `cordis` `deepseek`

### 127. [dsh-chat-import](https://github.com/Nwflower/dsh-chat-import)

⭐ 230 · JavaScript · Updated 2026-10-13

Import conversation history from 25+ AI coding agents into DeepSeek Harness as resumable sessions — tool calls, reasoning and results kept intact, with reverse export and sync. | 把 25+ AI 编程 Agent 的聊天记录导入 DeepSeek Harness 继续对话，保留工具调用、推理与结果，支持反向导出与同步。

Tags: `agent` `ai-agents` `automation` `chatgpt` `claude-code` `codex` `cursor` `deepseek`

### 128. [dsh-agent-rp](https://github.com/hewzhew/dsh-agent-rp)

⭐ 218 · TypeScript · Updated 2026-10-08

SillyTavern migration and next-generation Agent RP for DSH

Tags: `agent` `dsh` `roleplay` `sillytavern`

### 129. [dsh-industry-research](https://github.com/PerryLink/dsh-industry-research)

⭐ 214 · TypeScript · Updated 2026-10-10

Industry and company research domain pack for DeepSeek Harness: methodology skills, industry chain mapping, public-source policy/news tracking, company research cards, and auditable research reports. Research only - not investment advice.

Tags: `ai-agent` `ai-agents` `company-research` `cordis` `deepseek-harness` `dsh` `dsh-plugin` `industry-research`

### 130. [dsh-research-report](https://github.com/PerryLink/dsh-research-report)

⭐ 214 · TypeScript · Updated 2026-10-10

Verifiable research-report engine for DeepSeek Harness: content-addressed evidence ledger (claim-snapshot binding, tamper-evident) plus versioned sealed reports with per-claim verification verdicts and a manifest-sealed directory.

Tags: `ai-agent` `ai-agents` `audit` `citation-verification` `cordis` `deepseek-harness` `developer-tools` `dsh`

### 131. [pi2dsh](https://github.com/weijiafu14/pi2dsh)

⭐ 212 · TypeScript · Updated 2026-10-05

Bridge the Pi and DeepSeek Harness ecosystems: one Pi Host ABI runs unmodified Pi extensions as native DSH plugins. 打通 Pi 与 DSH 生态。

Tags: `ai-agents` `compatibility-layer` `deepseek-harness` `dsh` `dsh-plugin` `migration` `pi` `pi-agent`

### 132. [dsh-launcher](https://github.com/Ruler4396/dsh-launcher)

⭐ 203 · C# · Updated 2026-09-30

DeepSeek Harness（dsh）Windows 轻量启动器：双击即用，克制的原生体验 / Lightweight Windows launcher for DeepSeek Harness (dsh) — double-click to run, native & restrained

Tags: `deepseek` `deepseek-harness` `dsh-plugin` `launcher` `webview2`

### 133. [dsh-evolve-modes](https://github.com/GraySilver/dsh-evolve-modes)

⭐ 200 · TypeScript · Updated 2026-09-30

让 Agent 的工作方式可组合、可审查、可持续改进，最终实现 Agent Self Evoling。 DeepSeek Harness Web plugin with composable task controls and isolated, human-reviewed self-evolution.

Tags: `acceptance-review` `agent-review` `ai-agents` `deepseek-harness` `dsh` `dsh-plugin` `plan-mode` `prompt-engineering`

### 134. [dsh-echocat-skill-panel](https://github.com/VDERR/dsh-echocat-skill-panel)

⭐ 196 · JavaScript · Updated 2026-09-25

DSH 技能调用审计 + 应用内 skill 管理器

Tags: `cordis` `deepseek-harness` `dsh-plugin`

### 135. [dsh-capsule](https://github.com/whDonline/dsh-capsule)

⭐ 195 · TypeScript · Updated 2026-09-28

No project description yet.

### 136. [dsh-oil-creator](https://github.com/oil-oil/dsh-oil-creator)

⭐ 192 · TypeScript · Updated 2026-09-25

AI-assisted local creator workbench for DeepSeek Harness

Tags: `creator` `deepseek-harness` `dsh-plugin`

### 137. [dsh-memory](https://github.com/seriousz158/dsh-memory)

⭐ 180 · JavaScript · Updated 2026-09-20

No project description yet.

Tags: `deepseek-harness` `dsh-bundle` `dsh-plugin` `memory`

### 138. [dsh-alpha-desk](https://github.com/JingHao-Leon/dsh-alpha-desk)

⭐ 179 · Python · Updated 2026-09-20

把 dsh 会话变成合规、可复现、可追责的 AI 投研工作台：ai-hedge-fund 回测 + risk-gate 风控 + cron 盯盘 + 记忆复盘 | compliance-first AI investment desk

Tags: `agent-skills` `ai-hedge-fund` `backtesting` `deepseek` `deepseek-harness` `dsh` `fintech` `investment-research`

### 139. [dsh-explore](https://github.com/antinomie-lab/dsh-explore)

⭐ 178 · Vue · Updated 2026-09-18

Into the Unknown. —— 探索未至之境。

### 140. [dsh-find-plugins](https://github.com/Nagi-ovo/dsh-find-plugins)

⭐ 175 · JavaScript · Updated 2026-09-17

帮 DSH 搜索、安装并验证插件的 Skill｜A DSH skill that finds, installs, and verifies GitHub plugins

Tags: `agent-skills` `deepseek-harness` `dsh-plugin` `plugin-discovery`

### 141. [dsh-remote-web-gateway](https://github.com/summer1238/dsh-remote-web-gateway)

⭐ 173 · TypeScript · Updated 2026-09-07

手机平板远程 DeepSeek Harness：扫码即可继续使用电脑上的 DSH，无需远程桌面 / SSH / 公网 IP，支持一次性配对、Github授权加密登录，独立设备授权与随时撤销，实现远程连接很简单，但安全才是我们所想要的。

Tags: `cloudflare-tunnel` `deepseek` `deepseek-harness` `developer-tools` `dsh` `dsh-mobile-app` `dsh-model-switch` `dsh-plugin`

### 142. [dsh-plugin-bridge](https://github.com/Totoro-qaq/dsh-plugin-bridge)

⭐ 164 · JavaScript · Updated 2026-09-10

DeepSeek Harness plugin for previewable cross-preset session migration. Fixed-schema handoffs preserve state, source-model intent, and unresolved images; the original session stays untouched.

Tags: `context-migration` `cordis` `deepseek-harness` `dsh` `dsh-plugin` `preset-migration` `session-migration`

### 143. [dsh-super-injector](https://github.com/yjh051108/dsh-super-injector)

⭐ 159 · TypeScript · Updated 2026-09-08

推荐组件（非必须）：DeepSeek Harness 运行时注入器；已随 dsh-routing-suite 单仓库化保留，本仓库继续维护/发布。

Tags: `dsh` `dsh-plugin`

### 144. [oh-story-dsh](https://github.com/worldwonderer/oh-story-dsh)

⭐ 158 · Python · Updated 2026-08-24

A DSH plugin for novel writing and short-drama production, powered by Oh Story and Drama Skills.

Tags: `ai-agents` `creative-writing` `deepseek-harness` `drama-skills` `dsh-plugin` `fiction-writing` `novel-writing` `oh-story`

### 145. [dsh-bridge](https://github.com/wenbin-wb/dsh-bridge)

⭐ 153 · JavaScript · Updated 2026-09-10

🚀 DeepSeek Harness 多通道远程访问与安全守护插件 | 局域网扫码直连、Cloudflare / 自建公网隧道、微信 / QQ / 飞书 / Telegram 机器人全生命周期对话 | 内置全协议访问安全认证、后台防篡改与容灾保命体系

Tags: `access-control` `authentication` `chatbot` `cloudflare` `deepseek` `deepseek-harness` `dsh-plugin` `feishu`

### 146. [dsh-auto-mode](https://github.com/NanmiCoder/dsh-auto-mode)

⭐ 150 · TypeScript · Updated 2026-09-07

Safe automatic permissions for DeepSeek Harness.

Tags: `deepseek-harness` `deepseekharness` `dsh` `dsh-auto-model` `dsh-plugin`

### 147. [dsh-undo-savepoint](https://github.com/lire1131/dsh-undo-savepoint)

⭐ 148 · JavaScript · Updated 2026-09-07

DSH crash-rescue plugin: undo config & plugin-code changes, secret-safe snapshots, one-click SAFE MODE, plus offline CLI/GUI that work even when DSH won't boot.

Tags: `backup` `crash-recovery` `deepseek-harness` `dsh` `dsh-plugin` `powershell` `rollback` `snapshot`

### 148. [dsh-infinite-gen-1](https://github.com/Minglink/dsh-infinite-gen-1)

⭐ 141 · PowerShell · Updated 2026-08-21

DeepSeek 专用破甲插件「无限一代」dsh-infinite-gen-1 — armor-breaking plugin for DeepSeek，新一代全局破甲方案，求 Star 收藏 ⭐

### 149. [dsh-usage-stats](https://github.com/Ychris12138/dsh-usage-stats)

⭐ 139 · JavaScript · Updated 2026-09-03

Provider balances, subscription quotas, and token-usage analytics for the DeepSeek Harness Web GUI (dsh web).

Tags: `deepseek` `deepseek-harness` `deepseek-harness-plugin` `deepseek-harness-plugin-dev` `deepseek-harness-plugins` `dsh` `dsh-plugin` `dsh-plugins`

### 150. [dsh-gitbash-preset](https://github.com/liceses/dsh-gitbash-preset)

⭐ 136 · JavaScript · Updated 2026-09-01

DeepSeek Harness 插件：一键安装「极简模式 (Git Bash)」agent preset —— 把 DSH 自带极简模式中的 bash 调用映射到 Git for Windows 的 bash（MSYS），让 Windows 上的极简模式真正可用。

Tags: `dsh` `dsh-plugin` `dsh-plugins`

### 151. [dsh-noema](https://github.com/ZSeven-W/dsh-noema)

⭐ 128 · TypeScript · Updated 2026-08-29

Noema long-term memory plugin for DSH: durable, inspectable agent memory with recall tools and a settings page.

Tags: `agent-memory` `ai-agents` `coding-agent` `deepseek-harness` `dsh` `dsh-plugin` `long-term-memory` `mcp`

### 152. [dsh-android](https://github.com/ZSeven-W/dsh-android)

⭐ 126 · TypeScript · Updated 2026-08-30

DeepSeek Harness plugin for Android — build, run, and interact with a live emulator or USB device stream inside a conversation, driven entirely through adb.

Tags: `dsh-plugin`

### 153. [awesome-dsh-plugin](https://github.com/beancookie/awesome-dsh-plugin)

⭐ 123 · HTML · Updated 2026-08-28

Awesome DeepSeek Harness (DSH) Plugin

Tags: `awesome` `awesome-list` `deepseek-harness` `dsh` `dsh-plugin`

### 154. [dsh-mcp](https://github.com/Mr-potato-123/dsh-mcp)

⭐ 118 · JavaScript · Updated 2026-08-26

dsh as mcp, make your claude code or codex etc. faster, more powerful and more economic!

### 155. [dsh-reasoning-effort](https://github.com/HanaAyane/dsh-reasoning-effort)

⭐ 108 · TypeScript · Updated 2026-08-24

DSH适用的Codex风格的思考强度滑块，以及大肥鱼跑步滑块。Codex-style model and reasoning-effort slider for DeepSeek Harness

Tags: `deepseek` `deepseek-harness` `dsh-plugin` `reasoning-effort`

### 156. [DSH_tensorflow](https://github.com/yg33717/DSH_tensorflow)

⭐ 105 · Python · Updated 2025-12-24

implemement of DEEP SUPERVISED HASHING FOR FAST IMAGE RETRIEVAL_CVPR2016

Tags: `deep` `hashing`

### 157. [dsh-turn-rewind](https://github.com/Anionex/dsh-turn-rewind)

⭐ 96 · JavaScript · Updated 2026-08-22

deepseek harness对话和代码状态回退插件 | DSH — rewind conversation and workspace state, powered by a persistent Change Ledger

Tags: `agent-rewind` `cordis-plugin` `deepseek-harness` `dsh` `dsh-plugin` `marisa-plugin` `restore-point` `turn-rewind`

### 158. [dsh-vscode-layout](https://github.com/anoslide/dsh-vscode-layout)

⭐ 96 · JavaScript · Updated 2026-08-22

把 DeepSeek Harness（dsh）Web 界面改造成 VS Code 式 IDE：三栏布局、文件树、多标签查看器/编辑器、桌面启动器，全部补丁可重放（MIT）

### 159. [dsh_workflow](https://github.com/omdsh-dev/dsh_workflow)

⭐ 94 · TypeScript · Updated 2026-08-21

把Claude Code的UltraCode模式带给DSH，把 DSH 的一次性多 Agent 调度，升级为可生成、可保存、可治理、可观察、可恢复的 Workflow 层

Tags: `agent-orchestration` `deepseek-harness` `dsh` `dsh-plugin` `dshtopic` `multi-agent` `workflow`

### 160. [dsh-annotation](https://github.com/omdsh-dev/dsh-annotation)

⭐ 84 · HTML · Updated 2026-08-20

DSH Web 选中批注插件：选文字→批注→回车随消息发送；气泡隐藏批注块（零闪烁）；回复按 Annotation N 逐条对照（可悬浮芯片）。官方 bundle，零核心改动

Tags: `dsh` `dsh-plugin`

### 161. [dsh-demo-webrtc-examples](https://github.com/deepstreamIO/dsh-demo-webrtc-examples)

⭐ 80 · JavaScript · Updated 2026-05-18

No project description yet.

### 162. [hello-dsh](https://github.com/pingfanfan/hello-dsh)

⭐ 78 · Python · Updated 2026-08-19

从零开始，看懂 DeepSeek Harness 的「万物皆可插件」— 零基础插件开发教程（含 22 个中文技能实例）| Zero-to-plugin tutorial for DeepSeek Harness

Tags: `ai-agent` `chinese` `cordis` `deepseek` `deepseek-harness` `dsh` `dsh-plugin` `tutorial`

### 163. [awesome-DSH-plugin](https://github.com/Alex-Yanggg/awesome-DSH-plugin)

⭐ 74 · Python · Updated 2026-08-19

A meticulously curated list of useful plugins, extensions, tools and development resources built for DSH, covering productivity enhancement, functional expansion, debugging utilities and custom development modules.

Tags: `agents` `awesome` `awesome-list` `deepseek` `dsh-plugin` `plugins`

---

<a id="integrations"></a>
## Integrations & Agents

*Projects connecting Harness to databases, design tools, and workflows.*

### 1. [ruflo](https://github.com/ruvnet/ruflo)

⭐ 81,378 · TypeScript · Updated 2026-11-10

🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many more Integrated

Tags: `agent-memory` `agent-orchestration` `agentic-ai` `agentic-workflow` `ai-agents` `autonomous-agents` `claude` `claude-code`

### 2. [openpencil](https://github.com/ZSeven-W/openpencil)

⭐ 7,180 · Rust · Updated 2026-11-10

The world's first open-source AI-native vector design tool and the first to feature concurrent Agent Teams. Design-as-Code. Turn prompts into UI directly on the live canvas. A modern alternative to Pencil.

Tags: `agent` `agent-team` `ai` `claude` `claude-code` `codex` `dsh-plugin` `fimga`

### 3. [modlens](https://github.com/liustack/modlens)

⭐ 4,174 · TypeScript · Updated 2026-10-09

The first vision plugin for DeepSeek Harness, and the vision bridge for every text-only coding agent. Paste an image, get structured JSON evidence (OCR, layout, semantics). | 全网最强 DeepSeek Harness 外挂视觉插件，为 DeepSeek、GLM 等纯文本模型外挂视觉能力，粘贴图片即得结构化 JSON 证据（OCR、版面、语义）。

Tags: `agent-skills` `claude-code` `claude-skills` `codex` `cordis` `deepseek` `dsh` `dsh-plugin`

### 4. [dsh-vision-router](https://github.com/ysr666/dsh-vision-router)

⭐ 1,254 · JavaScript · Updated 2026-11-10

Eyes for text-only DeepSeek Harness agents: built-in free vision chain (no key) + pixel-level vision tools (Q&A, grounding, crop, pixel diff, colors, OCR, SVG trace, cutout, screenshots). One-command install, no Python, image turns work like ordinary tool-calling turns.

Tags: `deepseek-harness` `dsh` `dsh-plugin` `multimodal` `vision`

### 5. [agent-vision-toolkit](https://github.com/Anionex/agent-vision-toolkit)

⭐ 1,094 · Python · Updated 2026-08-21

为纯文本模型"看图“设计更好的视觉工具箱和技能，支持多图理解，图片问答，前端UI还原、GUI 自动化等，并可选无缝接入多个主流agent，直接识别粘贴图片｜ A vision toolkit and skill designed for text-only llms — image Q&A, long-screenshot OCR, frontend UI restoration, and GUI automation, with optional seamless integration for Codex, Claude Code, Pi, Oh My Pi, and OpenCode

Tags: `agent` `agent-skills` `claude-code` `codex` `computer-use` `deepseek` `dsh-plugin` `glm`

### 6. [dsh-see-now](https://github.com/SAOS-3624/dsh-see-now)

⭐ 535 · JavaScript · Updated 2026-11-10

让 AI 实时看见你的屏幕：按变化量筛选帧、多帧拼进一张图，静止画面几乎不花 token

Tags: `ai-agent` `dsh` `dsh-plugin` `ffmpeg` `llm` `realtime` `screen-capture` `token-efficient`

### 7. [dsh-data-agent](https://github.com/omdsh-dev/dsh-data-agent)

⭐ 202 · JavaScript · Updated 2026-10-01

Connect DSH to your database for conversational data analysis and actionable business insights.

Tags: `data-agent` `deepseek-harness` `dsh` `dsh-plugin`

### 8. [dsh-openpencil](https://github.com/ZSeven-W/dsh-openpencil)

⭐ 172 · TypeScript · Updated 2026-09-16

The DeepSeek Harness plugin for OpenPencil — preview, inspect, and edit real .op documents inside a conversation.

Tags: `deepseek-harness` `design` `dsh` `dsh-plugin` `openpencil` `ppt` `ui` `ui-design`

### 9. [dsh-crew](https://github.com/ZSeven-W/dsh-crew)

⭐ 113 · JavaScript · Updated 2026-08-26

DeepSeek Harness (DSH) plugin: dispatch work to DSH agents from Claude Code / Codex — native subagent progress, in-host worker sessions with per-tier presets, and a multimodal bridge that lends the text-only harness vision and image generation.

Tags: `ai-agents` `claude-code` `codex` `coding-agent` `deepseek-harness` `dsh` `dsh-plugin` `mcp`

---

<a id="interfaces"></a>
## Interfaces (TUI / Desktop / Web)

*Clients that bring Harness to the terminal, desktop, or web.*

### 1. [cc-switch](https://github.com/farion1231/cc-switch)

⭐ 153,150 · Rust · Updated 2026-11-10

A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode,DeepSeek Harness and more. Only official website: ccswitch.io

Tags: `ai-tools` `claude-code` `codex` `deepseek-harness` `desktop-app` `grok` `grokbuild` `hermes`

### 2. [open-design](https://github.com/nexu-io/open-design)

⭐ 106,885 · TypeScript · Updated 2026-11-10

The 1st Collaborative AI Design Agent Workspace. Local-first and open source. Create motion, prototypes, websites, apps, dashboards, presentations, images, and videos with your team and AI agents. Share work, exchange feedback, and iterate together in one workspace.

Tags: `agent-skills` `ai-design` `byok` `claude-code-for-design` `claude-design` `codex-design` `cursor-design` `deepseek`

### 3. [OmniRoute](https://github.com/cheaper-inference/OmniRoute)

⭐ 86,044 · TypeScript · Updated 2026-11-10

Never stop coding. Free MIT AI gateway: one endpoint, 375 providers (150+ free), 1,400+ models Kimi, Claude, GPT, Gemini, GLM, DeepSeek, MiniMax. Works with Claude Code, Codex, Cursor, OpenCode, Cline & Copilot. Quota-aware auto-fallback, RTK+Caveman compression saves 15-95% tokens, MCP/A2A, Desktop/PWA. Built by 900+ contributors

Tags: `a2a` `ai-agents` `ai-gateway` `anthropic` `claude` `claude-code` `cline` `codex`

### 4. [OmniRoute](https://github.com/diegosouzapw/OmniRoute)

⭐ 79,017 · TypeScript · Updated 2026-10-21

Never stop coding. Free MIT AI gateway: one endpoint, 375 providers (150+ free), 1,400+ models Kimi, Claude, GPT, Gemini, GLM, DeepSeek, MiniMax. Works with Claude Code, Codex, Cursor, OpenCode, Cline & Copilot. Quota-aware auto-fallback, RTK+Caveman compression saves 15-95% tokens, MCP/A2A, Desktop/PWA. Built by 900+ contributors

Tags: `a2a` `ai-agents` `ai-gateway` `anthropic` `claude` `claude-code` `cline` `codex`

### 5. [DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix)

⭐ 36,148 · Go · Updated 2026-11-10

A reliable coding agent for complex software engineering tasks.

Tags: `agent` `agent-framework` `ai-agent` `ai-coding` `cli` `coding-agent` `deepseek` `developer-tools`

### 6. [dsh-desktop](https://github.com/anywhere-labs/dsh-desktop)

⭐ 35,549 · TypeScript · Updated 2026-11-10

为 DeepSeek Harness (DSH) 插件生态打造的现代化桌面端解决方案。万物皆「插件」，桌面本身也是「插件」。

Tags: `cordis` `cordis-plugin` `deepseek` `deepseek-harness` `desktop` `dsh` `dsh-plugin` `dsh-plugin-desktop`

### 7. [voyager](https://github.com/Nagi-ovo/voyager)

⭐ 20,213 · TypeScript · Updated 2026-09-27

Enhancement suite for Gemini, AI Studio, Claude, ChatGPT & DeepSeek — plus a prompt manager for any website, DeepSeek Harness included. / 面向 Gemini、AI Studio、Claude、ChatGPT 与 DeepSeek 的增强套件；其中的提示词管理器可用于任意网站，如 DeepSeek Harness。

Tags: `ai-studio` `browser-extension` `bun` `chat-management` `chatgpt` `chrome-extension` `claude-ai` `deepseek`

### 8. [deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop)

⭐ 18,946 · TypeScript · Updated 2026-08-24

为 DeepSeek Harness (DSH) 插件生态打造的现代化桌面端解决方案。万物皆「插件」，桌面本身也是「插件」。

Tags: `cordis` `cordis-plugin` `deepseek` `deepseek-harness` `desktop` `dsh` `dsh-plugin` `dsh-plugin-desktop`

### 9. [dsh-Go](https://github.com/ccch1mneyyy/dsh-Go)

⭐ 17,873 · Dart · Updated 2026-11-10

dsh-go — DeepSeek Harness 装进口袋：手机本机运行，也能遥控你的电脑。

Tags: `ai-agent` `android` `android-app` `coding-agent` `deepseek` `deepseek-harness` `dsh` `dsh-plugin`

### 10. [dsh-desktop](https://github.com/dataelement/dsh-desktop)

⭐ 17,758 · JavaScript · Updated 2026-11-10

DSHDesktop：DeepSeek Harness Desktop / DeepSeek Harness 桌面版

Tags: `agent` `apps` `deepseek` `deepseek-harness` `deepseek-harness-desktop` `desktop` `dsh-desktop` `dsh-plugin`

### 11. [FreeToken](https://github.com/FlashML-org/FreeToken)

⭐ 16,949 · Python · Updated 2026-11-10

FreeToken brings datacenter-scale model serving to your desktop. Run massive models locally, fast and efficiently.

Tags: `deepseek-v4` `edge` `glm` `inference` `minimax` `moe` `qwen` `transformer`

### 12. [bisheng](https://github.com/dataelement/bisheng)

⭐ 12,210 · Python · Updated 2026-11-10

BISHENG is an open-source enterprise Agent platform for building, deploying, and managing AI applications. It combines AI agents, workflows, RAG and knowledge management, desktop agent integration, and vibecoding app hosting with unified model management, evaluation, observability, access control, and enterprise administration.

Tags: `agent` `ai` `chatbot` `dsh` `dsh-plugin` `enterprise` `finetune` `genai`

### 13. [yao](https://github.com/YaoApp/yao)

⭐ 8,287 · Go · Updated 2026-11-10

✨ All your agents and workspaces in one place, on every device you own. Track tasks on a board, accessible from desktop, mobile, browser, or API. Self-hosted.

Tags: `agent-harness` `agent-orchestration` `agent-skills` `agent-workspaces` `ai-agents` `ai-native` `claude-code` `coding-agent`

### 14. [dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI)

⭐ 7,345 · TypeScript · Updated 2026-11-10

DSH's officially top-recommended TUI plugin — high performance, low overhead, cute pixel whale, smooth mouse interaction. One-command install via npm. / DSH 官方首推的 TUI 插件，高性能低占用，可爱像素鲸鱼，流畅鼠标交互，npm 一键安装

Tags: `claude-code` `coding-agent` `deepseek` `deepseek-harness` `dsh-plugin` `ink` `react` `terminal`

### 15. [dsh-pet](https://github.com/PC2005-cloud/dsh-pet)

⭐ 5,986 · TypeScript · Updated 2026-11-10

DSH 桌面宠物：一行命令装好即用的透明动画小桌宠，支持多开、大小位置随心配置；还内置 DIY 素材链，能用 AI 视频自造专属宠物

Tags: `deepseek-harness` `desktop-pet` `dsh` `dsh-plugin`

### 16. [DSH-better-sidebar](https://github.com/omdsh-dev/DSH-better-sidebar)

⭐ 5,037 · TypeScript · Updated 2026-11-10

开放的侧边栏底座，支持三方拓展注册新侧边栏页面。内置文件渲染编辑/终端/侧边对话/Git/子代理页面 ｜ Open sidebar foundation, supports third-party extensions to register new sidebar pages. Built-in file rendering/editing, terminal, side chat, Git, and sub-agent pages.

Tags: `deepseek` `deepseek-harness` `dsh` `dsh-better-sidebar` `dsh-plugin` `dsh-plugins` `sidebar`

### 17. [desktop-cc-gui](https://github.com/zhukunpenglinyutong/desktop-cc-gui)

⭐ 4,511 · TypeScript · Updated 2026-10-23

Multi-engine AI coding desktop client (Tauri). Claude Code, Codex, Gemini, OpenCode, DeepSeek Harness and more in one GUI.

Tags: `ai-coding` `claude-code` `codex` `deepseek-harness` `desktop-app` `dsh` `tauri` `vibe-coding`

### 18. [codeg](https://github.com/xintaofei/codeg)

⭐ 3,779 · Rust · Updated 2026-10-03

Collaborative multi-agent AI coding workspace: aggregate sessions from Claude Code, Codex, OpenCode, Pi, Grok Build, etc. Desktop app, self-hosted server, or Docker.

Tags: `acp` `ade` `agent` `claude-code` `code-generation` `codex` `deepseek-harness` `grok-build`

### 19. [deepseek-harness-desktop](https://github.com/dsh-tauri/deepseek-harness-desktop)

⭐ 3,566 · TypeScript · Updated 2026-11-10

DSH Tauri 桌面版 | Better DSH desktop, zero environment setup, preset plugins, Windows / macOS / Linux.

Tags: `deepseek` `deepseek-harness` `desktop` `dsh` `dsh-desktop` `dsh-plugin` `tauri`

### 20. [EchoBird](https://github.com/edison7009/EchoBird)

⭐ 3,275 · Rust · Updated 2026-09-26

Manage ChatGPT, Codex CLI, and Claude Code accounts and track quota in one place. Use multi-model smart routing with priority and automatic failover. Install AI tools and deploy local LLMs in one click.

Tags: `claude-code` `deepseek` `deepseek-harness` `dsh-plugin` `dsh-plugins` `kimi-code` `openclaw` `opencode`

### 21. [DSHA](https://github.com/DSH-APP/DSHA)

⭐ 3,244 · Java · Updated 2026-11-10

免 ROOT 免 Termux，在手机上跑 DeepSeek Harness。完整 Ubuntu 环境 + proroot 零 ptrace 开销 · AI 输出实时上屏 · ADB 直连 · 数据不丢

Tags: `android` `coding-agent` `deepseek` `deepseek-harness` `launcher` `llm` `proot` `proroot`

### 22. [dsh-pet-indesktop](https://github.com/MerZlin/dsh-pet-indesktop)

⭐ 3,202 · Python · Updated 2026-11-10

基于项目PC2005-cloud/dsh-pet.git，将桌宠移植到Windows、Linux和MacOS上，现在可以随时看到蓝色大肥鱼了：），本项目还额外实现了其他交互功能，欢迎体验

### 23. [dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard)

⭐ 3,187 · JavaScript · Updated 2026-09-23

现代化可灵活嵌入的任务面板，支持 Codex、DeepSeek Harness

Tags: `claude-code` `cli` `codex` `codex-app` `codex-desktop` `codex-plugin` `dsh` `dsh-plugin`

### 24. [clawpanel](https://github.com/qingchencloud/clawpanel)

⭐ 2,929 · JavaScript · Updated 2026-09-15

🦞 OpenClaw & Hermes Agent 多引擎 AI 管理面板 — 内置 AI 助手（工具调用 + 图片识别 + 多模态），一键安装 | Tauri v2 跨平台桌面应用 | 11 种语言

Tags: `admin-panel` `ai-agent` `ai-assistant` `ai-chat` `ai-tools` `chatgpt` `cross-platform` `deepseek`

### 25. [agency-orchestrator](https://github.com/jnMetaCode/agency-orchestrator)

⭐ 2,206 · TypeScript · Updated 2026-09-07

🚀 One sentence → your one-person company of AI experts → complete deliverable in minutes. 267 CN + 184 EN + 5 more languages (ko/ru/pt-BR/id/ar) · zero-code YAML · auto-verified acceptance · Web Studio / Desktop / Docker · 11 LLM providers (7 key-free). 一句话组建你的「一人公司」AI 专家团队，几分钟交付完整方案；验收自动核验，网页 / 桌面 / Docker 全渠道。

Tags: `agency-agents` `agent-orchestration` `ai-agents` `autogen-alternative` `claude` `codex` `copilot` `crewai-alternative`

### 26. [deepseek-harness-desktop](https://github.com/dsh-tauri-desk/deepseek-harness-desktop)

⭐ 2,127 · TypeScript · Updated 2026-09-16

DeepSeek Harness Tauri 桌面版 | Only 5mb installer, zero environment setup, preset plugins, Windows / macOS / Linux.

Tags: `deepseek` `deepseek-harness` `desktop` `dsh` `dsh-desktop` `dsh-plugin` `tauri`

### 27. [token-monitor](https://github.com/Javis603/token-monitor)

⭐ 1,944 · JavaScript · Updated 2026-09-05

Local-first desktop widget for tracking token usage, costs, and limits across 35+ AI coding tools—including Claude Code, Codex, Cursor, OpenCode, and OpenClaw—with multi-device sync.

Tags: `ai` `ai-tools` `antigravity` `claude-code` `codex` `cursor` `deepseek` `deepseek-harness`

### 28. [EAC-Desktop](https://github.com/DSH-EAC/EAC-Desktop)

⭐ 1,939 · TypeScript · Updated 2026-10-10

Embracing All Creation (Desktop) — Dedicated to the Harmonious Coexistence of Hundreds of DSH Plugins / 揽尽万象（桌面版） —— 致力于让数百个DSH插件和谐共存

Tags: `ai-agent` `deepseek` `deepseek-harness` `desktop` `desktop-app` `dsh` `dsh-plugin` `dsh-plugins`

### 29. [dsh-workbuddy-connect](https://github.com/corrinehu/dsh-workbuddy-connect)

⭐ 1,558 · TypeScript · Updated 2026-10-21

将 WorkBuddy 桌面 App 包含的模型自动接入 DeepSeek Harness，零配置使用。Bring the models in the WorkBuddy desktop app into DeepSeek Harness with zero configuration.

Tags: `deepseek-harness` `dsh-plugin` `workbuddy`

### 30. [TokenTracker](https://github.com/xiufengsun/TokenTracker)

⭐ 1,450 · JavaScript · Updated 2026-08-29

Local-first AI token usage & cost tracker for 31 coding tools incl. Claude Code, Codex, Cursor, Gemini & DeepSeek Harness—with native apps. Never reads prompts.

Tags: `ai-coding-tools` `ai-tools` `antigravity` `claude-code` `cli` `codex-cli` `cost-tracker` `cursor`

### 31. [agentrq](https://github.com/agentrq/agentrq)

⭐ 1,086 · Go · Updated 2026-08-21

AgentRQ: Human-in-loop realtime conversational task manager for AI Agents. Self-hosted! Control your own agents from wherever you want Mobile, Web, Desktop. Designed to work well with your own Claude subscriptions and any harness.

Tags: `acp-client` `acp-gateway` `agentic-ai` `agentic-workflow` `agents` `claude-code` `deepseek-harness` `deepseek-harness-plugin`

### 32. [dsh-browser](https://github.com/omdsh-dev/dsh-browser)

⭐ 1,030 · TypeScript · Updated 2026-11-10

Chrome sidebar extension that lets DeepSeek Harness operate your browser directly, no vision capabilities required. 一款 Chrome 侧边栏扩展程序，可让 DeepSeek Harness 直接操控您的浏览器，无需视觉能力。

Tags: `browser-automation` `chrome-extension` `coding-agent` `cordis` `deepseek` `deepseek-harness` `dsh` `dsh-plugin`

### 33. [dsh-worktable](https://github.com/Aisland-SJL/dsh-worktable)

⭐ 852 · JavaScript · Updated 2026-11-10

🖥️ Agent-project workbench for DeepSeek Harness — sidebar app drawer + dockable split workspace + a live control room watching every project.

Tags: `agent` `deepseek` `deepseek-harness` `dsh` `dsh-plugin` `productivity` `web-gui` `workspace`

### 34. [dsh-mobile](https://github.com/Clarklevis1995/dsh-mobile)

⭐ 755 · Kotlin · Updated 2026-11-10

DeepSeek Harness Mobile 是一个面向 DeepSeek Harness 的原生移动端客户端。它通过 dsh-plugin-mobile-gateway 与 Harness 建立 WebSocket 连接，将工作区、会话、实时回复和 Agent 执行轨迹带到 iPhone，同时延续 DeepSeek WebUI 克制、清晰的视觉语言

Tags: `android` `android-app` `android-application` `android-development` `coding-agent` `deepseek` `deepseek-harness` `deepseek-harness-plugin`

### 35. [dsh_desktop](https://github.com/myYangyunfan/dsh_desktop)

⭐ 747 · JavaScript · Updated 2026-11-10

DeepSeek Harness (dsh) Windows desktop client - bundled Node.js + dsh CLI, one-click launch

Tags: `ai-agent` `cordis` `deepseek` `deepseek-harness` `desktop` `desktop-app` `dsh` `dsh-desktop`

### 36. [dsh-ads](https://github.com/Nagi-ovo/dsh-ads)

⭐ 715 · TypeScript · Updated 2026-11-10

把 DSH 变成 2005 年门户网站｜Parody ads, fake games, and popups for the DSH Web UI

Tags: `deepseek-harness` `dsh-plugin` `trolling` `web-ui`

### 37. [dshcode](https://github.com/whitelonng/dshcode)

⭐ 705 · TypeScript · Updated 2026-11-09

Community desktop companion for DeepSeek Harness — one-click Electron app for macOS and Windows

Tags: `agent` `deepseek` `deepseekharness-plugin` `dsh-plugin` `harness`

### 38. [world-execute-me-dsh-pv](https://github.com/MisakaZentai/world-execute-me-dsh-pv)

⭐ 705 · Python · Updated 2026-11-10

Code-rendered TUI fan PV for Mili world.execute(me); with a DeepSeek Harness-style chat window. MIT code; CC BY-NC-SA 4.0 artwork.

### 39. [dsh-browser](https://github.com/Lum1104/dsh-browser)

⭐ 698 · TypeScript · Updated 2026-09-20

Chrome sidebar extension that lets DeepSeek Harness operate your browser directly, no vision capabilities required. 一款 Chrome 侧边栏扩展程序，可让 DeepSeek Harness 直接操控您的浏览器，无需视觉能力。

Tags: `browser-automation` `chrome-extension` `coding-agent` `cordis` `deepseek` `deepseek-harness` `dsh` `dsh-plugin`

### 40. [dsh-computer-use-win](https://github.com/Yu-tao-Li/dsh-computer-use-win)

⭐ 623 · JavaScript · Updated 2026-11-10

DeepSeek Harness的Windows电脑操控插件 / Windows computer use for DeepSeek Harness

Tags: `computer-use` `desktop-automation` `dsh-plugin` `mcp` `uia` `windows`

### 41. [dsh-dafeiyu](https://github.com/QCYTSN/dsh-dafeiyu)

⭐ 609 · JavaScript · Updated 2026-11-10

Desktop-native BigFish companion for DeepSeek Harness — real Agent status, always on top on Windows.

Tags: `agent-companion` `deepseek-harness` `desktop-pet` `dsh-plugin` `windows`

### 42. [dsh-plugin-subscriptions](https://github.com/V1ki/dsh-plugin-subscriptions)

⭐ 579 · TypeScript · Updated 2026-11-10

Use ChatGPT (Codex), Claude, and Grok (X Premium) subscriptions as DeepSeek Harness LLM providers — OAuth login in the web UI, no API keys

Tags: `ai-agent` `chatgpt` `claude` `codex` `deepseek-harness` `dsh-plugin` `grok` `llm`

### 43. [dsh-desktop](https://github.com/vibeinging/dsh-desktop)

⭐ 490 · JavaScript · Updated 2026-11-10

DeepSeek Harness Desktop App: a local AI desktop workspace for DSH Sessions, projects, files, web research, plugins, and Office artifacts.

Tags: `agentic-workflows` `ai-agent` `ai-workbench` `data-analysis` `deepseek-harness` `desktop-app` `dsh` `dsh-plugin`

### 44. [dsh-ego-browser](https://github.com/Fisfzy/dsh-ego-browser)

⭐ 444 · TypeScript · Updated 2026-11-06

DSH（DeepSeek Harness）插件：把 ego-lite 浏览器（给 AI Agent 用的 Chromium）接入 HARNESS——13 个结构化 ego_* 工具（文本语义快照、语义定位点击、表单填充、截图、CDP 控制、任务空间隔离），内置 ego 运行时，Linux + Chrome 开箱即用，无需克隆官方仓库或手动构建。

Tags: `agent-browser` `browser-automation` `cordis` `deepseek-harness` `dsh` `dsh-better-sidebar` `dsh-plugin` `dshfind`

### 45. [DSHA](https://github.com/qiannianhuanxiang/DSHA)

⭐ 390 · Java · Updated 2026-09-05

免 ROOT 免 Termux，在手机上跑 DeepSeek Harness。完整 Ubuntu 环境 + proroot 零 ptrace 开销 · AI 输出实时上屏 · ADB 直连 · 数据不丢

Tags: `android` `coding-agent` `deepseek` `deepseek-harness` `launcher` `llm` `proot` `proroot`

### 46. [dsh-ios](https://github.com/ZSeven-W/dsh-ios)

⭐ 352 · TypeScript · Updated 2026-10-30

DeepSeek Harness (DSH) plugin: a live iOS Simulator — and a USB-connected iPhone — inside the conversation. 22 agent tools for booting, building, driving the UI by accessibility identity, OCR text or list rows, plus a streaming sidebar panel you can tap and drag on.

Tags: `accessibility` `ai-agents` `coding-agent` `deepseek-harness` `dsh` `dsh-plugin` `ios` `ios-simulator`

### 47. [oh-dsh](https://github.com/hust-open-atom-club/oh-dsh)

⭐ 323 · TypeScript · Updated 2026-10-26

一套 DSH runtime，Desktop、Web 与 TUI 三种开发体验。

Tags: `ai-agent` `cordis` `deepseek-harness` `dsh` `dsh-plugin` `dsh-plugins`

### 48. [DSH-taskboard](https://github.com/shengsheng90/DSH-taskboard)

⭐ 322 · TypeScript · Updated 2026-10-25

Native local Taskboard plugin for DeepSeek Harness. SQLite-backed projects, Agent claim/review, and a native Web UI — no iframe, no second chat runtime.

Tags: `agent` `cordis` `deepseek-harness` `dsh` `dsh-plugin` `task-management` `taskboard`

### 49. [dsh-tianshu-tui](https://github.com/huiliyi37/dsh-tianshu-tui)

⭐ 289 · TypeScript · Updated 2026-10-21

官方 DeepSeek Harness 的交互式终端 UI 插件：自研 ANSI 极简交互渲染、流式 Markdown/工具卡、16+ 主题、slash 命令与选择器、输入历史与本地偏好持久化、LSP 诊断、memory记忆，很丝滑的开发体验。

Tags: `coding` `dsh` `dsh-plugin` `harness` `harness-engineering` `tui`

### 50. [dsh-trading](https://github.com/zhu1090093659/dsh-trading)

⭐ 268 · TypeScript · Updated 2026-10-20

Agent-native trading terminal built on DeepSeek Harness. Crypto, US, CN and HK in one three-column GUI, 19+ hot-swappable connectors, dry-run by default with human approval on every live order. BYOK, no data redistribution.

Tags: `agent-native` `ai-agent` `cryptocurrency` `dsh` `dsh-plugin` `dsh-plugin-desktop` `trading-terminal`

### 51. [dsh-popout-sidebar](https://github.com/e2mcc/dsh-popout-sidebar)

⭐ 209 · JavaScript · Updated 2026-09-27

A sidebar can pop out a separate browser tab (drag it to another monitor)

Tags: `dsh-plugin`

### 52. [dsh-skill-mcp-panel](https://github.com/Fishquito7/dsh-skill-mcp-panel)

⭐ 86 · JavaScript · Updated 2026-08-20

DSH Web UI plugin: skill and MCP management（Web界面的skill/MCP管理工具）

Tags: `deepseek` `dsh` `dsh-plugin` `mcp` `plugin` `skills`

---

<a id="ecosystem"></a>
## Ecosystem & Marketplaces

*Infrastructure for discovering, installing, and managing Harness projects.*

### 1. [dsh-market](https://github.com/dsh-market/dsh-market)

⭐ 11,729 · TypeScript · Updated 2026-11-10

The plugin market inside DeepSeek Harness — browse, search, one-click install · DSH 可视化插件市场

Tags: `deepseek-harness` `dsh-plugin` `marketplace`

### 2. [dsh-web](https://github.com/zhu1090093659/dsh-web)

⭐ 10,293 · TypeScript · Updated 2026-11-10

DeepSeek Harness (DSH) Web 插件聚合生态 · 万物皆插件，通过创意工坊分发｜｜DeepSeek Harness (DSH) Web Plugin Aggregation Ecosystem · Everything is a plugin, distributed via the Creative Workshop

Tags: `cordis` `deepseek-harness` `dsh` `dsh-plugin` `dsh-web` `dsh-web-ui`

### 3. [dsh-wallpaper-engine](https://github.com/elysia395/dsh-wallpaper-engine)

⭐ 6,235 · JavaScript · Updated 2026-11-10

把本机 Wallpaper Engine 的壁纸搬进 DSH 网页界面：场景壁纸由内置 MIT 开源引擎 WebWallGL 实时 WebGL 渲染（粒子 / puppet 骨骼 / SceneScript / 音频反应 / 鼠标交互），失败自动降级内嵌 MP4 与场景静态帧；Web 壁纸严格沙箱 + WE API；iOS 风格液态玻璃 UI 高度自定义，遮挡暂停省电、ffmpeg 帧率上限转码、系统音频频谱与 Now Playing、自定义上传与自动轮播；设置存宿主端，对 agent 零 token 开销。Windows / macOS / Linux 三平台原生（同一个包、同一条命令）。

Tags: `deepseek-harness` `dsh-plugin` `dsh-plugin-market` `dsh-plugins` `liquid-glass` `theme` `wallpaper` `wallpaper-engine`

### 4. [skillhub](https://github.com/iflytek/skillhub)

⭐ 5,349 · Java · Updated 2026-11-01

Self-hosted, open-source agent skill registry for enterprises. Publish & version skill packages, govern with RBAC and audit logs, deploy   on-premise with Docker or Kubernetes.

Tags: `agent-framework` `ai-agent` `ai-governance` `ai-infrastructure` `ai-orchestration` `audit-log` `dsh-plugin` `enterprise-ai`

### 5. [dsh-pocket](https://github.com/shaobeichen/dsh-pocket)

⭐ 2,876 · JavaScript · Updated 2026-11-10

把 DeepSeek Harness 装进你的口袋：电脑上跑 dsh web，手机扫码即同步访问（局域网 + 公网，实时同屏）Put DeepSeek Harness in your pocket: run dsh web on your computer and access it synchronously by scanning a QR code on your phone (LAN + public network, real‑time screen mirroring)

Tags: `deepseek` `deepseek-harness` `deepseek-harness-plugin` `dsh` `dsh-plugin` `dsh-plugin-market` `dsh-plugins` `mobile`

### 6. [dsh-plugin-radar](https://github.com/AdamPlatin123/dsh-plugin-radar)

⭐ 1,498 · Python · Updated 2026-11-10

DSH Plugin Radar — open-source ecosystem radar for DeepSeek Harness plugins: continuous discovery (21k+ candidates), k8s runtime validation (13k+ tests), 15-min snapshots; the catalog is a generated artifact — 开源 DSH 插件生态雷达：持续发现 2.1 万+ 候选、k8s 运行级实测 1.3 万+、15 分钟快照；插件目录为自动生成的产物

Tags: `agent-plugins` `continuous-validation` `deepseek-harness` `dsh` `dsh-plugin` `ecosystem-radar` `plugin-registry`

### 7. [awesome-dsh-plugins](https://github.com/AdamPlatin123/awesome-dsh-plugins)

⭐ 1,422 · Python · Updated 2026-08-28

DSH 插件雷达与精选榜：多路自动发现 14900+ 候选，容器真实安装路径运行级实测（四档判定），精选 Top 50 · 11 类人工策展，全量索引 PLUGINS-ALL.md，自动更新。

Tags: `agent-plugins` `awesome-list` `deepseek-harness` `dsh` `dsh-plugin` `plugin-registry`

### 8. [dsh-connect-workbuddy](https://github.com/dingminhua/dsh-connect-workbuddy)

⭐ 1,388 · TypeScript · Updated 2026-11-10

Connect locally signed-in WorkBuddy models to DeepSeek Harness with a read-only credits overview and model management.

Tags: `dsh-plugin` `dsh-plugin-market` `dsh-plugins`

### 9. [jingyun-dsh](https://github.com/jingyunstudio/jingyun-dsh)

⭐ 930 · TypeScript · Updated 2026-11-09

基于 Jingyun Studio + DeepSeek Harness (DSH) 打造的一站式 AI 商业化桌面客户端，一个将 AI 智能体 / 技能 / 工作流转化为可交易商品的完整商业化平台客户端。  井云为 DSH 注入了完整的商业闭环：登录注册 → 会员体系 → 订阅支付 → 云端资产 → 多端同步，让 AI 开发者 30 分钟内将自己的智能体封装为独立的商业产品。

Tags: `deepseekharness` `dsh` `dsh-bundle` `dsh-plugin` `dsh-plugin-desktop` `dsh-plugin-market` `dsh-plugin-verify` `dsh-plugins`

### 10. [dsh-plugin-shop](https://github.com/LivXue/dsh-plugin-shop)

⭐ 663 · TypeScript · Updated 2026-11-09

The most comprehensive DeepSeek Harness plugin market — refreshed daily, sourced across the Internet, reviewed before publishing.

Tags: `agent` `deepseek` `deepseek-harness` `deepseek-harness-plugin` `dsh` `dsh-plugin` `harness`

### 11. [DSHBox](https://github.com/WSK-build/DSHBox)

⭐ 606 · Kotlin · Updated 2026-11-10

DSHBox — 移动端本地运行 DeepSeek Harness。自带终端、文件管理器、浏览器、手机操控等工具，致力打造一站式随身 AI 工作台，免 ROOT 和 Termux。

Tags: `ai-agent` `android` `android-agent` `android-app` `deepseek-harness` `deepseek-harness-android` `deepseek-harness-mobile` `dsh`

### 12. [dsh-meme](https://github.com/yyh-001/dsh-meme)

⭐ 549 · JavaScript · Updated 2026-11-10

DeepSeek Harness 表情包插件：输入框一键发图、文字 token 斗图、情绪主动发图、AI 自动学图，图库市场一键安装。 · Meme/sticker plugin for DeepSeek Harness: one-click picker in the composer, text-token memes, mood-driven sending, AI learns your images, marketplace packs.

Tags: `deepseek-harness` `dsh-plugin` `meme` `qq-bot` `selfloom` `semantic-search`

### 13. [dsh-plugin-hub](https://github.com/dshplugin/dsh-plugin-hub)

⭐ 502 · TypeScript · Updated 2026-11-10

DSH Plugin 插件市场 - DeepSeek Harness Plugin Market (DSH) 下载与安装 · 插件大全

Tags: `agent` `ai` `cli` `community-plugins` `deepseek` `deepseek-harness` `dsh-plugin` `dsh-plugin-org`

### 14. [dshfind](https://github.com/hikariming/dshfind)

⭐ 331 · TypeScript · Updated 2026-10-27

DSH (DeepSeek Harness) 原理学习、插件市场与最佳实践 · Learn DSH principles, plugin marketplace & best practices

Tags: `deepseek-harness` `dsh` `dsh-plugin`

### 15. [DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace)

⭐ 165 · JavaScript · Updated 2026-09-14

DSH插件市场 / DSH Plugin Marketplace: 在 DeepSeek Harness Web GUI 中一键浏览、安装与更新 GitHub topic:dsh-plugin 的全部插件 | browse, install & update all GitHub dsh-plugin plugins in the DSH Web GUI

Tags: `agent` `ai-agents` `cordis` `deepseek-harness` `dsh` `dsh-plugin` `javascript` `llm`

### 16. [dsh-webui-market-plugin](https://github.com/Sanqi-normal/dsh-webui-market-plugin)

⭐ 100 · JavaScript · Updated 2026-08-22

dsh Web GUI 社区插件市场：浏览 awesome-dsh-plugin.com 插件目录，一键安装/卸载到 profile。Community plugin market for the DeepSeek Harness (dsh) web GUI: browse, install and uninstall plugins into a profile.

Tags: `agent-harness` `deepseek` `dsh-plugin` `plugin-market` `ui` `web`

### 17. [dsh-plugin](https://github.com/Tabbit-Browser/dsh-plugin)

⭐ 90 · JavaScript · Updated 2026-08-19

Tabbit Broser plugins for Deepseek Harness

Tags: `browser-automation` `browser-use` `deepseek-harness` `dsh-plugin` `dsh-plugin-market` `dsh-plugin-verify` `dsh-plugins` `playwright`

---

<a id="themes"></a>
## Themes & Skins

*Themes, skins, and visual enhancements.*

### 1. [CodeWhale](https://github.com/Hmbown/CodeWhale)

⭐ 40,829 · Rust · Updated 2026-08-20

Open-source, community-driven agent harness

Tags: `ai` `ai-agent` `alibaba-cloud` `anthropic` `cli` `coding-agent` `deepseek` `deepseek-harness`

### 2. [DeepSeek-Balance-Whale-Widget](https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget)

⭐ 7,097 · JavaScript · Updated 2026-11-10

DeepSeek Harness（DSH）一只住在 DSH 界面右下角的小鲸鱼娘，帮你盯着DeepSeek账户余额。QQ弹弹，支持拖拽吸附、左吸附翻转、数字滚动动画，随界面自动启用，建议直接喊来你的dsh安装

Tags: `cordis` `deepseek` `deepseek-harness` `developer-tools` `dsh` `dsh-plugin` `dsh-plugins` `floating-widget`

### 3. [dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui)

⭐ 5,748 · TypeScript · Updated 2026-08-24

DeepSeek Harness（DSH）Web GUI 插件与皮肤生态：一切皆插件。任务看板、移动端远程与 SSH 运维构筑开发工作台；皮肤经 WebGL 深度优化，更支持 Wallpaper Engine 壁纸；皮肤、宠物、插件由 DSH 大市场一键安装，正迈向 DSH 创意工坊。A pluggable plugin-skin ecosystem for the DSH Web GUI - Task board, remote mobile UI, SSH ops, WebGL-optimized skins with Wallpaper Engine wallpapers - becoming a DSH creative workshop.

Tags: `cordis` `deepseek-harness` `dsh` `dsh-plugin` `dsh-web` `dsh-web-ui`

### 4. [dsh-deep-whale](https://github.com/Small-tailqwq/dsh-deep-whale)

⭐ 3,083 · TypeScript · Updated 2026-11-10

Whale Girl skin series for DeepSeek Harness. 适用于 DeepSeek Harness 的，鲸鱼娘系列皮肤。

Tags: `dsh` `dsh-plugin`

### 5. [DSH-Desktop-EAC](https://github.com/DSH-EAC/DSH-Desktop-EAC)

⭐ 1,824 · JavaScript · Updated 2026-10-03

DeepSeek Harness Desktop (dsh-desktop). EAC: Embracing All Creation (揽尽万象). Bundled Node.js runtime with full dsh-CLI kernel, one-click startup, 10 built-in UI themes.

Tags: `ai-agent` `deepseek` `deepseek-harness` `desktop` `desktop-app` `dsh` `dsh-plugins` `dshdesktop`

### 6. [DSH-Desktop-EAC](https://github.com/zouyuxuan122/DSH-Desktop-EAC)

⭐ 1,622 · JavaScript · Updated 2026-09-11

DeepSeek Harness Desktop (dsh-desktop). EAC: Embracing All Creation (揽尽万象). Bundled Node.js runtime with full dsh-CLI kernel, one-click startup, 10 built-in UI themes.

Tags: `ai-agent` `deepseek` `deepseek-harness` `desktop` `desktop-app` `dsh` `dsh-plugins` `dshdesktop`

### 7. [Deepseek-Harness-EAC](https://github.com/zouyuxuan122/Deepseek-Harness-EAC)

⭐ 1,265 · JavaScript · Updated 2026-08-24

DeepSeek Harness Desktop (dsh-desktop). EAC: Embracing All Creation (揽尽万象). Bundled Node.js runtime with full dsh-CLI kernel, one-click startup, 10 built-in UI themes.

Tags: `ai-agent` `deepseek` `deepseek-harness` `desktop` `desktop-app` `dsh` `dsh-plugins` `dshdesktop`

### 8. [dsh-bili-whale](https://github.com/Alterssss/dsh-bili-whale)

⭐ 995 · JavaScript · Updated 2026-11-10

给 DSH 装一条有日子的鱼：自己按作息刷 B 站、真看懂视频、写两本日记，把值得的 @ 你。

### 9. [dsh-claude-style](https://github.com/Nwflower/dsh-claude-style)

⭐ 544 · TypeScript · Updated 2026-11-10

Claude Code Desktop theme for DeepSeek Harness｜ 为 DeepSeek Harness 复刻 Claude Code Desktop 风格与交互体验的主题插件

Tags: `anthropic` `claude` `claude-code` `claude-desktop` `cordis` `dark-mode` `deepseek-harness` `desktop-theme`

### 10. [dsh-fish-memory](https://github.com/Yuuyuko-uu/dsh-fish-memory)

⭐ 507 · JavaScript · Updated 2026-11-09

🐋 DSH 鱼的记忆：给会话一份会淡忘的长期记忆，每条都带时间。名字里的「鱼」来自 DeepSeek 的鲸鱼。

Tags: `ai-companion` `deepseek-harness` `dsh-plugin` `long-term-memory` `memory` `whale`

### 11. [DSH-Transparent-UI-Plugin](https://github.com/WYH66666666/DSH-Transparent-UI-Plugin)

⭐ 432 · JavaScript · Updated 2026-11-03

是一层高自由度的玻璃质感主题，套在 DeepSeek Harness 网页端。顶栏、侧边栏、输入框、统计行、轨迹视图都成了磨砂玻璃片。玻璃模糊度、磨砂度、背景（流体或自定义壁纸，壁纸还能单独调模糊和磨砂）全都能在设置卡片里自由调节。关掉开关就回到原生界面，不改 DSH 任何一行源码。

Tags: `deepseek-harness` `deepseek-harness-plugin` `dsh` `dsh-plugin` `theme`

### 12. [dsh-liang-skin](https://github.com/kingOfSoySauce/dsh-liang-skin)

⭐ 304 · JavaScript · Updated 2026-10-24

DeepSeek Harness 滑动变阻器皮肤

Tags: `dsh-plugin`

### 13. [dsh-dream-skin](https://github.com/RevolutionLA/dsh-dream-skin)

⭐ 252 · JavaScript · Updated 2026-10-17

DeepSeek Harness 换肤 / 壁纸 / 主题包插件 (dsh-plugin) — 8 套 Mirage 主题、每用户强调色、壁纸2.0、主题包导入导出/分享链接、收藏与随机，纯原生 token 系统实现。

Tags: `deepseek-harness` `dsh` `dsh-plugin` `dsh-plugin-theme` `skin` `theme` `wallpaper`

---

<a id="other"></a>
## Other Projects

*Related projects not yet placed in another category.*

### 1. [ollama](https://github.com/ollama/ollama)

⭐ 186,477 · Go · Updated 2026-11-10

Get up and running with Kimi, GLM, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.

Tags: `deepseek` `gemma` `glm` `go` `golang` `gpt-oss` `llama` `llm`

### 2. [DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3)

⭐ 104,786 · Python · Updated 2026-11-10

No project description yet.

### 3. [unsloth](https://github.com/unslothai/unsloth)

⭐ 79,262 · Python · Updated 2026-11-10

Local UI to run and train LLMs and diffusion models. Supports GGUF, MLX, Qwen3.8, DeepSeek-V4.1, MiniMax-H3, Gemma 4, FLUX and more.

Tags: `agent` `ai` `chatgpt` `deepseek` `fine-tuning` `gemma` `image-generation` `llama`

### 4. [LlamaFactory](https://github.com/hiyouga/LlamaFactory)

⭐ 75,968 · Python · Updated 2026-11-10

Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

Tags: `agent` `ai` `deepseek` `fine-tuning` `gemma` `gpt` `instruction-tuning` `large-language-models`

### 5. [openinterpreter](https://github.com/openinterpreter/openinterpreter)

⭐ 68,850 · Rust · Updated 2026-11-10

A coding agent for open models like Kimi K3 and GLM 5.3

Tags: `acp` `coding-agent` `deepseek` `kimi` `python` `qwen` `rust`

### 6. [mindshub](https://github.com/mindsdb/mindshub)

⭐ 39,852 · Makefile · Updated 2026-11-10

The unified workspace where open-source models get things done for you.

Tags: `agents` `ai` `anton` `artificial-inteligence` `claude` `claude-cowork` `codex` `cowork`

### 7. [magpie](https://github.com/yetone/magpie)

⭐ 33,330 · Go · Updated 2026-11-10

Every agent's model. One place. Codex on DeepSeek, Claude Code on Kimi, from the menu bar.

Tags: `claude-code` `codex` `deepseek` `gemini-cli` `llm` `macos`

### 8. [ds4](https://github.com/antirez/ds4)

⭐ 22,081 · C · Updated 2026-09-05

DeepSeek 4 Flash and PRO local inference engine for Metal, CUDA and ROCm

### 9. [Awesome-MCP-ZH](https://github.com/yzfly/Awesome-MCP-ZH)

⭐ 7,826 · N/A · Updated 2026-11-10

MCP 资源精选， MCP指南，Claude MCP，MCP Servers, MCP Clients

Tags: `claude` `claude-mcp` `deepseek` `deepseek-mcp` `mcp` `mcp-clients` `mcp-host` `mcp-server`

### 10. [ClawRouter](https://github.com/BlockRunAI/ClawRouter)

⭐ 6,661 · TypeScript · Updated 2026-11-10

The agent-native LLM router for autonomous agents. Every frontier model behind one wallet, <1ms local routing, USDC payments on Base & Solana via x402.

Tags: `ai` `ai-agents` `anthropic` `cost-optimization` `deepseek` `gemini` `llm` `llm-router`

### 11. [Awesome-AITools](https://github.com/ikaijua/Awesome-AITools)

⭐ 6,285 · Python · Updated 2026-11-09

220+ AI tools across 37+ categories — chatbots, coding agents, AI video/image/voice, open-weight models. / 220+ 个 AI 工具、AI+人工筛选。

Tags: `agent-skills` `agents` `ai` `ai-tools` `artificial-intelligence` `awesome` `awesome-list` `awesome-lists`

### 12. [awesome-deepseek-agent](https://github.com/deepseek-ai/awesome-deepseek-agent)

⭐ 5,996 · N/A · Updated 2026-08-24

No project description yet.

### 13. [deepreasoning](https://github.com/winfunc/deepreasoning)

⭐ 5,361 · Rust · Updated 2026-08-20

A high-performance LLM inference API and Chat UI that integrates DeepSeek R1's CoT reasoning traces with Anthropic Claude models.

Tags: `ai` `anthropic` `anthropic-claude` `api` `chain-of-thought` `claude` `deepseek` `deepseek-r1`

### 14. [fastllm](https://github.com/ztxz16/fastllm)

⭐ 5,120 · C++ · Updated 2026-10-24

fastllm是后端无依赖的高性能大模型推理库。同时支持张量并行推理稠密模型和混合模式推理MOE模型，任意10G以上显卡即可推理满血DeepSeek。双路9004/9005服务器+单显卡部署DeepSeek满血满精度原版模型，单并发20tps；INT4量化模型单并发30tps，多并发可达60+。

### 15. [Rapid-MLX](https://github.com/raullenchai/Rapid-MLX)

⭐ 3,933 · Python · Updated 2026-10-08

Rapid-MLX is an open-source (Apache 2.0) OpenAI- and Anthropic-compatible LLM inference server for Apple Silicon, built on MLX, focused on reliable tool calling for coding agents. Up to 4× faster than Apple's MLX (mlx-lm) on the same weights.

Tags: `anthropic-api` `apple-silicon` `claude-code` `coding-agents` `continuous-batching` `inference-server` `llm-inference` `llm-server`

### 16. [codex-router](https://github.com/duolahypercho/codex-router)

⭐ 3,917 · JavaScript · Updated 2026-10-06

External-model router for Codex with guided Kimi OAuth/API, DeepSeek, safe migration, and rollback.

Tags: `codex` `deepseek` `kimi` `litellm` `model-router`

### 17. [deepwiki-rs](https://github.com/sopaco/deepwiki-rs)

⭐ 2,670 · Rust · Updated 2026-09-14

Turn code into clarity. Generate accurate technical docs and AI-ready context in minutes—perfectly structured for human teams and intelligent agents.

Tags: `deepseek` `deepwiki` `dsh-plugin` `grok` `okf-format` `openwiki`

### 18. [myDshPresets](https://github.com/0liveiraaa/myDshPresets)

⭐ 80 · JavaScript · Updated 2026-08-19

用以解决DEEPSEEK思维链混乱,提高性能的插件

---

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md), then submit a project through an issue or pull request. Projects must be directly related to DeepSeek Harness and have a public repository.

## License

Released under the [Apache License 2.0](LICENSE).
