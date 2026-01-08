"""
自定义异常类 - DOCX 转换模块的异常定义
"""


class DocxConversionError(Exception):
    """DOCX 转换基础异常类

    所有 DOCX 转换相关的异常都应该继承此类。
    """

    pass


class FontNotFoundError(DocxConversionError):
    """字体未找到异常

    当系统未安装所需字体时抛出此异常。
    """

    def __init__(self, font_name: str, install_guide: str = ""):
        """
        初始化字体未找到异常

        Args:
            font_name: 未找到的字体名称
            install_guide: 字体安装指南（可选）
        """
        self.font_name = font_name
        self.install_guide = install_guide
        message = f"系统未安装字体: {font_name}"
        if install_guide:
            message += f"\n{install_guide}"
        super().__init__(message)


class TemplateNotFoundError(DocxConversionError):
    """模板文件未找到异常

    当 DOCX 模板文件不存在时抛出此异常。
    """

    def __init__(self, template_path: str):
        """
        初始化模板未找到异常

        Args:
            template_path: 模板文件路径
        """
        self.template_path = template_path
        message = f"模板文件不存在: {template_path}"
        super().__init__(message)


class MarkdownParseError(DocxConversionError):
    """Markdown 解析异常

    当解析 Markdown 文件失败时抛出此异常。
    """

    def __init__(self, markdown_path: str, reason: str = ""):
        """
        初始化 Markdown 解析异常

        Args:
            markdown_path: Markdown 文件路径
            reason: 解析失败原因（可选）
        """
        self.markdown_path = markdown_path
        self.reason = reason
        message = f"Markdown 解析失败: {markdown_path}"
        if reason:
            message += f"\n原因: {reason}"
        super().__init__(message)


class ValidationError(DocxConversionError):
    """验证异常

    当 DOCX 文件验证失败时抛出此异常。
    """

    def __init__(self, docx_path: str, validation_errors: list):
        """
        初始化验证异常

        Args:
            docx_path: DOCX 文件路径
            validation_errors: 验证错误列表
        """
        self.docx_path = docx_path
        self.validation_errors = validation_errors
        message = f"DOCX 验证失败: {docx_path}\n"
        message += "\n".join(f"- {error}" for error in validation_errors)
        super().__init__(message)
