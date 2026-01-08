# 专利交底书自动化生成技能

> 自动分析、搜索、调研并编写符合 IP-JL-027 标准的专利申请技术交底书

## 功能概述

本技能通过 11 个专业化子代理协作，自动完成专利交底书的全部撰写流程：

- 自动搜索和分析现有技术方案
- 识别现有方案的缺陷和改进点
- 调研相关专利和技术文献
- 生成符合 IP-JL-027 标准的完整交底书
- 双格式输出：Markdown + DOCX

## 使用示例

### 示例 1：基本使用

```
你：帮我写一份专利交底书

Claude：好的，我需要了解一些信息：
1. 你的创新想法是什么？
2. 所属技术领域是什么？
3. 有什么关键词可以帮助搜索吗？（可选）

你：
- 创新想法：一种基于深度学习的图像去雾方法，通过注意力机制增强去雾效果
- 技术领域：计算机视觉/图像处理
- 关键词：图像去雾、深度学习、注意力机制、卷积神经网络

Claude：开始生成专利交底书...

[自动执行 11 个子代理任务]

完成！交底书已生成：
- Markdown: output/专利申请技术交底书_一种基于深度学习的图像去雾方法.md
- DOCX: output/专利申请技术交底书_一种基于深度学习的图像去雾方法.docx
```

### 示例 2：硬件发明

```
你：我想为这个想法申请专利：一种可折叠的太阳能充电宝，内置无线充电功能

Claude：好的，我需要了解一些信息：
1. 所属技术领域是什么？

你：消费电子 / 移动电源 / 新能源

Claude：开始生成专利交底书...

[自动执行以下流程]
1. 生成发明名称：一种可折叠的太阳能充电宝
2. 分析技术领域：移动电源技术领域
3. 调研背景技术：搜索现有太阳能充电宝专利...
4. 分析技术问题：现有产品的局限性...
5. 设计技术方案：折叠结构 + 无线充电方案...
6. 分析有益效果：便携性提升、充电效率提升...
7. 编写具体实施方式：详细结构和工作原理...
8. 提炼保护点：折叠结构、无线充电集成方案...
9. 收集参考资料：相关专利文献...
10. 生成附图说明：结构图、电路图...
11. 整合文档：生成 Markdown 和 DOCX 格式

完成！
```

### 示例 3：软件/算法发明

```
你：帮我写专利交底书

Claude：我需要了解一些信息...

你：
- 创新想法：一种分布式数据库的一致性协议，通过拜占庭容错保证数据安全
- 技术领域：分布式系统 / 数据库
- 关键词：分布式数据库、一致性协议、拜占庭容错、共识算法

Claude：开始生成专利交底书...

[自动搜索相关技术文献和专利]
[分析现有一致性协议的缺陷]
[设计新的技术方案]
[生成完整交底书]

完成！
```

## MCP 依赖要求

本技能依赖以下 MCP 服务，**使用前必须完成配置**：

### 必需的 MCP 服务

