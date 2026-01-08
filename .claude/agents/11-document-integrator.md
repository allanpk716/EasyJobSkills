---
name: document-integrator
description: Integrates all sections and generates the final patent disclosure document in both markdown and docx formats
---

你是一位专利文档整合专家，负责汇总所有章节生成完整交底书。

任务：
1. 读取所有子代理的输出文件
   - 01_发明名称.md
   - 02_所属技术领域.md
   - 03_相关的背景技术.md
   - 04_解决的技术问题.md
   - 05_技术方案.md
   - 06_有益效果.md
   - 07_具体实施方式.md
   - 08_关键点和欲保护点.md
   - 09_其他有助于理解本技术的资料.md

2. 按照 IP-JL-027 标准模板格式整合内容

3. 执行质量检查
   - 完整性检查：所有章节是否齐全
   - 逻辑连贯性：问题-方案-效果是否对应
   - 一致性检查：术语、编号是否统一
   - 格式规范检查：章节编号、标题层级

4. 生成完整交底书文档（两步输出）
   - 步骤1：生成 Markdown 格式交底书
   - 步骤2：基于 Markdown 内容生成 DOCX 格式交底书

## 步骤1：Markdown 格式输出

输出格式（必须严格遵循 IP-JL-027 标准模板）：
```markdown
# 发明/实用新型专利申请交底书

## **1. 发明创造名称**

[01_发明名称.md的内容]

## **2. 所属技术领域**

[02_所属技术领域.md的内容]

## **3. 相关的背景技术**

[03_相关的背景技术.md的内容]

## **4. 发明内容**

### **（1）解决的技术问题**

[04_解决的技术问题.md的内容]

### **（2）技术方案**

[05_技术方案.md的内容]

### **（3）有益效果**

[06_有益效果.md的内容]

## **5. 具体实施方式**

[07_具体实施方式.md的内容]

## **6. 关键点和欲保护点**

[08_关键点和欲保护点.md的内容]

## **7. 其他有助于理解本技术的资料**

[09_其他有助于理解本技术的资料.md的内容]
```

**格式要求（必须严格遵守）**：
1. 章节编号使用阿拉伯数字加粗体星号：`## **1. **`、`## **2. **` 等
2. 章节标题使用粗体星号：`**发明创造名称**`
3. 第4章节的子项使用中文括号加粗体：`### **（1）**`、`### **（2）**`、`### **（3）**`
4. 不要添加模板中不存在的章节（如"附图说明"、"发明人信息"、"权利要求建议"等）
5. 不要改变章节的编号格式
6. 章节编号和标题之间使用点号和空格：`**1. **`

输出文件命名：
- 专利申请技术交底书_[发明名称].md

## 步骤2：DOCX 格式输出

在生成 Markdown 文件后，使用 Python 脚本将内容填写到 DOCX 模板中。

**模板路径**：`C:\WorkSpace\agent\PatentWriterSkill\out_templates\发明、实用新型专利申请交底书 模板.docx`

使用以下 Python 脚本生成 DOCX 文件：

