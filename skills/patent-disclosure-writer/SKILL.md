---
name: patent-disclosure-writer
description: 自动生成专利申请技术交底书。当用户要求编写专利交底书、专利技术文档、专利申请书时使用此技能。自动搜索相关技术、分析现有方案、识别创新点，生成符合IP-JL-027标准的完整交底书，同时输出 Markdown 和 DOCX 格式。
---

# 专利申请技术交底书自动化生成技能

## 技能概述

本技能自动化分析、搜索、调研并编写《专利申请技术交底书》。用户只需提供基本的创新想法和思路，技能会自动搜索相关资料、分析现有技术、识别创新点，并生成完整的技术交底书。

**输出格式**：
- **优先输出**：Markdown 格式交底书（按 `out_templates/IP-JL-027(A／0)专利申请技术交底书模板.md` 模板格式）
- **随后生成**：DOCX 格式交底书（从 Markdown 提取内容填写到 `out_templates/发明、实用新型专利申请交底书 模板.docx`）

## 使用场景

当你有一个创新想法或技术改进思路时，使用此技能可以：
- 自动搜索和分析现有技术方案
- 识别现有方案的缺陷和改进点
- 调研相关专利和技术文献
- 生成符合 IP-JL-027 标准的专利申请技术交底书（Markdown + DOCX 双格式）

## 执行指令

当用户请求编写专利交底书时，必须按以下步骤执行：

### 1. 收集输入信息
询问用户的创新想法（idea）、所属技术领域（technical_field）和可选的关键词

### 2. 按顺序调用子代理（使用 Task 工具）

```
Task(tool="title-generator", prompt="用户创新想法：{idea}，技术领域：{technical_field}")
Task(tool="field-analyzer", prompt="技术领域：{technical_field}")
Task(tool="background-researcher", prompt="创新想法：{idea}，关键词：{keywords}")
Task(tool="problem-analyzer", prompt="创新想法：{idea}，背景技术：{背景技术内容}")
Task(tool="solution-designer", prompt="创新想法：{idea}")
Task(tool="benefit-analyzer", prompt="技术方案：{技术方案内容}")
Task(tool="implementation-writer", prompt="技术方案：{技术方案内容}")
Task(tool="protection-extractor", prompt="技术方案：{技术方案内容}")
Task(tool="reference-collector", prompt="技术领域：{technical_field}")
Task(tool="diagram-generator", prompt="技术方案：{技术方案内容}")
Task(tool="document-integrator", prompt="整合所有章节")
```

### 3. 输出文件管理
每个子代理完成后，确认输出文件已生成

### 4. 最终交付
向用户展示完整交底书路径和各章节文件（Markdown 和 DOCX）

**重要**：必须使用 Task 工具调用子代理，直接传递用户输入。不要尝试自己完成子代理的工作。

## 参数说明

| 参数 | 说明 | 必需 |
|------|------|------|
| idea | 创新想法的描述 | 是 |
| technical_field | 所属技术领域 | 是 |
| keywords | 关键词列表 | 否 |

## 工作流程

```
用户输入创新想法
       ↓
1. title-generator (发明名称生成)
   → 输出: 01_发明名称.md
       ↓
2. field-analyzer (技术领域分析)
   → 输出: 02_所属技术领域.md
       ↓
3. background-researcher (背景技术调研)
   → 使用: web-search-prime, google-patents-mcp, exa, web-reader
   → 输出: 03_相关的背景技术.md
       ↓
4. problem-analyzer (技术问题分析)
   → 输出: 04_解决的技术问题.md
       ↓
5. solution-designer (技术方案设计)
   → 使用: exa, web-search-prime
   → 输出: 05_技术方案.md
       ↓
6. benefit-analyzer (有益效果分析)
   → 输出: 06_有益效果.md
       ↓
7. implementation-writer (实施方式编写)
   → 使用: exa, web-search-prime
   → 输出: 07_具体实施方式.md
       ↓
8. protection-extractor (保护点提炼)
   → 使用: google-patents-mcp
   → 输出: 08_关键点和欲保护点.md
       ↓
9. reference-collector (参考资料收集)
   → 使用: google-patents-mcp, web-search-prime, web-reader
   → 输出: 09_其他有助于理解本技术的资料.md
       ↓
10. diagram-generator (附图生成)
    → 输出: 10_附图说明.mermaid
       ↓
11. document-integrator (文档整合)
    → 步骤1: 输出 Markdown 格式交底书
    → 步骤2: 生成 DOCX 格式交底书
       ↓
   输出完整交底书 (Markdown + DOCX)
```

## 子代理配置

技能使用 11 个专业化子代理完成各章节的撰写：

| 子代理 | 对应章节 | 主要MCP工具 | 输出文件 |
|--------|----------|-------------|----------|
| title-generator | 1.发明创造名称 | - | 01_发明名称.md |
| field-analyzer | 2.所属技术领域 | - | 02_所属技术领域.md |
| background-researcher | 3.相关的背景技术 | web-search-prime, google-patents-mcp, exa, web-reader | 03_相关的背景技术.md |
| problem-analyzer | 4.(1)解决的技术问题 | - | 04_解决的技术问题.md |
| solution-designer | 4.(2)技术方案 | exa, web-search-prime | 05_技术方案.md |
| benefit-analyzer | 4.(3)有益效果 | - | 06_有益效果.md |
| implementation-writer | 5.具体实施方式 | exa, web-search-prime | 07_具体实施方式.md |
| protection-extractor | 6.关键点和欲保护点 | google-patents-mcp | 08_关键点和欲保护点.md |
| reference-collector | 7.其他参考资料 | google-patents-mcp, web-search-prime, web-reader | 09_其他有助于理解本技术的资料.md |
| diagram-generator | 附图说明 | - | 10_附图说明.mermaid |
| document-integrator | 文档整合 | python-docx | 专利申请技术交底书_[发明名称].md + .docx |