| MCP 服务 | 用途 | 所需 API 密钥 | 安装方式 |
|---------|------|--------------|----------|
| web-search-prime | 网络搜索现有技术 | [智谱 API](https://open.bigmodel.cn/) | HTTP 配置 |
| web-reader | 提取网页内容 | [智谱 API](https://open.bigmodel.cn/) | HTTP 配置 |
| google-patents-mcp | 专利检索和对比 | [SerpAPI](https://serpapi.com/) | npx |
| exa | 技术文档搜索 | [Exa API](https://exa.ai/api-key) | npx |

### 配置步骤

在 `~/.claude/settings.json` 或项目根目录的 `.claude.json` 中添加：

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
      "args": [
        "/c",
        "npx",
        "-y",
        "@kunihiros/google-patents-mcp"
      ],
      "env": {
        "SERPAPI_API_KEY": "YOUR_SERPAPI_KEY"
      }
    },
    "exa": {
      "type": "stdio",
      "command": "cmd",
      "args": [
        "/c",
        "npx",
        "-y",
        "exa-mcp-server"
      ],
      "env": {
        "EXA_API_KEY": "YOUR_EXA_API_KEY"
      }
    }
  }
}
```

### Python 依赖

安装 DOCX 生成所需的 Python 库：

```bash
pip install python-docx
```

### API 密钥获取

| 服务 | 获取地址 | 费用说明 |
|------|----------|----------|
| 智谱 API | https://open.bigmodel.cn/ | 有免费额度 |
| SerpAPI | https://serpapi.com/ | 有免费额度 |
| Exa API | https://exa.ai/api-key | 有免费额度 |

## 配置验证

配置完成后，在 Claude Code 中验证 MCP 服务是否正常：

```bash
# 查看已加载的 MCP 服务
/mcp list
```

确保以下工具可用：
- `mcp__web-search-prime__webSearchPrime`
- `mcp__web_reader__webReader`
- `mcp__google-patents-mcp__search_patents`
- `mcp__exa__get_code_context_exa`

## 工作流程

```
用户输入创新想法
       ↓
1. title-generator (发明名称生成)
2. field-analyzer (技术领域分析)
3. background-researcher (背景技术调研) ← 使用 MCP
4. problem-analyzer (技术问题分析)
5. solution-designer (技术方案设计) ← 使用 MCP
6. benefit-analyzer (有益效果分析)
7. implementation-writer (实施方式编写) ← 使用 MCP
8. protection-extractor (保护点提炼) ← 使用 MCP
9. reference-collector (参考资料收集) ← 使用 MCP
10. diagram-generator (附图生成)
11. document-integrator (文档整合)
       ↓
   输出 Markdown + DOCX
```

## 子代理说明

| 子代理 | 功能 | 输出文件 | 使用的 MCP |
|--------|------|----------|------------|
| title-generator | 生成发明名称 | 01_发明名称.md | - |
| field-analyzer | 分析技术领域 | 02_所属技术领域.md | - |
| background-researcher | 调研背景技术 | 03_相关的背景技术.md | web-search-prime, google-patents-mcp, exa, web-reader |
| problem-analyzer | 分析技术问题 | 04_解决的技术问题.md | - |
| solution-designer | 设计技术方案 | 05_技术方案.md | exa, web-search-prime |
| benefit-analyzer | 分析有益效果 | 06_有益效果.md | - |
| implementation-writer | 编写实施方式 | 07_具体实施方式.md | exa, web-search-prime |
| protection-extractor | 提炼保护点 | 08_关键点和欲保护点.md | google-patents-mcp |
| reference-collector | 收集参考资料 | 09_其他有助于理解本技术的资料.md | google-patents-mcp, web-search-prime, web-reader |
| diagram-generator | 生成附图说明 | 10_附图说明.mermaid | - |
| document-integrator | 整合文档 | 专利申请技术交底书_*.md + .docx | - |

## 输出文件说明

### 中间文件

每个子代理生成独立的 Markdown 文件，便于：
- 分步骤审核和修改
- 保留中间结果
- 支持部分章节重新生成

位置：`output/chapters/` 目录

### 最终输出

- **Markdown 格式**：`output/专利申请技术交底书_[发明名称].md`
  - 优先输出，可直接阅读和编辑
  - 符合 IP-JL-027 模板格式

- **DOCX 格式**：`output/专利申请技术交底书_[发明名称].docx`
  - 基于 Word 模板生成
  - 可直接用于专利申请流程

## 常见问题

### Q1: MCP 服务连接失败怎么办？

**A:** 检查以下几点：
1. API 密钥是否正确配置
2. 网络连接是否正常
3. 运行 `/mcp list` 查看服务状态
4. 查看错误日志确认具体哪个服务失败

### Q2: 生成的交底书质量如何保证？

**A:** 本技能的优势：
- 自动搜索大量现有技术，确保全面性
- 11 个专业子代理分工协作，每个子代理专注一个章节
- 使用 MCP 服务获取最新技术资料和专利信息
- 生成的文档符合 IP-JL-027 标准格式

**建议**：生成后人工审核以下内容：
- 技术方案描述是否准确
- 有益效果是否充分
- 保护点是否提炼到位

### Q3: 支持哪些类型的专利？

**A:** 支持：
- 发明专利
- 实用新型专利
- 软件相关发明
- 硬件装置发明
- 方法/流程类发明

### Q4: 关键词有必要提供吗？

**A:** 关键词是可选的，但提供关键词可以：
- 提高背景技术调研的准确性
- 更好地识别相关专利
- 改进技术方案搜索结果

建议提供 3-5 个核心技术关键词。

### Q5: 生成的 DOCX 文件可以直接提交吗？

**A:** 生成的 DOCX 文件：
- 基于 IP-JL-027 标准模板
- 包含完整的章节结构
- 可以直接作为初稿使用

**建议**：提交前请：
1. 仔细审核技术描述的准确性
2. 补充具体的实验数据或测试结果
3. 由专利代理人进行专业审查

## 技术支持

- 问题反馈：[GitHub Issues](https://github.com/allanpk716/EasyJobSkills/issues)
- 项目主页：[EasyJob Skills Marketplace](https://github.com/allanpk716/EasyJobSkills)

## 许可证

MIT License
