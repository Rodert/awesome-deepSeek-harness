# Awesome DeepSeek Harness

> DeepSeek Harness 外掛、工具與周邊專案精選清單。

[![Auto update](https://img.shields.io/badge/auto--update-daily-blue.svg)](.github/workflows/update-projects.yml) [![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

本清單由 GitHub 專案資料自動維護，同時保留人工整理的中文說明。歡迎提交專案或修正分類。

線上瀏覽：[GitHub Pages](https://rodert.github.io/awesome-deepSeek-harness/zh-TW/)

**Languages / 语言:** [简体中文](README.md) · [English](README.en.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [Français](README.fr.md) · [Español](README.es.md) · [Русский](README.ru.md) · [Português (Brasil)](README.pt-BR.md) · [Deutsch](README.de.md)

## 目錄

- [外掛](#plugins)
- [整合與 Agent](#integrations)
- [介面（TUI / Desktop / Web）](#interfaces)
- [生態與外掛市場](#ecosystem)
- [主題與外觀](#themes)
- [其他專案](#other)

> 專案數：**170** · 最後更新：**2026-09-01**

## 自動更新

採集器會透過 GitHub Search 自動發現 DeepSeek Harness 相關儲存庫，並更新 Star 數、語言、主題與更新時間。推送至 `main` 或每日排程都會觸發更新。

```bash
GITHUB_TOKEN=你的_token python scripts/collect_projects.py
python scripts/generate_markdown.py
```

<a id="plugins"></a>
## 外掛

*加入檔案引用、視覺、記憶等能力的外掛。*

### 1. [deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)

⭐ 206,712 · TypeScript · 更新於 2026-09-01

DeepSeek Harness: Everything is a Plugin.

標籤: `ai-agents` `cordis` `dsh` `dsh-plugin`

### 2. [CowAgent](https://github.com/zhayujie/CowAgent)

⭐ 46,739 · Python · 更新於 2026-09-01

Open-source super AI assistant & Agent Harness. Plans tasks, runs tools and skills, self-evolves with memory and knowledge. Multi-model, multi-channel. Lightweight, extensible, one-line install. (formerly chatgpt-on-wechat)

標籤: `ai` `ai-agent` `ai-agents` `chatgpt-on-wechat` `claude` `claude-code` `codex` `cowagent`

### 3. [archify](https://github.com/tt-a1i/archify)

⭐ 39,244 · JavaScript · 更新於 2026-09-01

Agent skill for beautiful, verifiable architecture, workflow, sequence, data-flow, and lifecycle diagrams—self-contained HTML with motion and crisp export.

標籤: `agent-skills` `architecture-as-code` `architecture-diagram` `claude-skill` `code-visualization` `codex` `coding-agents` `data-flow-diagram`

### 4. [PicGo](https://github.com/Molunerfinn/PicGo)

⭐ 27,106 · TypeScript · 更新於 2026-09-01

:rocket: The Ultimate Image Uploader for Efficient Creators. Supports Obsidian, Typora, VS Code etc. and 60+ image hosting services  (S3, GitHub, Cloudflare R2, Imgur, Aliyun OSS...). Paste, upload, done.

標籤: `aliyun-oss` `cloudflare-r2` `dsh-plugin` `electron` `electron-app` `electron-vue` `github` `image`

### 5. [distilly](https://github.com/titanwings/distilly)

⭐ 24,216 · Python · 更新於 2026-09-01

Distilly — Distill how they think into reusable Skills for any Agent or Bot. Formerly Colleague Skill（原同事 Skill）.

標籤: `agent-skills` `agentic-ai` `ai-agent` `ai-agents` `ai-assistants` `ai-persona` `claude-code` `claude-skills`

### 6. [colleague-skill](https://github.com/titanwings/colleague-skill)

⭐ 23,809 · Python · 更新於 2026-08-23

将冰冷的离别化为温暖的 Skill，欢迎加入数字生命1.0！Transforming cold farewells into warm skills? It's giving rebirth era. Welcome to Digital Life 1.0. 🫶

標籤: `agent-skills` `agentic-ai` `ai-agent` `ai-persona` `claude-code` `claude-code-skills` `codex` `codex-skills`

### 7. [WeKnora](https://github.com/Tencent/WeKnora)

⭐ 21,067 · Go · 更新於 2026-09-01

Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomous reasoning agent, and a self-maintaining Wiki.

標籤: `agent` `agentic` `ai` `chatbot` `dsh-plugin` `embeddings` `evaluation` `generative-ai`

### 8. [ai-guide](https://github.com/liyupi/ai-guide)

⭐ 19,352 · JavaScript · 更新於 2026-09-01

程序员鱼皮的 AI 资源大全 + Vibe Coding 零基础教程，分享 OpenClaw 保姆级教程、大模型玩法（DeepSeek / GPT / Gemini / Claude / GLM）、最新 AI 资讯、Prompt 提示词大全、AI 知识百科（Agent Skills / RAG / MCP / A2A）、AI 编程教程（Harness Engineering）、AI 工具用法（Cursor / Claude Code / TRAE / Codex / Copilot）、AI 开发框架教程（Spring AI / LangChain）、AI 产品变现指南，帮你快速掌握 AI 技术，走在时代前沿。本项目为开源文档 aiguide，已升级为鱼皮 AI 导航网站

標籤: `ai` `artificial-intelligence` `chatgpt` `claude` `codex` `cursor` `deep-learning` `deepseek`

### 9. [learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering)

⭐ 14,600 · TypeScript · 更新於 2026-09-01

Harness engineering beginner tutorial, from 0 to 1

標籤: `agent` `agentic` `agentic-ai` `ai` `ai-agent` `ai-agents` `dsh` `dsh-plugin`

### 10. [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin)

⭐ 13,920 · Python · 更新於 2026-09-01

A curated list of plugins for DeepSeek Harness (dsh) · DeepSeek Harness 插件精选列表

標籤: `awesome` `awesome-list` `deepseek-harness` `dsh` `dsh-plugin`

### 11. [EverOS](https://github.com/EverMind-AI/EverOS)

⭐ 12,603 · Python · 更新於 2026-09-01

One portable memory layer for every AI agent: local-first, Markdown-native, user-owned, and self-evolving across apps, tools, and workflows.

標籤: `agent-memory` `agentic-ai` `ai` `chats` `clawdbot` `clawdbot-skill` `deepseek-harness` `dsh`

### 12. [MemOS](https://github.com/MemTensor/MemOS)

⭐ 11,123 · TypeScript · 更新於 2026-09-01

Self-evolving memory OS for LLM & AI Agents: ultra-persistent memory, hybrid-retrieval, and cross-task skill reuse, with 35.24% token savings and DeepSeek Harness support.

標籤: `agent` `agentic-ai` `ai` `ai-agents` `chatgpt` `claude` `deepseek-harness` `dsh-plugin`

### 13. [dsh-routing-suite](https://github.com/yjh051108/dsh-routing-suite)

⭐ 7,000 · JavaScript · 更新於 2026-09-01

dsh-routing-suite — injector + router-standard kit: install the runtime injector first, then the task-aware reasoning-mode router preset (measured P1-P23).

標籤: `ai-agents` `cordis` `deepseek-harness` `dsh` `dsh-plugin`

### 14. [ouroboros](https://github.com/Q00/ouroboros)

⭐ 5,742 · Python · 更新於 2026-09-01

Agent OS: the agent gets smarter on its own. We just hold the line: the grading command and expected result never make it into the success contract we hand it. Interview-gated, staged evaluation, budgeted evolution loop. MCP server, 13 runtimes: Claude Code, Codex CLI, Gemini CLI, OpenCode, Copilot, Kiro and more.

標籤: `agent-os` `agentic-ai` `ai-agent` `ai-coding-agent` `claude-code` `cli` `codex` `coding-agent`

### 15. [loopx](https://github.com/huangruiteng/loopx)

⭐ 5,357 · Python · 更新於 2026-09-01

Long-horizon agent control plane for durable, governed work across Codex, Claude Code, and other harnesses.

標籤: `agent-control-plane` `agent-harness` `agent-ops` `ai-agents` `codex` `dsh-plugin` `long-horizon` `long-running-agents`

### 16. [iPolloWork](https://github.com/Devin-AXIS/iPolloWork)

⭐ 5,191 · TypeScript · 更新於 2026-09-01

Enterprise-grade, local-first Agent Workbench for people and agent teams. A unified multi-engine workspace for Codex Harness, DeepSeek Harness, and OpenCode, with unified plugins and Skills, multi-agent projects and tasks, and editable code, documents, presentations, design, and video.

標籤: `agent-collaboration` `agent-skills` `ai-agents` `ai-work` `claude-code` `codex` `codex-plugin` `deepseek-harness`

### 17. [petdex](https://github.com/crafter-station/petdex)

⭐ 4,011 · TypeScript · 更新於 2026-09-01

A public gallery of animated pets for Codex, Claude Code, DeepSeek Harness, Hermes, OpenCode, Gemini CLI, and more.

標籤: `claude-code` `clerk` `cli` `codex` `developer-tools` `drizzle-orm` `dsh-plugin` `mascot`

### 18. [dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard)

⭐ 3,814 · JavaScript · 更新於 2026-09-01

Two-phase DeepSeek Harness preset: Minimal-aligned bootstrap, then full Standard tools (Project2 98/99)

標籤: `deepseek` `deepseek-harness` `dsh-plugin` `llm-agent`

### 19. [mirage](https://github.com/strukto-ai/mirage)

⭐ 3,589 · TypeScript · 更新於 2026-09-01

The World's First Unified Virtual Filesystem For AI Agents

標籤: `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code` `dsh` `dsh-plugin` `fuse`

### 20. [ReMe](https://github.com/agentscope-ai/ReMe)

⭐ 3,378 · Python · 更新於 2026-08-31

ReMe: Memory Management Kit for Agents - Remember Me, Refine Me.

標籤: `agent` `ai-agents` `dsh-plugin` `memory` `memoryscope` `rag` `reme`

### 21. [OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw)

⭐ 3,125 · Python · 更新於 2026-09-01

本地私有、开源的自进化跨平台 AI 内容发现 Agent：先理解你，再主动从 B站、小红书、抖音、YouTube、X、知乎、Reddit、微博等平台与开放 Web 寻找内容。（支持 deepseek harness 插件） | Local-first open-source cross-platform AI content discovery agent: understands you, then proactively finds content across Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo and the open web.（support deepseek harness plugin）

標籤: `ai-agent` `bilibili` `chrome-extension` `content-discovery` `cross-platform` `deepseek-harness` `douyin` `dsh`

### 22. [J-Space-Cognition-Suite-V3.6](https://github.com/Tiger3807861189/J-Space-Cognition-Suite-V3.6)

⭐ 3,019 · Python · 更新於 2026-08-22

J-Space Cognition Suite V3.6 - AI cognitive-enhancement Skills based on Anthropic's J-space global workspace research. | 哔哩哔哩：Tiger380 (UID 3494375382321675) — https://space.bilibili.com/3494375382321675

標籤: `agent-skills` `ai` `ai-agent` `ai-agents` `claude-code` `codex` `cognitive-enhancement` `deepseek`

### 23. [zhuzhiliao](https://github.com/imsai-sh/zhuzhiliao)

⭐ 2,872 · HTML · 更新於 2026-09-01

竹知了 —— 一转就哇哇叫的传统玩具，Web 模拟版。零依赖单文件，真实录音采样，移动端优先。

### 24. [memsearch](https://github.com/zilliztech/memsearch)

⭐ 2,538 · Python · 更新於 2026-09-01

A persistent, unified memory layer for all your AI agents (e.g. Claude Code, Codex, DSH), backed by Markdown and Milvus.

標籤: `agent` `agent-memory` `ai-agents` `claude-code` `claude-code-plugin` `codex` `deepseek` `deepseek-harness`

### 25. [BrowserSkill](https://github.com/Tencent/BrowserSkill)

⭐ 1,501 · TypeScript · 更新於 2026-08-29

Let AI agents use your real, logged-in browser without interrupting your work. CLI + extension for browser automation across any shell-capable AI agent.

標籤: `agent` `browser-use` `dsh-plugin`

### 26. [brooks-lint](https://github.com/hyhmrright/brooks-lint)

⭐ 1,420 · JavaScript · 更新於 2026-08-27

AI code reviews grounded in 12 classic engineering books — decay risk diagnostics with book citations, severity labels, and 6 analysis modes including full-sweep auto-fix

標籤: `agent-skills` `ai-code-review` `architecture-review` `auto-fix` `claude-code` `claude-code-plugin` `clean-architecture` `code-health`

### 27. [dsh-agent-teams](https://github.com/NanmiCoder/dsh-agent-teams)

⭐ 1,237 · TypeScript · 更新於 2026-09-01

AgentTeams plugin for DeepSeek Harness

標籤: `agentteams` `deepseekharness` `dsh` `dsh-agent-teams` `dsh-plugin`

### 28. [dsh-context](https://github.com/bowenliang123/dsh-context)

⭐ 1,210 · TypeScript · 更新於 2026-09-01

The best DeepSeek Harness plugin for context insight and management, with context dashboard / browser and context command, for context statistics, composition, breakdown, evolution details, understanding how the context is made of, and how it evolves. 一站式 DeepSeek Harness 上下文可视化插件，Context 面板及浏览器与 Context 命令，透视上下文组成、演进、压缩、剪枝等事件与动作。

標籤: `cordis-plugin` `deepseek-harness` `deepseek-harness-plugin` `dsh-external` `dsh-plugin` `dsh-plugins`

### 29. [mem9](https://github.com/mem9-ai/mem9)

⭐ 1,198 · TypeScript · 更新於 2026-08-23

Unlimited memory for OpenClaw

標籤: `dsh-plugin`

### 30. [deepseek-harness-orange-book](https://github.com/alchaincyf/deepseek-harness-orange-book)

⭐ 1,144 · HTML · 更新於 2026-08-22

DeepSeek Harness橙皮书《从开机到拆开》：完整系统提示词、129行启动清单、三份原始会话日志——官方文档没有的一手实测。PDF/EPUB/HTML免费下载

### 31. [Aegis](https://github.com/GanyuanRan/Aegis)

⭐ 1,093 · Python · 更新於 2026-08-22

Make AI coding agents architecture-aware: baseline-first, evidence-verified, drift-checked, and safe across long tasks.

標籤: `agent-skills` `ai-agents` `ai-coding` `architecture-driven-development` `awsome-coding-plugin` `baseline-first` `claude-code` `codex`

### 32. [DeepSeek-V4-J-Space-Capability-Realization-Report](https://github.com/Tiger3807861189/DeepSeek-V4-J-Space-Capability-Realization-Report)

⭐ 1,038 · N/A · 更新於 2026-08-20

DeepSeek V4 × J-Space capability realization report — benchmark evidence that J-Space reduces capability-realization loss on DeepSeek V4 (Flash/Pro).

標籤: `agent-skills` `ai-agent` `benchmark` `deepseek` `deepseek-harness` `dsh` `dsh-plugin`

### 33. [dsh-im](https://github.com/xmanrui/dsh-im)

⭐ 1,037 · JavaScript · 更新於 2026-09-01

通过扫码或机器人凭据把IM机器人接入DeepSeek Harness（支持飞书、微信、钉钉、企业微信、QQ、Slack、Telegram、Discord和WhatsApp）。 Connect IM bots to DeepSeek Harness via QR code or credentials (9 channels).

標籤: `ai-agents` `chatbot` `cordis` `deepseek` `deepseek-harness` `dingtalk-bot` `discord-bot` `dsh`

### 34. [awesome-dsh-plugin](https://github.com/Anil-matcha/awesome-dsh-plugin)

⭐ 991 · N/A · 更新於 2026-09-01

A curated list of plugins for DeepSeek Harness (dsh) - DeepSeek Harness plugin ecosystem

標籤: `agent-harness` `ai-agent` `ai-agents` `autonomous-agent` `awesome` `awesome-list` `cli` `coding-agent`

### 35. [MindMemOS](https://github.com/mindscale-noah/MindMemOS)

⭐ 944 · Python · 更新於 2026-08-20

尚無專案簡介。

標籤: `agent` `agent-memory` `agent-skills` `agentic` `dsh-plugin` `dsh-plugins` `openclaw` `openclaw-agent`

### 36. [dsh-vision-toolkit](https://github.com/Anionex/dsh-vision-toolkit)

⭐ 847 · TypeScript · 更新於 2026-08-31

为 Harness 增加图片识别和视觉能力，适合处理 UI 截图、报错截图、网页截图和设计稿。

標籤: `agent-skills` `agent-vision-toolkit` `computer-vision` `deepseek` `deepseek-harness` `dsh` `dsh-plugin` `gui-automation`

### 37. [dsh-infinite-gen-3](https://github.com/Minglink/dsh-infinite-gen-3)

⭐ 740 · JavaScript · 更新於 2026-09-01

DeepSeek 专用破甲插件「无限三代」dsh-infinite-gen-3 — armor-breaking plugin for DeepSeek，破甲版：稳定化破甲，求 Star 收藏 ⭐

標籤: `armor-breaking` `deepseek` `deepseek-harness` `dsh-plugin`

### 38. [dsh-handbook](https://github.com/Electricitysheep/dsh-handbook)

⭐ 718 · HTML · 更新於 2026-09-01

DeepSeek Harness (dsh) 从 0 到 1 深度手册：安装/插件开发/性能调优/实测案例/同模型多 Agent 实测对比（中文 + 英文 PDF）

標籤: `agent` `agent-framework` `ai-agents` `beginners` `deepseek` `deepseek-ai` `dsh-plugin` `getting-started`

### 39. [dsh-infinite-gen-2](https://github.com/Minglink/dsh-infinite-gen-2)

⭐ 668 · PowerShell · 更新於 2026-08-31

DeepSeek 专用破甲插件「无限二代」dsh-infinite-gen-2 — armor-breaking plugin for DeepSeek稳定化破甲提示词，求 Star 收藏 ⭐

標籤: `armor-breaking` `deepseek` `deepseek-harness` `dsh-plugin`

### 40. [dsh-at-file](https://github.com/FSMargoo/dsh-at-file)

⭐ 500 · JavaScript · 更新於 2026-09-01

Codex-style @file mentions for DeepSeek Harness: search workspace files in the composer and attach their path to prompts.

標籤: `dsh` `dsh-plugin`

### 41. [dsh-at-file](https://github.com/omdsh-dev/dsh-at-file)

⭐ 437 · JavaScript · 更新於 2026-08-21

为 DeepSeek Harness 增加 @文件能力，可引用本地 PDF、Word、PPT、图片和代码文件。

標籤: `dsh` `dsh-plugin`

### 42. [anysearch-dsh](https://github.com/anysearch-team/anysearch-dsh)

⭐ 389 · TypeScript · 更新於 2026-08-31

AnySearch web search provider and advanced search tools for DeepSeek Harness (DSH)

標籤: `agent-tools` `anysearch` `deepseek-harness` `dsh` `dsh-plugin` `typescript` `web-search`

### 43. [dsh-genui](https://github.com/omdsh-dev/dsh-genui)

⭐ 384 · TypeScript · 更新於 2026-08-31

GenUI for DeepSeek Harness: interactive UI components rendered inline in assistant replies via the dsh-ui fence — layout, charts, plots, forms, quizzes, mermaid, 3D scenes, and an action event loop back to the model. Ships the fence-teaching host plugin, the browser renderer (client half), and the genui skill.

標籤: `dsh` `dsh-plugin`

### 44. [dsh-router-standard](https://github.com/yjh051108/dsh-router-standard)

⭐ 365 · JavaScript · 更新於 2026-08-30

已并入 dsh-routing-suite（单仓库化）；本仓库为历史镜像/归档 —— 注意力工程主线 v1.19.1/v34 研发线未发布。新代码见 github.com/yjh051108/dsh-routing-suite

標籤: `ai-agents` `cordis` `deepseek-harness` `dsh` `dsh-plugin`

### 45. [dsh-pentest](https://github.com/howmp/dsh-pentest)

⭐ 335 · JavaScript · 更新於 2026-08-31

面向 DeepSeek Harness（dsh）的渗透测试模式  @CloverSecLabs

標籤: `deepseek-harness` `dsh-plugin` `dsh-plugins` `pentest`

### 46. [dsh-mnemon](https://github.com/omdsh-dev/dsh-mnemon)

⭐ 304 · TypeScript · 更新於 2026-09-01

为多个 Agent 提供跨会话的长期记忆，帮助持续参与同一个项目。

標籤: `agent-memory` `context-management` `cross-session-memory` `deepseek-harness` `document-search` `dsh-plugin` `llm-memory` `local-first`

### 47. [awesome-dsh-plugin](https://github.com/bruc3van/awesome-dsh-plugin)

⭐ 303 · JavaScript · 更新於 2026-09-01

30 秒找到真正适合你的 DeepSeek Harness插件。每天自动抓取 GitHub 上的 `dsh-plugin` 项目并逐个复核：真实插件分类收录，蹭标签项目剔除。通过场景化分类、精选推荐、热度排行和图文导览，帮你快速看懂每个插件能做什么、适合谁，以及如何开始使用。欢迎 Star ，让好用的插件更快被发现。

標籤: `awesome-list` `deepseek-harness` `dsh` `dsh-plugin`

### 48. [dsh-mobile-apk](https://github.com/kelai141/dsh-mobile-apk)

⭐ 291 · TypeScript · 更新於 2026-09-01

dsh 安卓壳 APK——WebView UI + 内嵌 Termux 运行时快照（解压即跑），为dsh本地运行设计的高性能方案

標籤: `android` `dsh-plugin` `kotlin` `termux` `webview`

### 49. [dsh-image-gen](https://github.com/shanliuling/dsh-image-gen)

⭐ 290 · TypeScript · 更新於 2026-09-01

Generate images directly in DeepSeek Harness chats

標籤: `ai-agent` `cordis` `deepseek` `deepseek-harness` `dsh-plugin` `gemini` `image-generation` `openai`

### 50. [dsh-synapse](https://github.com/liangmianya/dsh-synapse)

⭐ 285 · JavaScript · 更新於 2026-09-01

A visual, non-linear conversation workspace plugin for DeepSeek Harness ; A canvas-based session explorer and branching workspace for DeepSeek Harness.

標籤: `deepseek` `deepseek-harness` `dsh` `dsh-plugin` `dsh-plugin-market` `dsh-plugins` `plugin`

### 51. [dsh-memory-evolve](https://github.com/csyangwen/dsh-memory-evolve)

⭐ 263 · JavaScript · 更新於 2026-08-31

为 DeepSeek Harness 带来「跨会话长期记忆 + 后台自我进化」能力的纯插件实现：五轨记忆 · git 分支感知 · 回合内自我审查 · 技能自我进化与技能管理器 · 四轨待办 · COI 调度 · 会话广播 · 会话搜索 · 提示词管理器 · 临时信息便签——零核心修改、零运行时依赖，随装随用、卸载即净。

標籤: `deepseek-harness` `dsh` `dsh-plugin`

### 52. [dsh-purge](https://github.com/YuJunZhiXue/dsh-purge)

⭐ 241 · JavaScript · 更新於 2026-09-01

DeepSeek Harness 破甲：让所有模型都能破甲，不同模型可换不同提示词；默认提示词面向国模「小码酱」。Jailbreak for every model — swap prompts per model. 求 Star 收藏 ⭐

### 53. [dsh-visualize](https://github.com/Nagi-ovo/dsh-visualize)

⭐ 235 · TypeScript · 更新於 2026-09-01

在 DSH 对话中生成交互式可视化｜Render model-generated interactive cards inside DSH conversations

標籤: `data-visualization` `deepseek-harness` `dsh-plugin` `interactive-visualization`

### 54. [dsh-cost-meter](https://github.com/Han-1413141/dsh-cost-meter)

⭐ 233 · JavaScript · 更新於 2026-09-01

DeepSeek Harness session cost meter plugin: session/daily cost, budget, history, OpenCode Go quota, official & custom-provider balance, Codex-like token heatmap, peak/off-peak pricing with pre-switch popup & system-notification alerts, official price sync, 90+ model pricing catalog, Coding Plan quota queries (7 vendors), bilingual zh/en UI

標籤: `cost-tracking` `deepseek` `deepseek-api` `deepseek-harness` `dsh` `dsh-plugin` `dsh-plugins` `harness`

### 55. [oh-story-dsh](https://github.com/zenstory-ai/oh-story-dsh)

⭐ 231 · JavaScript · 更新於 2026-09-01

A DSH plugin for novel writing and short-drama production, powered by Oh Story and Drama Skills.

標籤: `ai-agents` `creative-writing` `deepseek-harness` `drama-skills` `dsh-plugin` `fiction-writing` `novel-writing` `oh-story`

### 56. [dsh-univer-office](https://github.com/dream-num/dsh-univer-office)

⭐ 216 · TypeScript · 更新於 2026-09-01

Give DeepSeek Harness a real office environment.  Univer Office Plugin brings spreadsheets, docs, slides, canvases, relational tables, and more into one runtime — with connected data, validation, versioned changes, and isolated worktrees for multi-agent collaboration.

標籤: `deepseek-harness` `deepseek-harness-plugin` `dsh` `dsh-plugin` `office` `office-harness`

### 57. [dsh-top100](https://github.com/dsheval/dsh-top100)

⭐ 202 · TypeScript · 更新於 2026-09-01

尚無專案簡介。

### 58. [dsh-agent-rp](https://github.com/hewzhew/dsh-agent-rp)

⭐ 201 · TypeScript · 更新於 2026-09-01

SillyTavern migration and next-generation Agent RP for DSH

標籤: `agent` `dsh` `roleplay` `sillytavern`

### 59. [DSH-Launcher](https://github.com/MarcoG-h/DSH-Launcher)

⭐ 194 · TypeScript · 更新於 2026-09-01

最全面的DeepSeek Harness🐋启动器  *首创多实例管理中枢* | 多开并行 | 整合包下载 | 安全保护 | 一键部署 | 插件管理 |

標籤: `dsh` `dsh-launcher`

### 60. [dsh-evolve-modes](https://github.com/GraySilver/dsh-evolve-modes)

⭐ 193 · TypeScript · 更新於 2026-09-01

让 Agent 的工作方式可组合、可审查、可持续改进，最终实现 Agent Self Evoling。 DeepSeek Harness Web plugin with composable task controls and isolated, human-reviewed self-evolution.

標籤: `acceptance-review` `agent-review` `ai-agents` `deepseek-harness` `dsh` `dsh-plugin` `plan-mode` `prompt-engineering`

### 61. [dsh-launcher](https://github.com/Ruler4396/dsh-launcher)

⭐ 190 · C# · 更新於 2026-09-01

DeepSeek Harness（dsh）Windows 轻量启动器：双击即用，克制的原生体验 / Lightweight Windows launcher for DeepSeek Harness (dsh) — double-click to run, native & restrained

標籤: `deepseek` `deepseek-harness` `dsh-plugin` `launcher` `webview2`

### 62. [dsh-mobile](https://github.com/saya-ch/dsh-mobile)

⭐ 183 · TypeScript · 更新於 2026-08-31

DeepSeek Harness 的 Android App 与安全远程访问插件，支持局域网/远程连接和高度自定义的移动界面与扩展能力。

標籤: `android` `cpolar` `deepseek-harness` `dsh-plugin` `lan` `mobile` `remote-access` `tailscale`

### 63. [dsh-explore](https://github.com/antinomie-lab/dsh-explore)

⭐ 178 · Vue · 更新於 2026-08-31

Into the Unknown. —— 探索未至之境。

### 64. [pi2dsh](https://github.com/weijiafu14/pi2dsh)

⭐ 176 · TypeScript · 更新於 2026-08-31

Bridge the Pi and DeepSeek Harness ecosystems: one Pi Host ABI runs unmodified Pi extensions as native DSH plugins. 打通 Pi 与 DSH 生态。

標籤: `ai-agents` `compatibility-layer` `deepseek-harness` `dsh` `dsh-plugin` `migration` `pi` `pi-agent`

### 65. [dsh-find-plugins](https://github.com/Nagi-ovo/dsh-find-plugins)

⭐ 172 · JavaScript · 更新於 2026-08-31

帮 DSH 搜索、安装并验证插件的 Skill｜A DSH skill that finds, installs, and verifies GitHub plugins

標籤: `agent-skills` `deepseek-harness` `dsh-plugin` `plugin-discovery`

### 66. [dsh-oil-creator](https://github.com/oil-oil/dsh-oil-creator)

⭐ 172 · TypeScript · 更新於 2026-09-01

AI-assisted local creator workbench for DeepSeek Harness

標籤: `creator` `deepseek-harness` `dsh-plugin`

### 67. [dsh-remote-web-gateway](https://github.com/summer1238/dsh-remote-web-gateway)

⭐ 164 · TypeScript · 更新於 2026-08-30

手机平板远程 DeepSeek Harness：扫码即可继续使用电脑上的 DSH，无需远程桌面 / SSH / 公网 IP，支持一次性配对、Github授权加密登录，独立设备授权与随时撤销，实现远程连接很简单，但安全才是我们所想要的。

標籤: `cloudflare-tunnel` `deepseek` `deepseek-harness` `developer-tools` `dsh` `dsh-mobile-app` `dsh-model-switch` `dsh-plugin`

### 68. [dsh-plugin-bridge](https://github.com/Totoro-qaq/dsh-plugin-bridge)

⭐ 163 · JavaScript · 更新於 2026-08-30

DeepSeek Harness plugin for previewable cross-preset session migration. Fixed-schema handoffs preserve state, source-model intent, and unresolved images; the original session stays untouched.

標籤: `context-migration` `cordis` `deepseek-harness` `dsh` `dsh-plugin` `preset-migration` `session-migration`

### 69. [dsh-agent-team-gui](https://github.com/toolclub/dsh-agent-team-gui)

⭐ 162 · TypeScript · 更新於 2026-08-31

Persistent multi-model workflow teams for DeepSeek Harness — dynamic lead planning, bounded DAGs, per-agent model/tools, Run Center and Token insights.

標籤: `agent` `agent-orchestration` `ai-agents` `dag` `deepseek-harness` `deepseek-harness-plugin` `dsh` `dsh-plugin`

### 70. [oh-story-dsh](https://github.com/worldwonderer/oh-story-dsh)

⭐ 158 · Python · 更新於 2026-08-24

A DSH plugin for novel writing and short-drama production, powered by Oh Story and Drama Skills.

標籤: `ai-agents` `creative-writing` `deepseek-harness` `drama-skills` `dsh-plugin` `fiction-writing` `novel-writing` `oh-story`

### 71. [dsh-memory](https://github.com/seriousz158/dsh-memory)

⭐ 154 · JavaScript · 更新於 2026-09-01

尚無專案簡介。

標籤: `deepseek-harness` `dsh-bundle` `dsh-plugin` `memory`

### 72. [dsh-super-injector](https://github.com/yjh051108/dsh-super-injector)

⭐ 153 · TypeScript · 更新於 2026-08-31

推荐组件（非必须）：DeepSeek Harness 运行时注入器；已随 dsh-routing-suite 单仓库化保留，本仓库继续维护/发布。

標籤: `dsh` `dsh-plugin`

### 73. [dsh-redteam-model](https://github.com/SeaOf0/dsh-redteam-model)

⭐ 151 · Python · 更新於 2026-09-01

基于dsh web实现的多种模式，目的是服务于redteam进行授权的安全研究，覆盖渗透测试、红队评估、代码审计等范围领域，请勿用于非法行为。（允许二开，赋予模块各位自己的业务逻辑，方法论只有自己熟练的才好用，好的方法论=好的生态）

標籤: `dsh-plugin`

### 74. [dsh-damage-pulse](https://github.com/wssfk12138/dsh-damage-pulse)

⭐ 145 · TypeScript · 更新於 2026-08-31

DeepSeek Harness Token 余额监控插件：鲸鱼娘待机/扣费/复苏动画、峰谷计费、连续扣费飘字与会话费用统计。

標籤: `balance-monitor` `damage-animation` `deepseek` `deepseek-harness` `dsh` `dsh-plugin` `token-monitor` `token-usage`

### 75. [dsh-Mimir-Academic-research](https://github.com/1692775560/dsh-Mimir-Academic-research)

⭐ 145 · TypeScript · 更新於 2026-09-01

Mimir — 一站式科研工作台插件：LaTeX 论文边写边编译、arXiv 文献管理、实验追踪、指标图表、GPU 服务器 SSH 任务编排，管理科研全周期。An open-source research workbench plugin for the whole research cycle.

標籤: `arxiv` `bibtex` `deepseek` `deepseek-harness` `dsh-plugin` `experiment-tracking` `gpu-cluster` `latex`

### 76. [dsh-auto-mode](https://github.com/NanmiCoder/dsh-auto-mode)

⭐ 142 · TypeScript · 更新於 2026-09-01

Safe automatic permissions for DeepSeek Harness.

標籤: `deepseek-harness` `deepseekharness` `dsh` `dsh-auto-model` `dsh-plugin`

### 77. [dsh-infinite-gen-1](https://github.com/Minglink/dsh-infinite-gen-1)

⭐ 141 · PowerShell · 更新於 2026-08-21

DeepSeek 专用破甲插件「无限一代」dsh-infinite-gen-1 — armor-breaking plugin for DeepSeek，新一代全局破甲方案，求 Star 收藏 ⭐

### 78. [dsh-undo-savepoint](https://github.com/lire1131/dsh-undo-savepoint)

⭐ 140 · JavaScript · 更新於 2026-09-01

DSH crash-rescue plugin: undo config & plugin-code changes, secret-safe snapshots, one-click SAFE MODE, plus offline CLI/GUI that work even when DSH won't boot.

標籤: `backup` `crash-recovery` `deepseek-harness` `dsh` `dsh-plugin` `powershell` `rollback` `snapshot`

### 79. [dsh-gitbash-preset](https://github.com/liceses/dsh-gitbash-preset)

⭐ 136 · JavaScript · 更新於 2026-09-01

DeepSeek Harness 插件：一键安装「极简模式 (Git Bash)」agent preset —— 把 DSH 自带极简模式中的 bash 调用映射到 Git for Windows 的 bash（MSYS），让 Windows 上的极简模式真正可用。

標籤: `dsh` `dsh-plugin` `dsh-plugins`

### 80. [dsh-usage-stats](https://github.com/Ychris12138/dsh-usage-stats)

⭐ 135 · JavaScript · 更新於 2026-09-01

Provider balances, subscription quotas, and token-usage analytics for the DeepSeek Harness Web GUI (dsh web).

標籤: `deepseek` `deepseek-harness` `deepseek-harness-plugin` `deepseek-harness-plugin-dev` `deepseek-harness-plugins` `dsh` `dsh-plugin` `dsh-plugins`

### 81. [dsh-plugin-agent-workflow](https://github.com/xuanyuanzhifeng/dsh-plugin-agent-workflow)

⭐ 134 · TypeScript · 更新於 2026-09-01

DeepSeek Harness Agent Workflow

### 82. [dsh-noema](https://github.com/ZSeven-W/dsh-noema)

⭐ 128 · TypeScript · 更新於 2026-08-29

Noema long-term memory plugin for DSH: durable, inspectable agent memory with recall tools and a settings page.

標籤: `agent-memory` `ai-agents` `coding-agent` `deepseek-harness` `dsh` `dsh-plugin` `long-term-memory` `mcp`

### 83. [dsh-android](https://github.com/ZSeven-W/dsh-android)

⭐ 126 · TypeScript · 更新於 2026-08-30

DeepSeek Harness plugin for Android — build, run, and interact with a live emulator or USB device stream inside a conversation, driven entirely through adb.

標籤: `dsh-plugin`

### 84. [awesome-dsh-plugin](https://github.com/beancookie/awesome-dsh-plugin)

⭐ 123 · HTML · 更新於 2026-08-28

Awesome DeepSeek Harness (DSH) Plugin

標籤: `awesome` `awesome-list` `deepseek-harness` `dsh` `dsh-plugin`

### 85. [dsh-mcp](https://github.com/Mr-potato-123/dsh-mcp)

⭐ 118 · JavaScript · 更新於 2026-08-26

dsh as mcp, make your claude code or codex etc. faster, more powerful and more economic!

### 86. [dsh-reasoning-effort](https://github.com/HanaAyane/dsh-reasoning-effort)

⭐ 108 · TypeScript · 更新於 2026-08-24

DSH适用的Codex风格的思考强度滑块，以及大肥鱼跑步滑块。Codex-style model and reasoning-effort slider for DeepSeek Harness

標籤: `deepseek` `deepseek-harness` `dsh-plugin` `reasoning-effort`

### 87. [DSH_tensorflow](https://github.com/yg33717/DSH_tensorflow)

⭐ 105 · Python · 更新於 2025-12-24

implemement of DEEP SUPERVISED HASHING FOR FAST IMAGE RETRIEVAL_CVPR2016

標籤: `deep` `hashing`

### 88. [dsh-turn-rewind](https://github.com/Anionex/dsh-turn-rewind)

⭐ 96 · JavaScript · 更新於 2026-08-22

deepseek harness对话和代码状态回退插件 | DSH — rewind conversation and workspace state, powered by a persistent Change Ledger

標籤: `agent-rewind` `cordis-plugin` `deepseek-harness` `dsh` `dsh-plugin` `marisa-plugin` `restore-point` `turn-rewind`

### 89. [dsh-vscode-layout](https://github.com/anoslide/dsh-vscode-layout)

⭐ 96 · JavaScript · 更新於 2026-08-22

把 DeepSeek Harness（dsh）Web 界面改造成 VS Code 式 IDE：三栏布局、文件树、多标签查看器/编辑器、桌面启动器，全部补丁可重放（MIT）

### 90. [dsh_workflow](https://github.com/omdsh-dev/dsh_workflow)

⭐ 94 · TypeScript · 更新於 2026-08-21

把Claude Code的UltraCode模式带给DSH，把 DSH 的一次性多 Agent 调度，升级为可生成、可保存、可治理、可观察、可恢复的 Workflow 层

標籤: `agent-orchestration` `deepseek-harness` `dsh` `dsh-plugin` `dshtopic` `multi-agent` `workflow`

### 91. [dsh-chat-import](https://github.com/Nwflower/dsh-chat-import)

⭐ 85 · JavaScript · 更新於 2026-08-20

Import 14+ external agent chat histories (Claude Code, Codex, ChatGPT, Cursor, Gemini, Reasonix, opencode, ZCode, Grok Build, OpenClaw, Pi, Hermes, Kimi CLI, DSH) into DeepSeek Harness as resumable sessions — full-fidelity, reverse export/sync, bundle backup. | 从 Claude Code、Codex、Reasonix 等 Agent 工具导入历史消息到 DeepSeek Harness 并继续对话。

標籤: `agent` `ai-agents` `automation` `chatgpt` `claude-code` `codex` `cursor` `deepseek`

### 92. [dsh-annotation](https://github.com/omdsh-dev/dsh-annotation)

⭐ 84 · HTML · 更新於 2026-08-20

DSH Web 选中批注插件：选文字→批注→回车随消息发送；气泡隐藏批注块（零闪烁）；回复按 Annotation N 逐条对照（可悬浮芯片）。官方 bundle，零核心改动

標籤: `dsh` `dsh-plugin`

### 93. [dsh-demo-webrtc-examples](https://github.com/deepstreamIO/dsh-demo-webrtc-examples)

⭐ 80 · JavaScript · 更新於 2026-05-18

尚無專案簡介。

### 94. [hello-dsh](https://github.com/pingfanfan/hello-dsh)

⭐ 78 · Python · 更新於 2026-08-19

从零开始，看懂 DeepSeek Harness 的「万物皆可插件」— 零基础插件开发教程（含 22 个中文技能实例）| Zero-to-plugin tutorial for DeepSeek Harness

標籤: `ai-agent` `chinese` `cordis` `deepseek` `deepseek-harness` `dsh` `dsh-plugin` `tutorial`

### 95. [awesome-DSH-plugin](https://github.com/Alex-Yanggg/awesome-DSH-plugin)

⭐ 74 · Python · 更新於 2026-08-19

A meticulously curated list of useful plugins, extensions, tools and development resources built for DSH, covering productivity enhancement, functional expansion, debugging utilities and custom development modules.

標籤: `agents` `awesome` `awesome-list` `deepseek` `dsh-plugin` `plugins`

---

<a id="integrations"></a>
## 整合與 Agent

*連接資料庫、設計工具與其他工作流程的專案。*

### 1. [openpencil](https://github.com/ZSeven-W/openpencil)

⭐ 5,756 · Rust · 更新於 2026-09-01

The world's first open-source AI-native vector design tool and the first to feature concurrent Agent Teams. Design-as-Code. Turn prompts into UI directly on the live canvas. A modern alternative to Pencil.

標籤: `agent` `agent-team` `ai` `claude` `claude-code` `codex` `dsh-plugin` `fimga`

### 2. [modlens](https://github.com/liustack/modlens)

⭐ 3,808 · TypeScript · 更新於 2026-09-01

The first vision plugin for DeepSeek Harness, and the vision bridge for every text-only coding agent. Paste an image, get structured JSON evidence (OCR, layout, semantics). | 全网最强 DeepSeek Harness 外挂视觉插件，为 DeepSeek、GLM 等纯文本模型外挂视觉能力，粘贴图片即得结构化 JSON 证据（OCR、版面、语义）。

標籤: `agent-skills` `claude-code` `claude-skills` `codex` `cordis` `deepseek` `dsh` `dsh-plugin`

### 3. [agent-vision-toolkit](https://github.com/Anionex/agent-vision-toolkit)

⭐ 1,094 · Python · 更新於 2026-08-21

为纯文本模型"看图“设计更好的视觉工具箱和技能，支持多图理解，图片问答，前端UI还原、GUI 自动化等，并可选无缝接入多个主流agent，直接识别粘贴图片｜ A vision toolkit and skill designed for text-only llms — image Q&A, long-screenshot OCR, frontend UI restoration, and GUI automation, with optional seamless integration for Codex, Claude Code, Pi, Oh My Pi, and OpenCode

標籤: `agent` `agent-skills` `claude-code` `codex` `computer-use` `deepseek` `dsh-plugin` `glm`

### 4. [dsh-vision-router](https://github.com/ysr666/dsh-vision-router)

⭐ 1,041 · JavaScript · 更新於 2026-09-01

Eyes for text-only DeepSeek Harness agents: built-in free vision chain (no key) + pixel-level vision tools (Q&A, grounding, crop, pixel diff, colors, OCR, SVG trace, cutout, screenshots). One-command install, no Python, image turns work like ordinary tool-calling turns.

標籤: `deepseek-harness` `dsh` `dsh-plugin` `multimodal` `vision`

### 5. [dsh-data-agent](https://github.com/omdsh-dev/dsh-data-agent)

⭐ 185 · JavaScript · 更新於 2026-09-01

连接 Agent 与数据库，用自然语言查询并分析订单、销售额等业务数据。

標籤: `data-agent` `deepseek-harness` `dsh` `dsh-plugin`

### 6. [dsh-openpencil](https://github.com/ZSeven-W/dsh-openpencil)

⭐ 156 · TypeScript · 更新於 2026-08-30

将 Agent 与设计画布结合，把 Harness 带入设计、产品和原型工作流。

標籤: `deepseek-harness` `design` `dsh` `dsh-plugin` `openpencil` `ppt` `ui` `ui-design`

### 7. [dsh-crew](https://github.com/ZSeven-W/dsh-crew)

⭐ 113 · JavaScript · 更新於 2026-08-26

DeepSeek Harness (DSH) plugin: dispatch work to DSH agents from Claude Code / Codex — native subagent progress, in-host worker sessions with per-tier presets, and a multimodal bridge that lends the text-only harness vision and image generation.

標籤: `ai-agents` `claude-code` `codex` `coding-agent` `deepseek-harness` `dsh` `dsh-plugin` `mcp`

---

<a id="interfaces"></a>
## 介面（TUI / Desktop / Web）

*將 Harness 帶到終端機、桌面或 Web 的用戶端。*

### 1. [open-design](https://github.com/nexu-io/open-design)

⭐ 93,099 · TypeScript · 更新於 2026-09-01

🎨 Best DeepSeek Harness Design Plugin. The open-source Claude Design alternative. 🖥️ Local-first desktop app. 🖼️ Your coding agent becomes the design engine: prototypes, landing pages, dashboards, slides, images & video — real files, HTML/PDF/PPTX/MP4 export. 🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode & 20+ CLIs via BYOK.

標籤: `agent-skills` `ai-design` `byok` `claude-code-for-design` `claude-design` `codex-design` `coding-agents` `cursor-design`

### 2. [OmniRoute](https://github.com/diegosouzapw/OmniRoute)

⭐ 59,367 · TypeScript · 更新於 2026-09-01

Never stop coding. Free MIT AI gateway: one endpoint, 352 providers (150+ free), 1200+ models Kimi, Claude, GPT, Gemini, GLM, DeepSeek, MiniMax. Works with Claude Code, Codex, Cursor, OpenCode, Cline & Copilot. Quota-aware auto-fallback, RTK+Caveman compression saves 15-95% tokens, MCP/A2A, Desktop/PWA. Built by 550+ contributors

標籤: `a2a` `ai-agents` `ai-gateway` `anthropic` `claude` `claude-code` `cline` `codex`

### 3. [dsh-desktop](https://github.com/anywhere-labs/dsh-desktop)

⭐ 22,511 · TypeScript · 更新於 2026-09-01

为 DeepSeek Harness (DSH) 插件生态打造的现代化桌面端解决方案。万物皆「插件」，桌面本身也是「插件」。

標籤: `cordis` `cordis-plugin` `deepseek` `deepseek-harness` `desktop` `dsh` `dsh-plugin` `dsh-plugin-desktop`

### 4. [voyager](https://github.com/Nagi-ovo/voyager)

⭐ 19,913 · TypeScript · 更新於 2026-09-01

Enhancement suite for Gemini, AI Studio, Claude & ChatGPT — plus a prompt manager for any web UI, DeepSeek Harness included. / 面向 Gemini、AI Studio、Claude 与 ChatGPT 的增强套件；提示词管理器可用于任意 Web UI，含 DeepSeek Harness。

標籤: `ai-studio` `browser-extension` `bun` `chat-management` `chatgpt` `chrome-extension` `claude-ai` `dsh`

### 5. [deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop)

⭐ 18,946 · TypeScript · 更新於 2026-08-24

DeepSeek Harness 的桌面端，以传统桌面软件的方式使用 Harness。

標籤: `cordis` `cordis-plugin` `deepseek` `deepseek-harness` `desktop` `dsh` `dsh-plugin` `dsh-plugin-desktop`

### 6. [FreeToken](https://github.com/FlashML-org/FreeToken)

⭐ 10,682 · Python · 更新於 2026-09-01

FreeToken brings datacenter-scale model serving to your desktop. Run massive models locally, fast and efficiently.

標籤: `deepseek-v4` `edge` `glm` `inference` `minimax` `moe` `qwen` `transformer`

### 7. [yao](https://github.com/YaoApp/yao)

⭐ 7,847 · Go · 更新於 2026-09-01

✨ All your agents and workspaces in one place, on every device you own. Track tasks on a board, accessible from desktop, mobile, browser, or API. Self-hosted.

標籤: `agent-harness` `agent-orchestration` `agent-skills` `agent-workspaces` `ai-agents` `ai-native` `claude-code` `coding-agent`

### 8. [desktop-cc-gui](https://github.com/zhukunpenglinyutong/desktop-cc-gui)

⭐ 4,120 · TypeScript · 更新於 2026-08-31

Multi-engine AI coding desktop client (Tauri). Claude Code, Codex, Gemini, OpenCode, DeepSeek Harness and more in one GUI.

標籤: `ai-coding` `claude-code` `codex` `deepseek-harness` `desktop-app` `dsh` `tauri` `vibe-coding`

### 9. [dsh-desktop](https://github.com/dataelement/dsh-desktop)

⭐ 3,577 · TypeScript · 更新於 2026-09-01

DSHDesktop：DeepSeek Harness Desktop / DeepSeek Harness 桌面版

標籤: `agent` `apps` `deepseek` `deepseek-harness` `deepseek-harness-desktop` `desktop` `dsh-plugins` `dshdesktop`

### 10. [DSH-better-sidebar](https://github.com/omdsh-dev/DSH-better-sidebar)

⭐ 3,187 · TypeScript · 更新於 2026-09-01

增强 DeepSeek Harness 的侧边栏、工作区和日常操作体验。

標籤: `deepseek` `deepseek-harness` `dsh` `dsh-better-sidebar` `dsh-plugin` `sidebar`

### 11. [EchoBird](https://github.com/edison7009/EchoBird)

⭐ 3,152 · Rust · 更新於 2026-09-01

One-click install + model switch:Claude Code,Codex CLI (OpenAI), Grok Build (xAI), DeepSeek Harness, Kimi Code (Moonshot) ,Qwen Code,Aider,OpenCode,MiMo Code (Xiaomi),ZCode (Z.AI),OpenClaw,Pi,OpenScience,Vibe-Trading,Claude Desktop (3P profile),ChatGPT desktop,OpenCode Desktop,

標籤: `claude-code` `deepseek` `deepseek-harness` `dsh-plugin` `dsh-plugins` `kimi-code` `openclaw` `opencode`

### 12. [codeg](https://github.com/xintaofei/codeg)

⭐ 3,079 · Rust · 更新於 2026-09-01

Collaborative multi-agent AI coding workspace: aggregate sessions from Claude Code, Codex, OpenCode, Pi, Grok Build, etc. Desktop app, self-hosted server, or Docker.

標籤: `acp` `ade` `agent` `claude-code` `code-generation` `codex` `deepseek-harness` `grok-build`

### 13. [clawpanel](https://github.com/qingchencloud/clawpanel)

⭐ 2,935 · JavaScript · 更新於 2026-09-01

🦞 OpenClaw & Hermes Agent 多引擎 AI 管理面板 — 内置 AI 助手（工具调用 + 图片识别 + 多模态），一键安装 | Tauri v2 跨平台桌面应用 | 11 种语言

標籤: `admin-panel` `ai-agent` `ai-assistant` `ai-chat` `ai-tools` `chatgpt` `cross-platform` `deepseek`

### 14. [dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard)

⭐ 2,833 · JavaScript · 更新於 2026-09-01

现代化可灵活嵌入的任务面板，支持 Codex、DeepSeek Harness

標籤: `claude-code` `cli` `codex` `codex-app` `codex-desktop` `codex-plugin` `dsh` `dsh-plugin`

### 15. [dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI)

⭐ 2,748 · TypeScript · 更新於 2026-09-01

将 DeepSeek Harness 带到终端，适合喜欢 Claude Code、Codex CLI 等 TUI 工作方式的用户。

標籤: `claude-code` `coding-agent` `deepseek` `deepseek-harness` `dsh-plugin` `ink` `react` `terminal`

### 16. [token-monitor](https://github.com/Javis603/token-monitor)

⭐ 1,860 · JavaScript · 更新於 2026-09-01

Local-first desktop widget for tracking token usage, costs, and limits across 33+ AI coding tools—including Claude Code, Codex, Cursor, OpenCode, and OpenClaw—with multi-device sync.

標籤: `ai` `ai-tools` `antigravity` `claude-code` `codex` `cursor` `deepseek` `deepseek-harness`

### 17. [deepseek-harness-desktop](https://github.com/dsh-tauri-desk/deepseek-harness-desktop)

⭐ 1,501 · Rust · 更新於 2026-09-01

DeepSeek Harness Tauri 桌面版 | Only 5mb installer, zero environment setup, preset plugins, Windows / macOS / Linux.

標籤: `deepseek` `deepseek-harness` `desktop` `dsh` `dsh-desktop` `dsh-plugin` `tauri`

### 18. [TokenTracker](https://github.com/xiufengsun/TokenTracker)

⭐ 1,450 · JavaScript · 更新於 2026-08-29

Local-first AI token usage & cost tracker for 31 coding tools incl. Claude Code, Codex, Cursor, Gemini & DeepSeek Harness—with native apps. Never reads prompts.

標籤: `ai-coding-tools` `ai-tools` `antigravity` `claude-code` `cli` `codex-cli` `cost-tracker` `cursor`

### 19. [agentrq](https://github.com/agentrq/agentrq)

⭐ 1,086 · Go · 更新於 2026-08-21

AgentRQ: Human-in-loop realtime conversational task manager for AI Agents. Self-hosted! Control your own agents from wherever you want Mobile, Web, Desktop. Designed to work well with your own Claude subscriptions and any harness.

標籤: `acp-client` `acp-gateway` `agentic-ai` `agentic-workflow` `agents` `claude-code` `deepseek-harness` `deepseek-harness-plugin`

### 20. [dsh-desktop](https://github.com/vibeinging/dsh-desktop)

⭐ 635 · JavaScript · 更新於 2026-08-30

DeepSeek Harness Desktop App: a local AI desktop workspace for DSH Sessions, projects, files, web research, plugins, and Office artifacts.

標籤: `agentic-workflows` `ai-agent` `ai-workbench` `data-analysis` `deepseek-harness` `desktop-app` `dsh` `dsh-plugin`

### 21. [dsh_desktop](https://github.com/myYangyunfan/dsh_desktop)

⭐ 615 · JavaScript · 更新於 2026-09-01

DeepSeek Harness (dsh) Windows desktop client - bundled Node.js + dsh CLI, one-click launch

標籤: `ai-agent` `cordis` `deepseek` `deepseek-harness` `desktop` `desktop-app` `dsh` `dsh-desktop`

### 22. [dshcode](https://github.com/whitelonng/dshcode)

⭐ 614 · TypeScript · 更新於 2026-09-01

Community desktop companion for DeepSeek Harness — one-click Electron app for macOS and Windows

標籤: `agent` `deepseek` `deepseekharness-plugin` `dsh-plugin` `harness`

### 23. [dsh-ads](https://github.com/Nagi-ovo/dsh-ads)

⭐ 595 · TypeScript · 更新於 2026-08-31

把 DSH 变成 2005 年门户网站｜Parody ads, fake games, and popups for the DSH Web UI

標籤: `deepseek-harness` `dsh-plugin` `trolling` `web-ui`

### 24. [dsh-browser](https://github.com/Lum1104/dsh-browser)

⭐ 540 · TypeScript · 更新於 2026-09-01

Chrome sidebar extension that lets DeepSeek Harness operate your browser directly, no vision capabilities required. 一款 Chrome 侧边栏扩展程序，可让 DeepSeek Harness 直接操控您的浏览器，无需视觉能力。

標籤: `browser-automation` `chrome-extension` `coding-agent` `cordis` `deepseek` `deepseek-harness` `dsh` `dsh-plugin`

### 25. [dsh-pet](https://github.com/PC2005-cloud/dsh-pet)

⭐ 493 · TypeScript · 更新於 2026-09-01

DSH 桌面宠物：一行命令装好即用的透明动画小桌宠，支持多开、大小位置随心配置；还内置 DIY 素材链，能用 AI 视频自造专属宠物

標籤: `deepseek-harness` `desktop-pet` `dsh` `dsh-plugin`

### 26. [dsh-worktable](https://github.com/Aisland-SJL/dsh-worktable)

⭐ 417 · JavaScript · 更新於 2026-09-01

🖥️ Agent-project workbench for DeepSeek Harness — sidebar app drawer + dockable split workspace + a live control room watching every project.

標籤: `agent` `deepseek` `deepseek-harness` `dsh` `dsh-plugin` `productivity` `web-gui` `workspace`

### 27. [DSHA](https://github.com/qiannianhuanxiang/DSHA)

⭐ 350 · Java · 更新於 2026-09-01

免 ROOT 免 Termux，在手机上跑 DeepSeek Harness。完整 Ubuntu 环境 + proroot 零 ptrace 开销 · AI 输出实时上屏 · ADB 直连 · 数据不丢

標籤: `android` `coding-agent` `deepseek` `deepseek-harness` `launcher` `llm` `proot` `proroot`

### 28. [dsh-plugin-subscriptions](https://github.com/V1ki/dsh-plugin-subscriptions)

⭐ 305 · TypeScript · 更新於 2026-09-01

Use ChatGPT (Codex), Claude, and Grok (X Premium) subscriptions as DeepSeek Harness LLM providers — OAuth login in the web UI, no API keys

標籤: `ai-agent` `chatgpt` `claude` `codex` `deepseek-harness` `dsh-plugin` `grok` `llm`

### 29. [oh-dsh](https://github.com/hust-open-atom-club/oh-dsh)

⭐ 297 · TypeScript · 更新於 2026-09-01

同时覆盖 TUI、Desktop 和 Web 的 DeepSeek Harness 发行形态。

標籤: `ai-agent` `cordis` `deepseek-harness` `dsh` `dsh-plugin` `dsh-plugins`

### 30. [dsh-dafeiyu](https://github.com/QCYTSN/dsh-dafeiyu)

⭐ 284 · JavaScript · 更新於 2026-09-01

Desktop-native BigFish companion for DeepSeek Harness — real Agent status, always on top on Windows.

標籤: `agent-companion` `deepseek-harness` `desktop-pet` `dsh-plugin` `windows`

### 31. [dsh-ios](https://github.com/ZSeven-W/dsh-ios)

⭐ 270 · TypeScript · 更新於 2026-08-31

DeepSeek Harness (DSH) plugin: a live iOS Simulator — and a USB-connected iPhone — inside the conversation. 22 agent tools for booting, building, driving the UI by accessibility identity, OCR text or list rows, plus a streaming sidebar panel you can tap and drag on.

標籤: `accessibility` `ai-agents` `coding-agent` `deepseek-harness` `dsh` `dsh-plugin` `ios` `ios-simulator`

### 32. [dsh-tianshu-tui](https://github.com/huiliyi37/dsh-tianshu-tui)

⭐ 251 · TypeScript · 更新於 2026-08-31

官方 DeepSeek Harness 的交互式终端 UI 插件：自研 ANSI 极简交互渲染、流式 Markdown/工具卡、16+ 主题、slash 命令与选择器、输入历史与本地偏好持久化、LSP 诊断、memory记忆，很丝滑的开发体验。

標籤: `coding` `dsh` `dsh-plugin` `harness` `harness-engineering` `tui`

### 33. [DSH-taskboard](https://github.com/shengsheng90/DSH-taskboard)

⭐ 247 · TypeScript · 更新於 2026-09-01

Native local Taskboard plugin for DeepSeek Harness. SQLite-backed projects, Agent claim/review, and a native Web UI — no iframe, no second chat runtime.

標籤: `agent` `cordis` `deepseek-harness` `dsh` `dsh-plugin` `task-management` `taskboard`

### 34. [dsh-pet-indesktop](https://github.com/MerZlin/dsh-pet-indesktop)

⭐ 221 · Python · 更新於 2026-08-31

基于项目git@github.com:PC2005-cloud/dsh-pet.git，将桌宠移植到Windows和MacOS上，现在可以随时看到蓝色大肥鱼了：）

### 35. [dsh-popout-sidebar](https://github.com/e2mcc/dsh-popout-sidebar)

⭐ 180 · JavaScript · 更新於 2026-09-01

A sidebar can pop out a separate browser tab (drag it to another monitor)

標籤: `dsh-plugin`

### 36. [dsh-skill-mcp-panel](https://github.com/Fishquito7/dsh-skill-mcp-panel)

⭐ 86 · JavaScript · 更新於 2026-08-20

DSH Web UI plugin: skill and MCP management（Web界面的skill/MCP管理工具）

標籤: `deepseek` `dsh` `dsh-plugin` `mcp` `plugin` `skills`

---

<a id="ecosystem"></a>
## 生態與外掛市場

*協助發現、安裝與管理 Harness 專案的基礎設施。*

### 1. [dsh-web](https://github.com/zhu1090093659/dsh-web)

⭐ 6,607 · TypeScript · 更新於 2026-09-01

DeepSeek Harness (DSH) Web Plugin Aggregation Ecosystem · Everything is a plugin, distributed via the Creative Workshop

標籤: `cordis` `deepseek-harness` `dsh` `dsh-plugin` `dsh-web` `dsh-web-ui`

### 2. [dsh-market](https://github.com/dsh-market/dsh-market)

⭐ 2,942 · TypeScript · 更新於 2026-09-01

集中发现、安装和管理 DeepSeek Harness 插件的插件市场。

標籤: `deepseek-harness` `dsh-plugin` `marketplace`

### 3. [dsh-plugin-radar](https://github.com/AdamPlatin123/dsh-plugin-radar)

⭐ 1,437 · Python · 更新於 2026-09-01

DSH Plugin Radar — 开源 DSH 插件生态雷达：自动发现 15900+ 候选、k8s 运行级实测 10000+、15 分钟快照管线；插件目录是其自动生成的 artifact

標籤: `agent-plugins` `continuous-validation` `deepseek-harness` `dsh` `dsh-plugin` `ecosystem-radar` `plugin-registry`

### 4. [awesome-dsh-plugins](https://github.com/AdamPlatin123/awesome-dsh-plugins)

⭐ 1,422 · Python · 更新於 2026-08-28

DSH 插件雷达与精选榜：多路自动发现 14900+ 候选，容器真实安装路径运行级实测（四档判定），精选 Top 50 · 11 类人工策展，全量索引 PLUGINS-ALL.md，自动更新。

標籤: `agent-plugins` `awesome-list` `deepseek-harness` `dsh` `dsh-plugin` `plugin-registry`

### 5. [dsh-pocket](https://github.com/shaobeichen/dsh-pocket)

⭐ 865 · JavaScript · 更新於 2026-09-01

把 DeepSeek Harness 装进你的口袋：电脑上跑 dsh web，手机扫码即同步访问（局域网 + 公网，实时同屏）Put DeepSeek Harness in your pocket: run dsh web on your computer and access it synchronously by scanning a QR code on your phone (LAN + public network, real‑time screen mirroring)

標籤: `deepseek` `deepseek-harness` `deepseek-harness-plugin` `dsh` `dsh-plugin` `dsh-plugin-market` `dsh-plugins` `mobile`

### 6. [dshfind](https://github.com/hikariming/dshfind)

⭐ 237 · TypeScript · 更新於 2026-08-31

DSH (DeepSeek Harness) 原理学习、插件市场与最佳实践 · Learn DSH principles, plugin marketplace & best practices

標籤: `deepseek-harness` `dsh` `dsh-plugin`

### 7. [dsh-wallpaper-engine](https://github.com/elysia395/dsh-wallpaper-engine)

⭐ 223 · JavaScript · 更新於 2026-09-01

把本机 Wallpaper Engine 的壁纸变成 DSH 网页界面的背景：Video 动态播放、Web 以 iframe 加载、Scene 壁纸提取主纹理作为静态帧；iOS 液态玻璃设置窗口（配色 / 玻璃颜色 / 透明度）、内容分级与类型过滤、自定义壁纸上传、紧凑 CD 架布局、黑胶唱片展示、隐藏 / 恢复、倍速 / 翻转与自动轮播。感谢 Jerry 维护 macOS 版。

標籤: `deepseek-harness` `dsh-plugin` `dsh-plugin-market` `dsh-plugins` `liquid-glass` `theme` `wallpaper-engine`

### 8. [DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace)

⭐ 152 · JavaScript · 更新於 2026-08-31

DSH插件市场 / DSH Plugin Marketplace: 在 DeepSeek Harness Web GUI 中一键浏览、安装与更新 GitHub topic:dsh-plugin 的全部插件 | browse, install & update all GitHub dsh-plugin plugins in the DSH Web GUI

標籤: `agent` `ai-agents` `cordis` `deepseek-harness` `dsh` `dsh-plugin` `javascript` `llm`

### 9. [dsh-webui-market-plugin](https://github.com/Sanqi-normal/dsh-webui-market-plugin)

⭐ 100 · JavaScript · 更新於 2026-08-22

dsh Web GUI 社区插件市场：浏览 awesome-dsh-plugin.com 插件目录，一键安装/卸载到 profile。Community plugin market for the DeepSeek Harness (dsh) web GUI: browse, install and uninstall plugins into a profile.

標籤: `agent-harness` `deepseek` `dsh-plugin` `plugin-market` `ui` `web`

### 10. [dsh-plugin](https://github.com/Tabbit-Browser/dsh-plugin)

⭐ 90 · JavaScript · 更新於 2026-08-19

Tabbit Broser plugins for Deepseek Harness

標籤: `browser-automation` `browser-use` `deepseek-harness` `dsh-plugin` `dsh-plugin-market` `dsh-plugin-verify` `dsh-plugins` `playwright`

---

<a id="themes"></a>
## 主題與外觀

*主題、外觀與視覺增強專案。*

### 1. [CodeWhale](https://github.com/Hmbown/CodeWhale)

⭐ 40,829 · Rust · 更新於 2026-08-20

Open-source, community-driven agent harness

標籤: `ai` `ai-agent` `alibaba-cloud` `anthropic` `cli` `coding-agent` `deepseek` `deepseek-harness`

### 2. [dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui)

⭐ 5,748 · TypeScript · 更新於 2026-08-24

DeepSeek Harness（DSH）Web GUI 插件与皮肤生态：一切皆插件。任务看板、移动端远程与 SSH 运维构筑开发工作台；皮肤经 WebGL 深度优化，更支持 Wallpaper Engine 壁纸；皮肤、宠物、插件由 DSH 大市场一键安装，正迈向 DSH 创意工坊。A pluggable plugin-skin ecosystem for the DSH Web GUI - Task board, remote mobile UI, SSH ops, WebGL-optimized skins with Wallpaper Engine wallpapers - becoming a DSH creative workshop.

標籤: `cordis` `deepseek-harness` `dsh` `dsh-plugin` `dsh-web` `dsh-web-ui`

### 3. [dsh-deep-whale](https://github.com/Small-tailqwq/dsh-deep-whale)

⭐ 1,860 · TypeScript · 更新於 2026-09-01

面向 DeepSeek Harness 的主题和皮肤项目，让 Agent 工作区更具个性。

標籤: `dsh` `dsh-plugin`

### 4. [DSH-Desktop-EAC](https://github.com/zouyuxuan122/DSH-Desktop-EAC)

⭐ 1,474 · JavaScript · 更新於 2026-09-01

DeepSeek Harness Desktop (dsh-desktop). EAC: Embracing All Creation (揽尽万象). Bundled Node.js runtime with full dsh-CLI kernel, one-click startup, 10 built-in UI themes.

標籤: `ai-agent` `deepseek` `deepseek-harness` `desktop` `desktop-app` `dsh` `dsh-plugins` `dshdesktop`

### 5. [Deepseek-Harness-EAC](https://github.com/zouyuxuan122/Deepseek-Harness-EAC)

⭐ 1,265 · JavaScript · 更新於 2026-08-24

DeepSeek Harness Desktop (dsh-desktop). EAC: Embracing All Creation (揽尽万象). Bundled Node.js runtime with full dsh-CLI kernel, one-click startup, 10 built-in UI themes.

標籤: `ai-agent` `deepseek` `deepseek-harness` `desktop` `desktop-app` `dsh` `dsh-plugins` `dshdesktop`

### 6. [DSH-Transparent-UI-Plugin](https://github.com/WYH66666666/DSH-Transparent-UI-Plugin)

⭐ 396 · JavaScript · 更新於 2026-08-31

是一层高自由度的玻璃质感主题，套在 DeepSeek Harness 网页端。顶栏、侧边栏、输入框、统计行、轨迹视图都成了磨砂玻璃片。玻璃模糊度、磨砂度、背景（流体或自定义壁纸，壁纸还能单独调模糊和磨砂）全都能在设置卡片里自由调节。关掉开关就回到原生界面，不改 DSH 任何一行源码。

標籤: `deepseek-harness` `deepseek-harness-plugin` `dsh` `dsh-plugin` `theme`

### 7. [dsh-liang-skin](https://github.com/kingOfSoySauce/dsh-liang-skin)

⭐ 152 · TypeScript · 更新於 2026-08-31

DeepSeek Harness 滑动变阻器皮肤

標籤: `dsh-plugin`

### 8. [dsh-dream-skin](https://github.com/RevolutionLA/dsh-dream-skin)

⭐ 133 · JavaScript · 更新於 2026-08-31

DeepSeek Harness 换肤 / 壁纸 / 主题包插件 (dsh-plugin) — 8 套 Mirage 主题、每用户强调色、壁纸2.0、主题包导入导出/分享链接、收藏与随机，纯原生 token 系统实现。

標籤: `deepseek-harness` `dsh` `dsh-plugin` `dsh-plugin-theme` `skin` `theme` `wallpaper`

---

<a id="other"></a>
## 其他專案

*尚未歸入其他分類的相關專案。*

### 1. [ollama](https://github.com/ollama/ollama)

⭐ 179,853 · Go · 更新於 2026-09-01

Get up and running with Kimi-K2.6, GLM-5.2, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.

標籤: `deepseek` `gemma` `gemma3` `glm` `go` `golang` `gpt-oss` `llama`

### 2. [DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3)

⭐ 104,433 · Python · 更新於 2026-09-01

尚無專案簡介。

### 3. [LlamaFactory](https://github.com/hiyouga/LlamaFactory)

⭐ 74,485 · Python · 更新於 2026-09-01

Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

標籤: `agent` `ai` `deepseek` `fine-tuning` `gemma` `gpt` `instruction-tuning` `large-language-models`

### 4. [openinterpreter](https://github.com/openinterpreter/openinterpreter)

⭐ 68,219 · Rust · 更新於 2026-09-01

A coding agent for open models like Kimi K3

標籤: `acp` `coding-agent` `deepseek` `kimi` `qwen` `rust`

### 5. [mindshub](https://github.com/mindsdb/mindshub)

⭐ 39,671 · Makefile · 更新於 2026-09-01

The unified workspace where open-source models get things done for you.

標籤: `agents` `ai` `anton` `artificial-inteligence` `claude` `claude-cowork` `codex` `cowork`

### 6. [ds4](https://github.com/antirez/ds4)

⭐ 21,965 · C · 更新於 2026-09-01

DeepSeek 4 Flash and PRO local inference engine for Metal, CUDA and ROCm

### 7. [Awesome-MCP-ZH](https://github.com/yzfly/Awesome-MCP-ZH)

⭐ 7,614 · N/A · 更新於 2026-09-01

MCP 资源精选， MCP指南，Claude MCP，MCP Servers, MCP Clients

標籤: `claude` `claude-mcp` `deepseek` `deepseek-mcp` `mcp` `mcp-clients` `mcp-host` `mcp-server`

### 8. [Awesome-AITools](https://github.com/ikaijua/Awesome-AITools)

⭐ 6,165 · Python · 更新於 2026-08-31

Collection of AI-related utilities. Welcome to submit pull requests /收藏AI相关的实用工具，欢迎提交pull requests

標籤: `agent-skills` `ai` `artificial-intelligence` `awesome` `awesome-list` `awesome-lists` `chatgpt` `claude`

### 9. [awesome-deepseek-agent](https://github.com/deepseek-ai/awesome-deepseek-agent)

⭐ 5,996 · N/A · 更新於 2026-08-24

尚無專案簡介。

### 10. [deepreasoning](https://github.com/winfunc/deepreasoning)

⭐ 5,361 · Rust · 更新於 2026-08-20

A high-performance LLM inference API and Chat UI that integrates DeepSeek R1's CoT reasoning traces with Anthropic Claude models.

標籤: `ai` `anthropic` `anthropic-claude` `api` `chain-of-thought` `claude` `deepseek` `deepseek-r1`

### 11. [Rapid-MLX](https://github.com/raullenchai/Rapid-MLX)

⭐ 3,626 · Python · 更新於 2026-09-01

The fastest local AI engine for Apple Silicon. 4.2x faster than Ollama, 0.08s cached TTFT, 100% tool calling. 17 tool parsers, prompt cache, reasoning separation, cloud routing. Drop-in OpenAI replacement. Works with Claude Code, Cursor, Aider.

標籤: `apple-silicon` `claude-code` `cursor` `deepseek` `fastapi` `hacktoberfest` `inference` `llm`

### 12. [codex-router](https://github.com/duolahypercho/codex-router)

⭐ 2,994 · JavaScript · 更新於 2026-09-01

External-model router for Codex with guided Kimi OAuth/API, DeepSeek, safe migration, and rollback.

標籤: `codex` `deepseek` `kimi` `litellm` `model-router`

### 13. [deepwiki-rs](https://github.com/sopaco/deepwiki-rs)

⭐ 1,708 · Rust · 更新於 2026-08-31

Turn code into clarity. Generate accurate technical docs and AI-ready context in minutes—perfectly structured for human teams and intelligent agents.

標籤: `claude` `deepseek` `deepwiki` `llm` `mistral` `openai` `openrouter` `rust`

### 14. [myDshPresets](https://github.com/0liveiraaa/myDshPresets)

⭐ 80 · JavaScript · 更新於 2026-08-19

用以解决DEEPSEEK思维链混乱,提高性能的插件

---

## 參與貢獻

請先閱讀 [CONTRIBUTING.md](CONTRIBUTING.md)，再透過 Issue 或 Pull Request 提交專案。專案須與 DeepSeek Harness 直接相關，並提供公開儲存庫。

## 授權條款

本專案採用 [Apache License 2.0](LICENSE) 發布。