## 交底书章节结构

生成的交底书符合 IP-JL-027 标准模板，包含以下章节：

1. **发明创造名称** - 发明的通用名称或核心技术描述
2. **所属技术领域** - 技术方案所属领域描述
3. **相关的背景技术** - 技术领域现状及存在的技术问题
4. **发明内容**
   - （1）解决的技术问题
   - （2）技术方案
   - （3）有益效果
5. **具体实施方式** - 具体实施方案和工作原理
6. **关键点和欲保护点** - 技术方案的关键创新点
7. **其他有助于理解本技术的资料** - 参考文献等

## 输出格式要求（重要）

### Markdown 格式（优先输出）

document-integrator 子代理必须严格按照以下格式输出交底书：

```markdown
# 发明/实用新型专利申请交底书

## **1. 发明创造名称**
[内容]

## **2. 所属技术领域**
[内容]

## **3. 相关的背景技术**
[内容]

## **4. 发明内容**

### **（1）解决的技术问题**
[内容]

### **（2）技术方案**
[内容]

### **（3）有益效果**
[内容]

## **5. 具体实施方式**
[内容]

## **6. 关键点和欲保护点**
[内容]

## **7. 其他有助于理解本技术的资料**
[内容]
```

**格式规范**：
- 章节编号：`## **1. **`、`## **2. **` 等（阿拉伯数字 + 粗体）
- 章节标题：`**发明创造名称**`（粗体）
- 子章节：`### **（1）**`、`### **（2）**` 等（中文括号 + 粗体）
- 不要添加模板中不存在的章节

### DOCX 格式（随后生成）

- 基于模板文件：`out_templates/发明、实用新型专利申请交底书 模板.docx`
- 从 Markdown 文件中提取各章节内容
- 使用 Python `python-docx` 库填写模板
- 输出到 `output/` 文件夹

## MCP 工具依赖（必须配置）

本技能依赖以下 MCP 服务，使用前**必须**完成配置：

### 必需的 MCP 服务

| MCP 服务 | 用途 | 使用的子代理 | 配置方式 |
|---------|------|--------------|----------|
| web-search-prime | 网络搜索 | background-researcher, solution-designer, implementation-writer, reference-collector | 智谱 API（HTTP） |
| web-reader | 网页内容提取 | background-researcher, reference-collector | 智谱 API（HTTP） |
| google-patents-mcp | 专利检索 | background-researcher, protection-extractor, reference-collector | npx + SerpAPI |
| exa | 技术文档搜索 | background-researcher, solution-designer, implementation-writer | npx + Exa API |

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

### API 密钥获取

| 服务 | 获取地址 |
|------|----------|
| 智谱 API（web-search-prime/web-reader） | https://open.bigmodel.cn/ |
| SerpAPI（google-patents-mcp） | https://serpapi.com/ |
| Exa API（exa） | https://exa.ai/api-key |

### 配置验证

配置完成后，在 Claude Code 中运行以下命令验证 MCP 服务是否正常：

```bash
# 查看已加载的 MCP 服务
/mcp list
```

确保以下工具可用：
- `mcp__web-search-prime__webSearchPrime`
- `mcp__web_reader__webReader`
- `mcp__google-patents-mcp__search_patents`
- `mcp__exa__get_code_context_exa`

### MCP 工具使用映射

| MCP服务 | 工具名称 | 主要用途 | 使用的子代理 |
|---------|----------|----------|--------------|
| web-search-prime | webSearchPrime | 网络搜索 | background-researcher, solution-designer, implementation-writer, reference-collector |
| web-reader | webReader | 网页内容提取 | background-researcher, reference-collector |
| google-patents-mcp | search_patents | 专利检索 | background-researcher, protection-extractor, reference-collector |
| exa | get_code_context_exa | 技术文档和代码搜索 | background-researcher, solution-designer, implementation-writer |
| zai-mcp-server | - | 图像和文档分析 | 可选 |

## Python 依赖要求

document-integrator 子代理需要以下 Python 库：
```bash
pip install python-docx
```

## 子代理执行顺序

子代理按照以下顺序串行执行（某些可以并行）：

**第一阶段：基础信息生成**
1. title-generator
2. field-analyzer

**第二阶段：背景调研**
3. background-researcher（并行：reference-collector）

**第三阶段：发明内容撰写**
4. problem-analyzer
5. solution-designer
6. benefit-analyzer

**第四阶段：实施与保护**
7. implementation-writer
8. protection-extractor

**第五阶段：补充材料**
9. diagram-generator
10. reference-collector（可提前进行）

**第六阶段：文档整合**
11. document-integrator
    - 步骤1：生成 Markdown 格式
    - 步骤2：生成 DOCX 格式

## 输出文件说明

每个子代理生成独立的输出文件，便于：
- 分步骤审核和修改
- 保留中间结果
- 支持部分章节重新生成
- 便于调试和优化

最终 document-integrator 汇总所有文件生成完整交底书：
- Markdown 格式：`专利申请技术交底书_[发明名称].md`
- DOCX 格式：`output/专利申请技术交底书_[发明名称].docx`

## 模板文件位置

- Markdown 模板：`out_templates/IP-JL-027(A／0)专利申请技术交底书模板.md`
- DOCX 模板：`out_templates/发明、实用新型专利申请交底书 模板.docx`
