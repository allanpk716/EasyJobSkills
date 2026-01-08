---
description: 将 Markdown 格式的专利交底书转换为 DOCX 格式
arguments:
  - name: markdown_file
    description: Markdown 交底书文件路径（必需）
    required: true
  - name: output_dir
    description: 输出目录（可选，默认与 Markdown 文件同目录）
    required: false
---

# 专利交底书 Markdown 转 DOCX

你正在调用专利交底书 Markdown 转 DOCX 转换命令。本命令将已有的 Markdown 格式交底书转换为正式的 DOCX 格式，包含附图渲染和质量验证。

## 执行步骤

### 1. 参数验证和路径确定

**步骤 1.1：验证 Markdown 文件**

确认 `markdown_file` 参数指向的文件存在：
- 使用 Glob 或 Read 工具验证文件存在
- 如果文件不存在，提示用户检查路径

**步骤 1.2：确定输出目录**

- 如果指定了 `output_dir`，使用该目录
- 如果未指定，使用 Markdown 文件所在目录

**步骤 1.3：提取发明名称**

从 Markdown 文件路径或内容中提取发明名称，用于命名输出文件：
- 文件名格式：`专利申请技术交底书_[发明名称].md`
- 输出 DOCX：`专利申请技术交底书_[发明名称].docx`

### 2. 环境检查

在开始转换前，检查所有依赖项。

**步骤 2.1：检查 Python 环境**

```bash
python --version
```

要求：Python >= 3.7

**步骤 2.2：检查 python-docx 库**

```bash
python -c "import docx; print(docx.__version__)"
```

如果未安装，提供安装指导：
```bash
pip install python-docx
```

**步骤 2.3：检查字体**

运行字体检查脚本：
```bash
python .claude/scripts/docx_conversion/font_utils.py
```

检查思源黑体 CN 字体是否已安装。

如果未安装，提供安装指导：
```
❌ 系统未安装思源黑体 CN 字体

💡 解决方法：

1. 下载思源黑体（Source Han Sans）字体
   访问: https://github.com/adobe-fonts/source-han-sans/releases
   下载: SourceHanSansSC.zip (简体中文版本)

2. 安装字体

   Windows: 右键字体文件，选择"安装"
   macOS: 双击字体文件，点击"安装字体"
   Linux: 复制到 ~/.fonts/，运行 fc-cache -fv
```

**步骤 2.4：检查 mermaid-cli**

```bash
mmdc --version
```

如果未安装，提供安装指导：
```bash
npm install -g @mermaid-js/mermaid-cli
```

**步骤 2.5：检查 DOCX 模板**

确认模板文件存在：
`skills/patent-disclosure-writer/templates/发明、实用新型专利申请交底书 模板.docx`

### 3. Markdown 解析

使用 Bash 工具执行 Markdown 解析脚本：

```bash
python .claude/scripts/docx_conversion/markdown_parser.py "{markdown_file_path}" "{output_dir}/parsed_sections.json"
```

**预期输出**：
- `parsed_sections.json`：包含章节结构的 JSON 文件
- 解析统计信息（标题、章节数量、验证结果）

**验证**：
- 检查 `validation.is_complete` 是否为 `true`
- 确认包含7个主要章节和第4章节的3个子项

### 4. DOCX 生成

使用 Bash 工具执行 DOCX 生成脚本：

```bash
python .claude/scripts/docx_conversion/docx_generator.py \
  "{output_dir}/parsed_sections.json" \
  "skills/patent-disclosure-writer/templates/发明、实用新型专利申请交底书 模板.docx" \
  "{output_dir}/专利申请技术交底书_{发明名称}.docx"
```

**预期输出**：
- `专利申请技术交底书_{发明名称}.docx`：生成的 DOCX 文件
- 生成统计信息（段落数、章节填充数、字体应用）

### 5. 附图渲染和插入（可选）

如果 Markdown 文件中包含 Mermaid 代码块（附图），执行附图渲染和插入：

