# EasyJob Skills - 开发指南

> 专注于提升工作效率的 Claude Code 技能集合开发文档

## 项目定位

EasyJob Skills Marketplace 是一个致力于提升工作效率的 Claude Code 插件市场。通过本市场，用户可以轻松安装和更新各类实用技能，帮助自动化完成日常工作任务。

## 开发前必读：官方文档资源

在开发任何新功能之前，**务必先阅读官方文档**以获取最新、最准确的信息。这样可以避免绕弯路，确保开发方向正确。

### 官方文档链接

| 主题 | 官方文档 | 阅读时机 |
|------|----------|----------|
| **Skills（技能）** | https://code.claude.com/docs/en/skills | 开发新技能前必读 |
| **Subagents（子代理）** | https://code.claude.com/docs/en/sub-agents | 配置子代理前必读 |
| **Plugins（插件）** | https://code.claude.com/docs/en/plugins | 理解插件架构 |
| **Slash Commands（斜杠命令）** | https://code.claude.com/docs/en/slash-commands | 创建命令前必读 |
| **Hooks（钩子）** | https://code.claude.com/docs/en/hooks-guide | 需要自动化流程时 |
| **Output Styles（输出样式）** | https://code.claude.com/docs/en/output-styles | 自定义输出行为 |
| **Headless/Agent SDK** | https://code.claude.com/docs/en/headless | 程序化调用 |
| **Troubleshooting** | https://code.claude.com/docs/en/troubleshooting | 遇到问题时 |

### 开发工作流程

```
1. 确定开发目标（Skill/Subagent/Command/Hook）
       ↓
2. 阅读对应的官方文档
       ↓
3. 理解最佳实践和规范
       ↓
4. 按照项目结构进行开发
       ↓
5. 本地测试验证
       ↓
6. 更新 marketplace.json
       ↓
7. 提交代码
```

---

## 项目结构规范

```
EasyJobSkills/
├── .claude-plugin/
│   └── marketplace.json         # Marketplace 清单文件（必需）
├── .claude/
│   └── agents/                  # 子代理配置（共享）
│       ├── 01-title-generator.md
│       ├── 02-field-analyzer.md
│       └── ...
├── commands/                    # 斜杠命令（可选）
│   └── patent.md
├── skills/                      # 技能目录（核心）
│   └── patent-disclosure-writer/
│       ├── SKILL.md            # 技能定义文件（必需）
│       ├── LICENSE.txt         # 技能许可证（推荐）
│       └── templates/          # 技能专属资源
│           └── ...
├── CLAUDE.md                    # 本文件 - 开发指南
└── README.md                    # 用户文档
```

---

## 一、Skills（技能）开发指南

### 1.1 Skill 文件结构

每个 Skill 必须包含一个 `SKILL.md` 文件，位于独立的技能目录下：

```
skills/
└── your-skill-name/
    ├── SKILL.md              # 技能定义（必需）
    ├── LICENSE.txt           # 许可证（推荐）
    └── [resources]/          # 技能专属资源（可选）
        ├── templates/
        ├── scripts/
        └── ...
```

### 1.2 SKILL.md 文件格式

`SKILL.md` 必须包含 YAML frontmatter 和 Markdown 指令：

```markdown
---
name: your-skill-name
description: 简洁描述技能功能和触发时机（max 1024字符）
allowed-tools: Tool1, Tool2  # 可选 - 限制工具访问
model: sonnet                # 可选 - 指定模型
---

# 技能名称

## 技能概述
[技能功能的简要说明]

## 使用场景
[描述何时使用此技能]

## 执行指令
[详细的执行步骤说明]
```

### 1.3 Frontmatter 字段说明

| 字段 | 必需 | 说明 |
|------|------|------|
| `name` | 是 | 技能名称，小写字母、数字、连字符，最多64字符 |
| `description` | 是 | 技能描述，Claude 用它决定何时触发，最多1024字符 |
| `allowed-tools` | 否 | 允许使用的工具列表（逗号分隔） |
| `model` | 否 | 使用的模型（sonnet/opus/haiku/inherit） |

### 1.4 编写优秀 Description 的技巧

根据官方文档，`description` 是 Claude 决定是否使用技能的关键：

**好的 description 示例：**
```
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
```

**不好的 description 示例：**
```
description: Helps with documents  # 太模糊，无法触发
```