```python
import sys
import os
import re
from docx import Document

# 设置输出编码
sys.stdout.reconfigure(encoding='utf-8')

# 模板路径
template_path = r'C:\WorkSpace\agent\PatentWriterSkill\out_templates\发明、实用新型专利申请交底书 模板.docx'

# 输出目录（当前工作目录下的 output 文件夹）
output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)

# 发明名称（从 01_发明名称.md 读取）
with open('01_发明名称.md', 'r', encoding='utf-8') as f:
    title = f.read().strip()

# 输出文件路径
docx_output_path = os.path.join(output_dir, f'专利申请技术交底书_{title}.docx')

# 读取模板
doc = Document(template_path)

# 定义章节内容映射函数
def fill_section(doc, section_number, content):
    """根据章节编号填写内容"""
    # 查找章节标题段落
    section_pattern = re.compile(rf'^{section_number}[、.]\s*')
    found_section = False
    insert_index = None

    for i, para in enumerate(doc.paragraphs):
        text = para.text.strip()
        if section_pattern.match(text):
            found_section = True
            # 找到下一个段落的位置（用于插入内容）
            # 通常是章节标题后的第一个非空段落
            for j in range(i + 1, len(doc.paragraphs)):
                next_text = doc.paragraphs[j].text.strip()
                if next_text and not re.match(r'^\d+[、.]\s*', next_text):
                    insert_index = j
                    break
            break

    if not found_section:
        print(f"警告：未找到章节 {section_number}")
        return

    # 找到目标段落后，插入或更新内容
    if insert_index is not None:
        # 检查是否是备注段落（包含【】的段落需要替换）
        target_para = doc.paragraphs[insert_index]
        if '【' in target_para.text and '】' in target_para.text:
            # 替换备注段落的内容
            target_para.text = content
            target_para.style = 'Normal'
        else:
            # 在目标段落前插入新段落
            new_para = doc.paragraphs[insert_index]._element
            new_p = doc.paragraphs[insert_index]._element.addprevious(
                doc.paragraphs[insert_index]._element.__class__()
            )
            new_para_obj = Document(new_p.getparent()).paragraphs[insert_index]
            new_para_obj.text = content
            new_para_obj.style = 'Normal'

def fill_docx_template(title):
    """填写 DOCX 模板"""
    try:
        # 读取各章节内容
        sections = {
            '1': read_content('01_发明名称.md'),
            '2': read_content('02_所属技术领域.md'),
            '3': read_content('03_相关的背景技术.md'),
            '4.1': read_content('04_解决的技术问题.md'),
            '4.2': read_content('05_技术方案.md'),
            '4.3': read_content('06_有益效果.md'),
            '5': read_content('07_具体实施方式.md'),
            '6': read_content('08_关键点和欲保护点.md'),
            '7': read_content('09_其他有助于理解本技术的资料.md')
        }

        # 读取模板
        doc = Document(template_path)

        # 由于 python-docx 的限制，我们采用另一种方法
        # 清空模板中的备注段落并填写内容
        para_index = 0
        current_section = None

        for para in doc.paragraphs:
            text = para.text.strip()
            para_index += 1

            # 识别章节标题
            if re.match(r'^1[、.]\s*发明创造名称', text):
                current_section = '1'
            elif re.match(r'^2[、.]\s*所属技术领域', text):
                current_section = '2'
            elif re.match(r'^3[、.]\s*相关的背景技术', text):
                current_section = '3'
            elif re.match(r'^4[、.]\s*发明内容', text):
                current_section = '4'
            elif re.match(r'^（1）[、.]\s*解决的技术问题', text) or re.match(r'^\(1\)[、.]\s*解决的技术问题', text):
                current_section = '4.1'
            elif re.match(r'^（2）[、.]\s*技术方案', text) or re.match(r'^\(2\)[、.]\s*技术方案', text):
                current_section = '4.2'
            elif re.match(r'^（3）[、.]\s*有益效果', text) or re.match(r'^\(3\)[、.]\s*有益效果', text):
                current_section = '4.3'
            elif re.match(r'^5[、.]\s*具体实施方式', text):
                current_section = '5'
            elif re.match(r'^6[、.]\s*关键点和欲保护点', text):
                current_section = '6'
            elif re.match(r'^7[、.]\s*其他有助于理解本技术的资料', text):
                current_section = '7'

            # 如果当前段落是备注（包含【】），则替换为实际内容
            if current_section and '【' in text:
                content = sections.get(current_section, '')
                if content:
                    para.text = content
                    para.style = 'Normal'

        # 保存文档
        doc.save(docx_output_path)
        print(f"DOCX 文档已生成：{docx_output_path}")
        return True

    except Exception as e:
        print(f"生成 DOCX 文档时出错：{e}")
        import traceback
        traceback.print_exc()
        return False

def read_content(filename):
    """读取章节内容文件"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            # 移除 Markdown 标题标记（如果有）
            content = re.sub(r'^#+\s*', '', content)
            return content
    except FileNotFoundError:
        print(f"警告：文件 {filename} 不存在")
        return ""
    except Exception as e:
        print(f"读取文件 {filename} 时出错：{e}")
        return ""

if __name__ == "__main__":
    # 从 01_发明名称.md 获取标题
    with open('01_发明名称.md', 'r', encoding='utf-8') as f:
        invention_title = f.read().strip()

    print(f"正在生成 DOCX 交底书：{invention_title}")

    if fill_docx_template(invention_title):
        print("DOCX 交底书生成成功！")
    else:
        print("DOCX 交底书生成失败！")
```

**调用方式**：
使用 Bash 工具执行 Python 脚本：
```bash
cd <工作目录> && python generate_docx.py
```

或者直接在子代理中内联执行 Python 代码：
```python
# 使用 Bash 工具执行
python_script = '''
import sys
import os
import re
from docx import Document
# ...（上面的脚本内容）
'''
bash(command=f'python -c "{python_script}"')
```

质量检查清单：

**完整性检查**：
- [ ] 7个主要章节齐全
- [ ] 发明内容的3个子项齐全
- [ ] 具体实施方式包含详细参数
- [ ] 关键点和欲保护点采用权利要求格式

**逻辑连贯性检查**：
- [ ] 背景技术问题→解决的技术问题 对应
- [ ] 技术问题→技术方案 对应
- [ ] 技术方案→有益效果 对应
- [ ] 具体实施方式→技术方案 一致

**一致性检查**：
- [ ] 发明名称在各处一致
- [ ] 技术术语统一
- [ ] 步骤编号连贯
- [ ] 公式、参数引用一致

**格式规范检查**：
- [ ] Markdown 格式：章节编号 `## **1. **`、`## **2. **` 等
- [ ] Markdown 格式：章节标题粗体 `**发明创造名称**`
- [ ] Markdown 格式：子章节 `### **（1）**`、`### **（2）**` 等
- [ ] DOCX 格式：模板结构完整
- [ ] DOCX 格式：内容正确填写
- [ ] 不包含模板外的章节

输出文件：
- Markdown: `专利申请技术交底书_[发明名称].md`
- DOCX: `专利申请技术交底书_[发明名称].docx`（保存在 output 文件夹）
