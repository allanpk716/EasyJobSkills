"""
Markdown 解析器 - 解析专利交底书 Markdown 文件
提取章节结构和内容，输出 JSON 格式
"""

import re
import json
from typing import Dict, List, Any
from pathlib import Path
from datetime import datetime

from .exceptions import MarkdownParseError


class MarkdownParser:
    """专利交底书 Markdown 解析器"""

    # 主要章节正则模式：## **1. 发明创造名称**
    MAIN_SECTION_PATTERN = re.compile(r"^##\s*\*\*(\d+)\.\s*(.+?)\*\*")

    # 子章节正则模式：### **（1）解决的技术问题**
    SUBSECTION_PATTERN = re.compile(r"^###\s*\*\*（(\d+)）(.+?)\*\*")

    # 必需章节列表
    REQUIRED_SECTIONS = ["1", "2", "3", "4", "5", "6", "7"]

    # 第4章节必需子项
    REQUIRED_SUBSECTIONS = ["1", "2", "3"]

    def __init__(self, markdown_path: str):
        """
        初始化解析器

        Args:
            markdown_path: Markdown 文件路径
        """
        self.markdown_path = Path(markdown_path)
        if not self.markdown_path.exists():
            raise MarkdownParseError(markdown_path, "文件不存在")

        self.content = self._read_markdown()
        self.sections = []

    def _read_markdown(self) -> str:
        """读取 Markdown 文件内容"""
        with open(self.markdown_path, "r", encoding="utf-8") as f:
            return f.read()

    def parse(self) -> Dict[str, Any]:
        """
        解析 Markdown 文件

        Returns:
            包含标题和章节结构的字典
        """
        lines = self.content.split("\n")

        # 提取标题（第一行 # 开头）
        title = self._extract_title(lines)

        # 解析章节
        self.sections = self._parse_sections(lines)

        # 验证完整性
        validation_result = self._validate_completeness()

        result = {
            "title": title,
            "sections": self.sections,
            "metadata": {
                "total_sections": len(self.sections),
                "has_subsections": any(s.get("subsections") for s in self.sections),
                "parsing_timestamp": datetime.now().isoformat(),
            },
            "validation": validation_result,
        }

        return result

    def _extract_title(self, lines: List[str]) -> str:
        """提取文档标题"""
        for line in lines:
            if line.strip().startswith("#"):
                # 移除 # 标记和空白
                title = re.sub(r"^#+\s*", "", line).strip()
                return title
        return "专利申请技术交底书"

    def _parse_sections(self, lines: List[str]) -> List[Dict[str, Any]]:
        """解析章节结构"""
        sections = []
        current_section = None
        current_content = []

        for line in lines:
            # 检查主要章节
            main_match = self.MAIN_SECTION_PATTERN.match(line)
            if main_match:
                # 保存上一章节
                if current_section:
                    current_section["content"] = "\n".join(current_content).strip()
                    sections.append(current_section)

                # 开始新章节
                section_number = main_match.group(1)
                section_title = main_match.group(2).strip()
                current_section = {
                    "number": section_number,
                    "title": section_title,
                    "content": "",
                    "level": 2,
                }
                current_content = []
                continue

            # 检查子章节（仅在第4章节下）
            if current_section and current_section["number"] == "4":
                sub_match = self.SUBSECTION_PATTERN.match(line)
                if sub_match:
                    # 保存章节当前内容
                    if current_content:
                        if "content" not in current_section or not current_section["content"]:
                            current_section["content"] = "\n".join(current_content).strip()

                    # 初始化 subsections 列表
                    if "subsections" not in current_section:
                        current_section["subsections"] = []

                    # 保存上一个子章节（如果有）
                    subsections = current_section["subsections"]
                    if subsections and subsections[-1].get("content") == "":
                        subsections[-1]["content"] = "\n".join(current_content).strip()

                    # 开始新子章节
                    sub_number = f"4.{sub_match.group(1)}"
                    sub_title = sub_match.group(2).strip()
                    subsections.append(
                        {
                            "number": sub_number,
                            "title": sub_title,
                            "content": "",
                            "level": 3,
                        }
                    )
                    current_content = []
                    continue

            # 累积内容
            if current_section:
                # 过滤掉章节标题行和空行
                if (
                    line.strip()
                    and not self.MAIN_SECTION_PATTERN.match(line)
                    and not self.SUBSECTION_PATTERN.match(line)
                ):
                    current_content.append(line)

        # 保存最后一章节
        if current_section:
            current_section["content"] = "\n".join(current_content).strip()
            sections.append(current_section)

        return sections

    def _validate_completeness(self) -> Dict[str, Any]:
        """验证章节完整性"""
        found_numbers = [s["number"] for s in self.sections]
        missing_numbers = [
            n for n in self.REQUIRED_SECTIONS if n not in found_numbers
        ]

        # 检查第4章节的子项
        section_4 = next((s for s in self.sections if s["number"] == "4"), None)
        subsections_complete = True
        missing_subsections = []

        if section_4 and "subsections" in section_4:
            found_subs = [
                s["number"].split(".")[-1] for s in section_4["subsections"]
            ]
            missing_subsections = [
                n for n in self.REQUIRED_SUBSECTIONS if n not in found_subs
            ]
            subsections_complete = len(missing_subsections) == 0

        return {
            "is_complete": len(missing_numbers) == 0 and subsections_complete,
            "missing_sections": missing_numbers,
            "missing_subsections": missing_subsections,
            "all_sections_found": len(found_numbers),
            "expected_sections": len(self.REQUIRED_SECTIONS),
        }

    def save_json(self, output_path: str):
        """
        保存解析结果为 JSON 文件

        Args:
            output_path: 输出 JSON 文件路径
        """
        result = self.parse()
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        return output_path


def main():
    """命令行入口"""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python markdown_parser.py <markdown_file> [output_json]")
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_json = sys.argv[2] if len(sys.argv) > 2 else "parsed_sections.json"

    try:
        parser = MarkdownParser(markdown_file)
        result = parser.parse()

        with open(output_json, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)

        print(f"✅ 解析完成！结果保存到: {output_json}")
        print(f"📄 标题: {result['title']}")
        print(f"📊 章节数量: {len(result['sections'])}")

        # 显示验证结果
        validation = result.get("validation", {})
        if validation.get("is_complete"):
            print("✅ 章节完整性检查通过")
        else:
            print("⚠️  章节完整性检查发现问题:")
            if validation.get("missing_sections"):
                print(f"   缺失章节: {validation['missing_sections']}")
            if validation.get("missing_subsections"):
                print(f"   缺失子章节: {validation['missing_subsections']}")

    except MarkdownParseError as e:
        print(f"❌ {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ 解析失败: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