**步骤 5.1：检查是否存在附图**

检查 `10_附图说明.md` 文件或 Markdown 中的 Mermaid 代码块。

**步骤 5.2：渲染 Mermaid 图表**

使用 Bash 工具执行附图插入脚本：

```bash
python .claude/scripts/docx_conversion/diagram_inserter.py \
  "{markdown_file_path}" \
  "{output_dir}/专利申请技术交底书_{发明名称}.docx" \
  "{output_dir}/10_附图说明.md" \
  "{output_dir}/diagram_images"
```

**预期输出**：
- 渲染的图片文件（PNG格式，保存在 `{output_dir}/diagram_images/`）
- 修改后的 DOCX 文件（包含插入的图片）
- 附图插入报告（JSON格式）

### 6. DOCX 验证

使用 Bash 工具执行 DOCX 验证脚本：

```bash
python .claude/scripts/docx_conversion/docx_validator.py \
  "{output_dir}/专利申请技术交底书_{发明名称}.docx" \
  "{output_dir}/validation_report.json" \
  --level strict
```

**预期输出**：
- `validation_report.json`：验证报告
- 总体评分（0-100）
- 详细检查结果（6个类别）
- 关键问题和改进建议

**通过标准**：
- 总体评分 >= 80分
- 没有关键问题

### 7. 展示结果

读取验证报告并向用户展示：

```markdown
## DOCX 转换完成

**Markdown 文件**: {markdown_file_path}
**DOCX 文件**: {output_dir}/专利申请技术交底书_{发明名称}.docx
**验证报告**: {output_dir}/validation_report.json

---

### 验证结果总览

⭐ **总体评分**: {overall_score}/100
{validation_status}

---

### 详细检查结果

{详细检查结果}

---

📄 生成的 DOCX 文件已通过质量检查，可以交付给专利代理机构使用。
```

**如果验证未通过**，显示详细的改进建议：

```markdown
⚠️ **验证未通过**

**总体评分**: {overall_score}/100
**通过标准**: >= 80分 且无关键问题

---

### ⚠️ 关键问题

{critical_issues}

---

### 💡 改进建议

{recommendations}
```

## 错误处理

### Markdown 解析失败

```
❌ Markdown 解析失败
💡 请检查 Markdown 文件格式是否符合规范
💡 确认包含7个章节和第4章节的3个子项
💡 检查章节编号格式：## **1. **、## **2. ** 等
```

### DOCX 生成失败

```
❌ DOCX 生成失败
💡 请检查思源黑体 CN 字体是否已安装
💡 请检查模板文件是否存在
💡 参考 step 2 中的安装指导
```

### mermaid-cli 未安装

```
❌ 附图渲染失败：mermaid-cli 未安装

💡 解决方法：

1. 安装 Node.js（如果未安装）
   访问: https://nodejs.org/

2. 安装 mermaid-cli
   npm install -g @mermaid-js/mermaid-cli

3. 验证安装
   mmdc --version
```

### DOCX 验证未通过

```
❌ DOCX 验证未通过
💡 请查看验证报告中的详细问题
💡 根据改进建议修复问题或重新生成
```

## 注意事项

1. **字体要求**：必须安装思源黑体 CN 字体，否则生成的 DOCX 字体会不正确
2. **Mermaid 渲染**：需要安装 mermaid-cli，附图才能正确渲染
3. **模板文件**：确保 DOCX 模板文件存在于正确位置
4. **文件编码**：Markdown 文件必须使用 UTF-8 编码

## 输出文件

执行完成后，输出目录将包含以下文件：

| 文件 | 说明 |
|------|------|
| `专利申请技术交底书_{发明名称}.docx` | 正式的 DOCX 格式交底书 |
| `parsed_sections.json` | Markdown 解析结果 |
| `validation_report.json` | DOCX 质量验证报告 |
| `diagram_images/` | 附图渲染图片（如果存在附图） |
