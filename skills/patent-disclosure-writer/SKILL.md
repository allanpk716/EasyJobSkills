---
name: patent-disclosure-writer
description: 自动生成专利申请技术交底书，符合IP-JL-027标准。支持发明专利和实用新型专利，可转换为DOCX格式。
---

# 专利交底书自动生成

## 技能概述

本技能自动化分析、搜索、调研并编写《专利申请技术交底书》。用户只需提供基本的创新想法和思路，技能会自动搜索相关资料、分析现有技术、识别创新点，并生成完整的技术交底书。

**输出格式**：
- **Markdown 格式交底书**（按模板格式）
- **附图说明**：包含 Mermaid 代码块
- **DOCX 格式**：使用 `/patent-md-2-docx` 命令转换

## 快速开始

### 1. 确保已配置 MCP 服务

本技能依赖以下 MCP 服务（必须先配置）：
- web-search-prime（网络搜索）
- web-reader（网页内容提取）
- google-patents-mcp（专利检索）
- exa（技术文档搜索）

**配置方法**：见 [CONFIG.md](CONFIG.md)

### 2. 运行生成命令

```bash
/patent
```

按提示输入：
- **创新想法**（idea）：创新想法的描述
- **所属技术领域**（technical_field）：所属技术领域
- **关键词**（keywords）：可选的关键词列表
- **专利类型**（patent_type）：发明专利/实用新型专利（默认发明专利）
- **输出目录**（output_dir）：交底书输出目录（默认 `output/`）

### 3. 等待生成完成

技能将自动调用多个子代理完成各章节撰写，最终生成：
- 完整的 Markdown 格式交底书
- 各章节独立文件（便于审核和修改）
- 附图（Mermaid 代码块形式）

### 4. 转换为 DOCX（可选）

```bash
/patent-md-2-docx
```

## 使用场景

- 编写发明专利申请交底书
- 编写实用新型专利申请交底书
- 从创新想法到完整交底书的全流程自动化

## 斜杠命令

| 命令 | 功能 | 说明 |
|------|------|------|
| `/patent` | 智能生成交底书 | 支持断点续传、选择性重新生成 |
| `/patent-update-diagrams` | 智能补充附图 | 扫描章节并补充缺失的附图 |
| `/patent-md-2-docx` | Markdown 转 DOCX | 将 Markdown 交底书转换为正式格式 |

## 执行流程概览

```
用户输入创新想法
       ↓
1. title-generator (发明名称)
2. field-analyzer (技术领域)
3. background-researcher (背景技术调研 + 创新度评估)
4. problem-analyzer (技术问题)
5. solution-designer (技术方案)
6. benefit-analyzer (有益效果)
7. implementation-writer (实施方式)
8. protection-extractor (保护点)
9. reference-collector (参考资料)
10. document-integrator (文档整合)
       ↓
输出: 专利申请技术交底书_[发明名称].md
```

## 子代理列表

| 子代理 | 对应章节 | 输出文件 |
|--------|----------|----------|
| title-generator | 1.发明创造名称 | 01_发明名称.md |
| field-analyzer | 2.所属技术领域 | 02_所属技术领域.md |
| background-researcher | 3.相关的背景技术 | 03_相关的背景技术.md |
| problem-analyzer | 4.(1)解决的技术问题 | 04_解决的技术问题.md |
| solution-designer | 4.(2)技术方案 | 05_技术方案.md |
| benefit-analyzer | 4.(3)有益效果 | 06_有益效果.md |
| implementation-writer | 5.具体实施方式 | 07_具体实施方式.md |
| protection-extractor | 6.关键点和欲保护点 | 08_关键点和欲保护点.md |
| reference-collector | 7.其他参考资料 | 09_其他有助于理解本技术的资料.md |
| document-integrator | 文档整合 | 专利申请技术交底书_[发明名称].md |

**详细信息**：见 [AGENTS.md](AGENTS.md)

## 专利类型说明

| 类型 | 创新要求 | 审查周期 | 保护期限 |
|------|---------|---------|----------|
| **发明专利** | 突出的实质性特点和显著的进步 | 2-3年 | 20年 |
| **实用新型专利** | 实质性特点和进步 | 6-12个月 | 10年 |

**创新度评估**：background-researcher 会自动评估创新程度，如果建议降级到实用新型专利，会询问你是否接受。

## MCP 工具依赖

本技能依赖以下 MCP 服务：

| MCP 服务 | 用途 | 使用的子代理 |
|---------|------|--------------|
| web-search-prime | 网络搜索 | background-researcher, solution-designer, implementation-writer, reference-collector |
| web-reader | 网页内容提取 | background-researcher, reference-collector |
| google-patents-mcp | 专利检索 | background-researcher, protection-extractor, reference-collector |
| exa | 技术文档搜索 | background-researcher, solution-designer, implementation-writer |

**配置方法**：见 [CONFIG.md](CONFIG.md)

## 详细文档

- [完整配置指南](CONFIG.md) - MCP 服务配置详细步骤
- [子代理详解](AGENTS.md) - 每个子代理的详细说明
- [故障排查指南](TROUBLESHOOTING.md) - 常见问题和解决方案

## 输出文件说明

每个子代理生成独立的输出文件，便于：
- 分步骤审核和修改
- 保留中间结果
- 支持部分章节重新生成

最终 document-integrator 汇总所有文件生成完整交底书：
- Markdown 格式：`专利申请技术交底书_[发明名称].md`

**转换为 DOCX**：使用 `/patent-md-2-docx` 命令。

## 模板文件位置

- Markdown 模板：`skills/patent-disclosure-writer/templates/IP-JL-027(A／0)专利申请技术交底书模板.md`
- DOCX 模板：`skills/patent-disclosure-writer/templates/发明、实用新型专利申请交底书 模板.docx`
