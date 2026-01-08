# 子代理详解

本文档详细说明专利交底书技能使用的每个子代理的职责、输入输出格式和使用的 MCP 工具。

## 子代理列表

| 序号 | 子代理名称 | 对应章节 | 主要 MCP 工具 |
|------|-----------|----------|--------------|
| 1 | title-generator | 1.发明创造名称 | - |
| 2 | field-analyzer | 2.所属技术领域 | - |
| 3 | background-researcher | 3.相关的背景技术 | web-search-prime, google-patents-mcp, exa, web-reader |
| 4 | problem-analyzer | 4.(1)解决的技术问题 | - |
| 5 | solution-designer | 4.(2)技术方案 | exa, web-search-prime |
| 6 | benefit-analyzer | 4.(3)有益效果 | - |
| 7 | implementation-writer | 5.具体实施方式 | exa, web-search-prime |
| 8 | protection-extractor | 6.关键点和欲保护点 | google-patents-mcp |
| 9 | reference-collector | 7.其他参考资料 | google-patents-mcp, web-search-prime, web-reader |
| 10 | document-integrator | 文档整合 | - |

## 详细说明

### 1. title-generator（发明名称生成器）

**职责**：生成符合专利命名规范的发明名称

**输入参数**：
- `patent_type`：专利类型（发明专利/实用新型专利）
- `idea`：创新想法
- `technical_field`：技术领域

**输出文件**：`01_发明名称.md`

**命名要求**：
- 格式：一种XXXX方法/装置/系统/介质
- 简洁准确，不超过30字
- 体现技术类型（方法、装置、系统等）
- 不使用"新型"、"高效"、"改进"等修饰词
- 不包含人名、地名、商标、商业化用语

**专利类型差异**：
- 发明专利：可以使用"方法"、"装置"、"系统"等技术类型
- 实用新型专利：优先使用"装置"、"系统"等结构性技术类型，避免"方法"

---

### 2. field-analyzer（技术领域分析器）

**职责**：分析并描述技术方案所属的技术领域

**输入参数**：
- `patent_type`：专利类型
- `idea`：创新想法
- `technical_field`：技术领域

**输出文件**：`02_所属技术领域.md`

**描述要求**：
- 明确技术方案所属或应用的技术领域
- 可以是广义技术领域或细分技术领域
- 通常为1-2段文字

---

### 3. background-researcher（背景技术调研器）

**职责**：调研现有技术，分析技术问题，评估创新度

**输入参数**：
- `patent_type`：专利类型
- `idea`：创新想法
- `keywords`：关键词列表
- `starting_figure_number`：起始附图编号（可选）

**输出文件**：`03_相关的背景技术.md`

**使用的 MCP 工具**：
- `mcp__web-search-prime__webSearchPrime`：搜索现有产品和技术方案
- `mcp__google-patents-mcp__search_patents`：检索相关专利
- `mcp__exa__get_code_context_exa`：搜索技术实现参考
- `mcp__web_reader__webReader`：深入阅读技术文档

**搜索策略差异**：

| 搜索类型 | 发明专利 | 实用新型专利 |
|---------|---------|-------------|
| 专利检索范围 | 最近5-10年 | 最近3-5年 |
| 检索深度 | 国内外专利 + 学术论文 + 技术标准 | 国内专利 + 产品资料 |
| 检索语言 | 中英文 | 中文 |
| 重点关注 | 技术原理、算法创新 | 产品结构、构造 |

**创新度评估**：
- 现有技术接近度：高度/中度/低度
- 技术创新程度：高度/中度/低度
- 如果建议降级到实用新型专利，会返回提醒信息

**附图生成职责**：
- 根据内容需要动态生成现有技术架构图（可选）
- 以 Mermaid 代码块形式嵌入到章节中

---

### 4. problem-analyzer（技术问题分析器）

**职责**：分析现有技术存在的问题和缺陷

**输入参数**：
- `patent_type`：专利类型
- `idea`：创新想法
- `background_content`：背景技术内容
- `starting_figure_number`：起始附图编号（可选）

**输出文件**：`04_解决的技术问题.md`

**分析要求**：
- 针对现有技术的缺陷和不足
- 明确指出需要解决的技术问题
- 问题应具体、与发明解决方案相关

**附图生成职责**：
- 根据内容需要动态生成问题场景图（可选）

---

### 5. solution-designer（技术方案设计器）

**职责**：设计完整的技术方案

**输入参数**：
- `patent_type`：专利类型
- `idea`：创新想法
- `starting_figure_number`：起始附图编号（可选）

**输出文件**：`05_技术方案.md`

**使用的 MCP 工具**：
- `mcp__exa__get_code_context_exa`：搜索技术实现参考
- `mcp__web-search-prime__webSearchPrime`：搜索技术标准