### 1.5 渐进式披露（Progressive Disclosure）

为避免占用过多上下文，应该：
- 在 `SKILL.md` 中放核心指令和快速参考
- 详细文档放在单独文件中（如 REFERENCE.md）
- 通过链接引用详细资源

**示例：**
```markdown
## 快速开始
[核心步骤]

## 详细文档
- 完整 API 参考：见 [REFERENCE.md](REFERENCE.md)
- 使用示例：见 [EXAMPLES.md](EXAMPLES.md)
```

### 1.6 技能资源组织

按照官方最佳实践：

| 资源类型 | 位置 | 说明 |
|----------|------|------|
| 技能专属模板 | `skills/<skill-name>/templates/` | 仅该技能使用 |
| 共享子代理 | `.claude/agents/` | 多个技能共享 |
| 共享脚本 | `.claude/scripts/` | 通用工具脚本 |

### 1.7 技能开发检查清单

开发新技能前，确认：
- [ ] 已阅读官方 Skills 文档
- [ ] 确定技能触发场景
- [ ] 编写清晰的 description
- [ ] 创建技能目录结构
- [ ] 编写 SKILL.md
- [ ] 添加必要资源文件
- [ ] 添加 LICENSE.txt
- [ ] 更新 marketplace.json
- [ ] 本地测试

---

## 二、Subagents（子代理）开发指南

### 2.1 子代理文件结构

```
.claude/agents/
└── agent-name.md
```

### 2.2 子代理配置格式

```markdown
---
name: agent-name
description: 子代理的功能描述和触发时机
tools: Read, Edit, Bash  # 可选 - 继承所有工具若省略
model: sonnet            # 可选 - 默认 sonnet
permissionMode: default  # 可选
skills: skill1, skill2   # 可选 - 预加载的技能
---

# 子代理系统提示

你是一个专门的子代理，负责...
```

### 2.3 子代理配置字段

| 字段 | 必需 | 说明 |
|------|------|------|
| `name` | 是 | 唯一标识符，小写字母和连字符 |
| `description` | 是 | 自然语言描述，Claude 用它决定是否调用 |
| `tools` | 否 | 工具列表，省略则继承全部 |
| `model` | 否 | 模型选择（sonnet/opus/haiku/inherit） |
| `permissionMode` | 否 | 权限模式 |
| `skills` | 否 | 预加载的技能列表（逗号分隔） |

### 2.4 子代理最佳实践

根据官方文档：
- **专注单一职责**：不要让一个子代理做所有事情
- **详细的系统提示**：包含具体指令、示例和约束
- **限制工具访问**：只授予必要的工具
- **版本控制**：将项目级子代理纳入版本控制

### 2.5 子代理命名规范

为了便于管理，使用数字前缀排序：
```
01-title-generator.md
02-field-analyzer.md
03-background-researcher.md
...
```

---

## 三、Slash Commands（斜杠命令）开发指南

### 3.1 命令文件结构

```
commands/
└── command-name.md
```

### 3.2 命令配置格式

```markdown
---
description: 命令的简短描述
arguments:
  - name: arg1
    description: 参数说明
    required: true
  - name: arg2
    description: 可选参数
    required: false
---

# 命令标题

命令的具体执行指令...
```

### 3.3 命令触发方式

- **Standalone（独立）**：`/command-name`
- **Plugin（插件）**：`/plugin-name:command-name`

本项目作为插件市场，命令会自动命名空间化。

---

## 四、Hooks（钩子）开发指南

### 4.1 钩子事件类型

| 事件 | 说明 | 是否可阻塞 |
|------|------|------------|
| `PreToolUse` | 工具调用前 | 是 |
| `PermissionRequest` | 权限请求时 | 是 |
| `PostToolUse` | 工具调用后 | 否 |
| `UserPromptSubmit` | 用户提交提示时 | 否 |
| `Notification` | 发送通知时 | 否 |
| `SessionStart` | 会话开始 | 否 |
| `SessionEnd` | 会话结束 | 否 |

### 4.2 钩子配置位置

插件中的钩子放在：
```
my-plugin/
└── hooks/
    └── hooks.json
```

