# 参与贡献

感谢你帮助完善 DeepSeek Harness 项目列表。

## 提交一个项目

请提交一个公开的 GitHub 仓库，并确认它与 DeepSeek Harness 直接相关，例如插件、客户端、主题、集成或生态工具。Pull Request 中请说明项目用途、所属分类，并提供简短中文介绍。

项目数据由 `data/projects.json` 保存。修改数据后运行：

```bash
python scripts/generate_markdown.py
```

采集 GitHub 新项目或更新 Star、语言、更新时间等信息：

```bash
GITHUB_TOKEN=你的_token python scripts/collect_projects.py
```

不想访问 GitHub 时，可使用 `python scripts/collect_projects.py --offline` 检查本地数据流程。