**设计要求**：
- 描述技术方案的整体架构
- 说明关键技术手段
- 阐述技术原理

**附图生成职责**：
- 根据内容需要动态生成架构图、协议图、原理图（核心章节）

---

### 6. benefit-analyzer（有益效果分析器）

**职责**：分析技术方案带来的有益效果

**输入参数**：
- `patent_type`：专利类型
- `solution_content`：技术方案内容
- `starting_figure_number`：起始附图编号（可选）

**输出文件**：`06_有益效果.md`

**分析要求**：
- 描述技术方案带来的技术效果和优点
- 可以量化对比（性能提升、成本降低等）
- 效果应与技术方案有直接因果关系

**附图生成职责**：
- 根据内容需要动态生成效果对比图（可选）

---

### 7. implementation-writer（实施方式编写器）

**职责**：编写具体实施方式

**输入参数**：
- `patent_type`：专利类型
- `solution_content`：技术方案内容
- `starting_figure_number`：起始附图编号（可选）

**输出文件**：`07_具体实施方式.md`

**使用的 MCP 工具**：
- `mcp__exa__get_code_context_exa`：搜索技术实现参考
- `mcp__web-search-prime__webSearchPrime`：搜索技术标准

**编写要求**：
- 详细描述技术方案的具体实施方式
- 提供具体的工作原理和操作步骤
- 可以包含实施例

**附图生成职责**：
- 根据内容需要动态生成流程图、时序图（核心章节）

---

### 8. protection-extractor（保护点提炼器）

**职责**：提炼技术方案的关键创新点和保护点

**输入参数**：
- `idea`：创新想法
- `solution_content`：技术方案内容

**输出文件**：`08_关键点和欲保护点.md`

**使用的 MCP 工具**：
- `mcp__google-patents-mcp__search_patents`：检索相关专利

**提炼要求**：
- 识别技术方案的核心创新点
- 提炼关键技术特征
- 明确保护范围

---

### 9. reference-collector（参考资料收集器）

**职责**：收集相关参考文献和资料

**输入参数**：
- `patent_type`：专利类型
- `technical_field`：技术领域

**输出文件**：`09_其他有助于理解本技术的资料.md`

**使用的 MCP 工具**：
- `mcp__google-patents-mcp__search_patents`：检索相关专利
- `mcp__web-search-prime__webSearchPrime`：搜索技术资料
- `mcp__web_reader__webReader`：提取网页内容

**收集内容**：
- 相关专利文献
- 技术标准文档
- 学术论文
- 技术报告

---

### 10. document-integrator（文档整合器）

**职责**：整合所有章节，生成完整交底书

**输入参数**：
- `patent_type`：专利类型

**输出文件**：`专利申请技术交底书_[发明名称].md`

**整合要求**：
- 严格按照 IP-JL-027 模板格式
- 附图以 Mermaid 代码块形式嵌入到对应章节中
- 确保章节编号和格式正确

**格式规范**：
- 章节编号：`## **1. **`、`## **2. **` 等（阿拉伯数字 + 粗体）
- 章节标题：`**发明创造名称**`（粗体）
- 子章节：`### **（1）**`、`### **（2）**` 等（中文括号 + 粗体）

## 附图生成说明

### 附图编号管理

- 使用全局计数器确保附图编号从1开始连续
- 各章节生成器接收 `starting_figure_number` 参数
- 生成器返回实际生成的附图数量
- 下一个章节的起始编号 = 当前起始编号 + 已生成数量

### 附图类型映射

| 附图类型 | 主要生成器 | 适用章节 |
|---------|-----------|---------|
| 流程图 | flowchart-generator | 07_具体实施方式 |
| 时序图 | sequence-generator | 07_具体实施方式 |
| 架构图 | architecture-generator | 03_背景技术, 05_技术方案 |
| 协议图 | protocol-generator | 05_技术方案 |
| 原理图 | architecture-generator | 05_技术方案 |
| 场景图 | architecture-generator | 04_技术问题 |
| 效果对比图 | 架构图变体 | 06_有益效果 |

### 附图嵌入格式

```markdown
#### 附图X：[附图名称]

```mermaid
[Mermaid代码]
```

图X说明：[附图说明文字]
```

## 执行顺序

子代理按照以下顺序串行执行：

```
1. title-generator
2. field-analyzer
3. background-researcher
   ├─ 创新度评估（降级建议）
4. problem-analyzer
5. solution-designer
6. benefit-analyzer
7. implementation-writer
8. protection-extractor
9. reference-collector
10. document-integrator
```

**注意**：
- background-researcher 执行后，如果返回降级建议，会询问用户是否接受
- 如果接受降级，后续子代理使用更新后的专利类型
- 附图编号全局连续管理