### 4.3 钩子配置示例

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/formatter.py"
          }
        ]
      }
    ]
  }
}
```

---

## 五、插件开发完整流程

### 5.1 开发新技能的步骤

```bash
# 1. 创建技能目录
mkdir skills/your-new-skill

# 2. 创建 SKILL.md
cat > skills/your-new-skill/SKILL.md << 'EOF'
---
name: your-new-skill
description: 具体描述技能功能和触发时机
---

# 技能名称

## 技能概述
...

## 使用场景
...

## 执行指令
...
EOF

# 3. 添加许可证（可选）
cp LICENSE skills/your-new-skill/LICENSE.txt

# 4. 更新 marketplace.json
# 添加 "./skills/your-new-skill" 到 skills 数组

# 5. 本地测试
claude --plugin-dir ./

# 6. 测试技能功能
# 在 Claude Code 中测试技能是否正确触发

# 7. 提交代码
git add skills/your-new-skill .claude-plugin/marketplace.json
git commit -m "Add new skill: your-new-skill"
```

### 5.2 更新 marketplace.json

```json
{
  "name": "easy-job-skills",
  "displayName": "EasyJob Skills Marketplace",
  "owner": {
    "name": "allanpk716",
    "email": "allanpk716@gmail.com"
  },
  "metadata": {
    "description": "专注于提升工作效率的 Claude Code 技能集合",
    "version": "1.0.0",
    "homepage": "https://github.com/allanpk716/EasyJobSkills"
  },
  "plugins": [
    {
      "name": "easy-job-skills",
      "description": "提升工作效率的技能集合",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/patent-disclosure-writer",
        "./skills/your-new-skill"
      ]
    }
  ]
}
```

---

## 六、本地测试指南

### 6.1 使用 --plugin-dir 测试

```bash
# 在项目根目录运行
claude --plugin-dir ./
```

这会加载当前目录作为插件进行测试。

### 6.2 测试清单

- [ ] 插件正确加载
- [ ] Skills 出现在 `/agents` 中
- [ ] Skills 能够正确触发
- [ ] 子代理配置正确
- [ ] MCP 工具可访问
- [ ] 输出文件符合预期

---

## 七、MCP 服务集成

### 7.1 常用 MCP 服务

| MCP 服务 | 安装命令 | 用途 |
|----------|----------|------|
| google-patents-mcp | `npm install -g @modelcontextprotocol/server-google-patents` | 专利检索 |
| exa | `npm install -g @modelcontextprotocol/server-exa` | 技术文档搜索 |
| web-reader | `npm install -g @modelcontextprotocol/server-web-reader` | 网页内容提取 |
| web-search-prime | `npm install -g @modelcontextprotocol/server-web-search-prime` | 网络搜索 |

### 7.2 在 Skill 中声明 MCP 依赖

在 SKILL.md 中添加 MCP 依赖说明：

```markdown
## MCP 工具依赖

本技能依赖以下 MCP 服务：

| MCP 服务 | 用途 | 安装命令 |
|---------|------|----------|
| google-patents-mcp | 专利检索 | npm install -g @modelcontextprotocol/server-google-patents |
| exa | 技术文档搜索 | npm install -g @modelcontextprotocol/server-exa |
```

### 7.3 配置 MCP 服务

在 `~/.claude/settings.json` 或项目 `.mcp.json` 中配置：

```json
{
  "mcpServers": {
    "google-patents": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-google-patents"]
    }
  }
}
```

---

## 八、常见问题排查

### 8.1 Skill 未触发

**可能原因：**
1. description 不够具体 → 添加更多触发关键词
2. YAML frontmatter 格式错误 → 检查 `---` 分隔符
3. 文件路径不正确 → 确认在正确的目录

### 8.2 子代理未加载

**可能原因：**
1. 文件不在 `.claude/agents/` 目录
2. 文件名不是 `.md` 格式
3. frontmatter 格式错误

**解决方法：**
运行 `claude --debug` 查看加载错误

### 8.3 MCP 工具不可用

**可能原因：**
1. MCP 服务未安装
2. MCP 服务未配置
3. MCP 服务未启动

**解决方法：**
```bash
# 检查已安装的 MCP 服务
npm list -g | grep @modelcontextprotocol

