# EasyJob Skills Marketplace

> 专注于提升工作效率的 Claude Code 技能集合

## 简介

EasyJob Skills Marketplace 是一个致力于提升工作效率的 Claude Code 技能市场。通过本市场，你可以轻松安装和更新各类实用技能，帮助自动化完成日常工作任务。

## 目录结构

```
EasyJobSkills/
├── .claude-plugin/
│   └── marketplace.json         # Marketplace 清单文件
├── .claude/
│   └── agents/                  # 子代理配置（共享）
│       ├── 01-title-generator.md
│       ├── 02-field-analyzer.md
│       └── ...
├── commands/                    # 斜杠命令（可选）
│   └── patent.md
├── skills/                      # 技能目录
│   └── patent-disclosure-writer/
│       ├── SKILL.md            # 技能定义文件
│       ├── LICENSE.txt         # 技能许可证
│       └── templates/          # 技能专属资源
│           ├── IP-JL-027(A／0)专利申请技术交底书模板.md
│           └── 发明、实用新型专利申请交底书 模板.docx
└── README.md
```

## 设计说明

### 资源文件放置规则

遵循 [official anthropics/skills](https://github.com/anthropics/skills) 的最佳实践：

1. **skill 专属资源**：放在 `skills/<skill-name>/` 目录下
   - 例如：`skills/patent-disclosure-writer/templates/`
   - 每个技能可以有独立的 `templates/`、资源文件等

2. **共享资源**：放在 marketplace 根目录
   - 例如：`.claude/agents/`、`commands/`

3. **每个 skill 可以有自己的 LICENSE.txt**

### 添加新技能

按照官方结构，新技能应该：

```
skills/
└── your-new-skill/
    ├── SKILL.md              # 技能定义（必需）
    ├── LICENSE.txt           # 许可证（推荐）
    └── templates/            # 技能专属资源（可选）
        └── your-template.md
```

## 已收录技能

### 专利交底书生成器 (patent-disclosure-writer)

自动化生成符合 IP-JL-027 标准的专利申请技术交底书，支持发明专利和实用新型专利。

**功能特性**：
- 自动搜索和分析现有技术方案
- 识别现有方案的缺陷和改进点
- 调研相关专利和技术文献
- 自动创新度评估，建议专利类型
- 智能检测已有章节，支持断点续传
- 附图自动生成和编号管理
- 支持 Markdown + DOCX 双格式输出

**斜杠命令**：
| 命令 | 功能 |
|------|------|
| `/patent` | 智能生成交底书（支持断点续传、选择性重新生成） |
| `/patent-update-diagrams` | 智能补充附图 |
| `/patent-md-2-docx` | Markdown 转 DOCX |

**技能资源**：
- 模板文件：`skills/patent-disclosure-writer/templates/`
- 子代理：`.claude/agents/`（共享）
- 文档：
  - [用户文档](skills/patent-disclosure-writer/README.md)
  - [配置指南](skills/patent-disclosure-writer/CONFIG.md)
  - [子代理详解](skills/patent-disclosure-writer/AGENTS.md)
  - [故障排查](skills/patent-disclosure-writer/TROUBLESHOOTING.md)

## 安装 Marketplace

### 通过 GitHub 安装

```bash
claude plugin marketplace add allanpk716/EasyJobSkills
```

### 通过本地路径安装

```bash
cd /path/to/EasyJobSkills
claude plugin marketplace add .
```

### 通过远程 URL 安装

```bash
claude plugin marketplace add https://github.com/allanpk716/EasyJobSkills.git
```

## 安装技能

添加 marketplace 后，可以安装其中的技能：

```bash
claude plugin install patent-disclosure-writer@easy-job-skills
```

## 管理技能

| 操作 | 命令 |
|------|------|
| 查看已安装技能 | `claude plugin list` |
| 更新 marketplace | `claude plugin marketplace update easy-job-skills` |
| 更新特定技能 | `claude plugin update patent-disclosure-writer@easy-job-skills` |
| 卸载技能 | `claude plugin uninstall patent-disclosure-writer@easy-job-skills` |

## MCP 依赖

某些技能依赖 MCP 服务。安装技能前，请确保已配置所需的 API 密钥和服务。

### 专利交底书生成器所需 MCP 服务

| MCP 服务 | 用途 | 所需 API 密钥 |
|---------|------|--------------|
| web-search-prime | 网络搜索 | [智谱 API](https://open.bigmodel.cn/) |
| web-reader | 网页内容提取 | [智谱 API](https://open.bigmodel.cn/) |
| google-patents-mcp | 专利检索 | [SerpAPI](https://serpapi.com/) |
| exa | 技术文档搜索 | [Exa API](https://exa.ai/api-key) |

### 配置步骤

在 `~/.claude/settings.json` 或 `.claude.json` 中添加以下 MCP 服务配置：

```json
{
  "mcpServers": {
    "web-search-prime": {
      "type": "http",
      "url": "https://open.bigmodel.cn/api/mcp/web_search_prime/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_ZHIPU_API_KEY"
      }
    },
    "web-reader": {
      "type": "http",
      "url": "https://open.bigmodel.cn/api/mcp/web_reader/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_ZHIPU_API_KEY"
      }
    },
    "google-patents-mcp": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "@kunihiros/google-patents-mcp"],
      "env": {
        "SERPAPI_API_KEY": "YOUR_SERPAPI_KEY"
      }
    },
    "exa": {
      "type": "stdio",
      "command": "cmd",
      "args": ["/c", "npx", "-y", "exa-mcp-server"],
      "env": {
        "EXA_API_KEY": "YOUR_EXA_API_KEY"
      }
    }
  }
}
```

### Python 依赖

```bash
pip install python-docx
```

### 验证配置

配置完成后，运行以下命令验证 MCP 服务是否正常：

```bash
# 查看已加载的 MCP 服务
/mcp list
```

## 贡献新技能

欢迎贡献！请遵循官方目录结构：

1. 在 `skills/` 下创建技能目录
2. 创建 `SKILL.md` 定义技能行为
3. 添加技能专属资源到技能目录下
4. 添加 `LICENSE.txt`
5. 更新 `.claude-plugin/marketplace.json`

```json
{
  "plugins": [
    {
      "name": "easy-job-skills",
      "description": "...",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/patent-disclosure-writer",
        "./skills/your-new-skill"  // 添加新技能
      ]
    }
  ]
}
```

## 许可证

MIT License

## 联系方式

- [GitHub Issues](https://github.com/allanpk716/EasyJobSkills/issues)
