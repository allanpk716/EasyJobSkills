"""
字体工具函数 - 检查和安装字体
"""

import platform
from typing import List


class FontChecker:
    """字体检查器"""

    def __init__(self):
        """初始化字体检查器"""
        self.system = platform.system()
        self._cached_fonts = None

    def get_installed_fonts(self) -> List[str]:
        """
        获取系统已安装的字体列表

        Returns:
            字体名称列表
        """
        if self._cached_fonts is not None:
            return self._cached_fonts

        if self.system == "Windows":
            fonts = self._get_windows_fonts()
        elif self.system == "Darwin":  # macOS
            fonts = self._get_mac_fonts()
        elif self.system == "Linux":
            fonts = self._get_linux_fonts()
        else:
            fonts = []

        self._cached_fonts = fonts
        return fonts

    def _get_windows_fonts(self) -> List[str]:
        """获取 Windows 系统字体"""
        import winreg

        fonts = []
        try:
            key = winreg.OpenKey(
                winreg.HKEY_LOCAL_MACHINE,
                r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts",
            )
            i = 0
            while True:
                try:
                    font_name = winreg.EnumValue(key, i)[0]
                    fonts.append(font_name)
                    i += 1
                except WindowsError:
                    break
            winreg.CloseKey(key)
        except Exception as e:
            print(f"读取 Windows 字体列表失败: {e}")

        return fonts

    def _get_mac_fonts(self) -> List[str]:
        """获取 macOS 系统字体"""
        import os

        fonts = []

        font_dirs = [
            "/Library/Fonts",
            "/System/Library/Fonts",
            os.path.expanduser("~/Library/Fonts"),
        ]

        for font_dir in font_dirs:
            if os.path.exists(font_dir):
                for file in os.listdir(font_dir):
                    if file.endswith((".ttf", ".otf", ".ttc")):
                        # 移除扩展名
                        font_name = os.path.splitext(file)[0]
                        fonts.append(font_name)

        return fonts

    def _get_linux_fonts(self) -> List[str]:
        """获取 Linux 系统字体"""
        import os

        fonts = []

        font_dirs = [
            "/usr/share/fonts",
            "/usr/local/share/fonts",
            os.path.expanduser("~/.fonts"),
        ]

        for font_dir in font_dirs:
            if os.path.exists(font_dir):
                for root, dirs, files in os.walk(font_dir):
                    for file in files:
                        if file.endswith((".ttf", ".otf", ".ttc")):
                            # 移除扩展名
                            font_name = os.path.splitext(file)[0]
                            fonts.append(font_name)

        return fonts

    def is_font_available(self, font_name: str) -> bool:
        """
        检查字体是否可用

        Args:
            font_name: 字体名称

        Returns:
            字体是否可用
        """
        installed_fonts = self.get_installed_fonts()

        # 不区分大小写匹配
        font_name_lower = font_name.lower()
        for installed in installed_fonts:
            if font_name_lower in installed.lower():
                return True

        return False


class FontInstaller:
    """字体安装器"""

    SOURCE_HAN_SANS_URL = "https://github.com/adobe-fonts/source-han-sans/releases"

    @staticmethod
    def get_installation_guide() -> str:
        """
        获取字体安装指南

        Returns:
            安装指南文本
        """
        return f"""
思源黑体（Source Han Sans）字体安装指南
=====================================

1. 下载字体
   访问: {FontInstaller.SOURCE_HAN_SANS_URL}
   下载: SourceHanSansSC.zip (简体中文版本)

2. Windows 安装:
   - 解压下载的 ZIP 文件
   - 找到 OTF 或 TTF 文件
   - 右键点击字体文件，选择"安装"或"为所有用户安装"
   - 或将字体文件复制到 C:\\Windows\\Fonts\\

3. macOS 安装:
   - 解压下载的 ZIP 文件
   - 双击字体文件
   - 点击"安装字体"按钮
   - 或将字体文件复制到 ~/Library/Fonts/

4. Linux 安装:
   - 解压下载的 ZIP 文件
   - 复制字体文件到 ~/.fonts/ 或 /usr/share/fonts/
   - 运行: fc-cache -fv

5. 验证安装:
   安装完成后，重新运行程序自动检测字体。

=====================================
"""


if __name__ == "__main__":
    # 测试代码
    print("系统平台:", platform.system())
    checker = FontChecker()
    fonts = checker.get_installed_fonts()
    print(f"找到 {len(fonts)} 个字体")

    # 检查思源黑体 CN
    source_han_fonts = [
        "思源黑体 CN",
        "思源黑体 CN Bold",
        "思源黑体 CN Normal",
        "Source Han Sans CN",
    ]

    print("\n检查思源黑体 CN 字体:")
    for font in source_han_fonts:
        available = checker.is_font_available(font)
        print(f"  {font}: {'✓ 已安装' if available else '✗ 未安装'}")