# 检查配置
cat ~/.claude/settings.json | grep -A 10 mcpServers
```

---

## 九、最佳实践总结

### 9.1 Skills 开发

- ✅ description 要具体，包含触发关键词
- ✅ 使用渐进式披露减少上下文占用
- ✅ 技能资源放在技能目录下
- ✅ 共享资源放在根目录 `.claude/` 下

### 9.2 Subagents 开发

- ✅ 专注单一职责
- ✅ 详细的系统提示
- ✅ 只授予必要的工具
- ✅ 使用数字前缀便于管理

### 9.3 插件结构

- ✅ 遵循官方目录结构
- ✅ 及时更新 marketplace.json
- ✅ 本地测试后再提交
- ✅ 添加适当的许可证

---

## 十、官方文档阅读策略

### 10.1 首次开发

如果是第一次开发某种类型的组件（Skill/Subagent/Command），**必须**完整阅读对应的官方文档。

### 10.2 后续开发

后续开发时，可以：
1. 先参考项目内现有的实现
2. 遇到不确定的问题时查阅官方文档
3. 定期查看官方文档更新（API 可能变化）

### 10.3 快速参考

| 需求 | 文档位置 |
|------|----------|
| Skill 不触发 | https://code.claude.com/docs/en/skills#skill-not-triggering |
| 子代理配置 | https://code.claude.com/docs/en/sub-agents#subagent-configuration |
| 插件结构 | https://code.claude.com/docs/en/plugins#plugin-structure-overview |
| 钩子事件 | https://code.claude.com/docs/en/hooks-guide#hook-events-overview |

### 10.4 文档访问失败处理

**重要规则**：如果按照本文档提供的官方文档链接访问失败，必须立即停止开发流程，并请求人工介入。

**执行步骤**：
1. **停止当前任务**：不要继续凭经验或旧文档开发
2. **报告问题**：明确告知用户哪个文档链接无法访问
3. **请求更新**：请用户提供最新的官方文档地址
4. **更新文档**：获得新地址后，更新 CLAUDE.md 中的链接
5. **重新阅读**：使用新的链接重新阅读官方文档
6. **继续开发**：确认信息准确后再继续开发

**示例提示**：
```
⚠️ 官方文档访问失败

尝试访问以下文档时出错：
- https://code.claude.com/docs/en/skills

请提供该文档的最新地址，以便我更新 CLAUDE.md 并确保开发基于准确的信息。
```

**为什么这条规则重要**：
- 官方文档 URL 可能随时间变化
- 基于过时信息开发可能导致功能不兼容
- API 和最佳实践可能已更新
- 确保项目始终符合最新规范

---

## 十一、贡献指南

### 11.1 提交新技能

1. Fork 项目
2. 创建特性分支
3. 按照本指南开发新技能
4. 确保通过本地测试
5. 提交 Pull Request

### 11.2 代码审查要点

- [ ] 遵循官方最佳实践
- [ ] 目录结构正确
- [ ] SKILL.md 格式规范
- [ ] description 清晰具体
- [ ] 更新了 marketplace.json
- [ ] 添加了适当的文档

---

## 十二、更新日志

### 版本 1.0.0
- 初始发布
- 包含专利交底书生成技能

---

## 附录：官方文档速查

### Skills 关键概念

- **Model-invoked**：Claude 自动决定何时使用
- **Progressive disclosure**：渐进式披露，核心信息优先
- **Skill locations**：
  - Enterprise: managed settings
  - Personal: `~/.claude/skills/`
  - Project: `.claude/skills/`
  - Plugin: `skills/` in plugin directory

### Subagents 关键概念

- **Separate context**：独立上下文窗口
- **Tool restrictions**：可限制工具访问
- **Auto-delegation**：Claude 自动委托任务
- **Resume capability**：可恢复之前的对话

### Skills vs 其他扩展

| 特性 | Skills | Slash Commands | CLAUDE.md | Subagents |
|------|--------|----------------|-----------|-----------|
| 触发方式 | 自动 | 手动输入 | 加载到每次对话 | 委托或手动 |
| 上下文 | 当前对话 | 当前对话 | 当前对话 | 独立上下文 |
| 工具限制 | 支持 | 不支持 | 不支持 | 支持 |
| 适用场景 | 知识传递 | 可复用提示 | 项目约定 | 隔离任务 |

---

**重要提醒**：本文档基于官方文档编写，但官方文档可能会更新。遇到不确定的情况时，请务必查阅最新的官方文档。
