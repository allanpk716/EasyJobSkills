"""
DOCX 转换模块 - Markdown 转 DOCX 工具包

本模块提供完整的 Markdown 到 DOCX 转换功能，包括：
- 环境检查（Python 版本、库、字体）
- Markdown 解析
- DOCX 生成
- DOCX 验证
"""

__version__ = "1.0.0"
__author__ = "EasyJob Skills"

from .exceptions import (
    DocxConversionError,
    FontNotFoundError,
    TemplateNotFoundError,
    MarkdownParseError,
    ValidationError,
)

__all__ = [
    "DocxConversionError",
    "FontNotFoundError",
    "TemplateNotFoundError",
    "MarkdownParseError",
    "ValidationError",
]
