---
description: 自动生成专利申请技术交底书
---

# 专利申请技术交底书生成

你正在调用专利申请技术交底书自动化生成技能。本技能将帮助你完成从创新想法到完整交底书的整个过程。

## 执行步骤

请按以下步骤执行：

### 1. 收集用户输入

如果用户未提供以下信息，请询问：

- **创新想法 (idea)**: 请描述你的创新内容或技术改进思路
- **所属技术领域 (technical_field)**: 这项技术属于哪个领域？
- **关键词 (keywords)**: 可选，用于搜索相关技术的关键词

### 2. 按顺序调用子代理

使用 Task 工具按以下顺序调用各子代理：

```
1. title-generator        - 生成发明名称
2. field-analyzer         - 分析所属技术领域
3. background-researcher  - 调研背景技术（使用 web-search-prime, google-patents-mcp, exa, web-reader）
4. problem-analyzer       - 分析解决的技术问题
5. solution-designer      - 设计技术方案（使用 exa, web-search-prime）
6. benefit-analyzer       - 分析有益效果
7. implementation-writer  - 编写具体实施方式（使用 exa, web-search-prime）
8. protection-extractor   - 提炼保护点（使用 google-patents-mcp）
9. reference-collector    - 收集参考资料（使用 google-patents-mcp, web-search-prime, web-reader）
10. diagram-generator      - 生成附图说明
11. document-integrator   - 整合所有章节生成完整交底书
```

### 3. 输出结果

- 每个子代理生成一个独立的 Markdown 文件
- 最终生成完整的交底书文档：`专利申请技术交底书_[发明名称].md`

## MCP 工具说明

本技能依赖以下 MCP 服务：

| MCP 服务 | 用途 |
|---------|------|
| google-patents-mcp | 专利检索 |
| exa | 技术文档和代码搜索 |
| web-reader | 网页内容提取 |
| web-search-prime | 网络搜索 |

## 注意事项

- 必须使用 Task 工具调用子代理，不要自行完成子代理的工作
- 每个子代理完成后确认输出文件已生成
- 确保用户安装了所需的 MCP 服务
