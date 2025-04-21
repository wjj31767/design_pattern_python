"""
跨平台 UI 组件（组件类型 vs 操作系统）
场景描述
开发一套跨平台 UI 框架，支持按钮（Button）、文本框（TextField）等组件在 Windows、Mac、Linux 系统上渲染，且组件和系统实现可独立扩展。
抽象与实现分离
抽象部分（UI 组件）：定义 UIComponent 抽象类，声明交互接口（如 click()），持有系统实现的引用。
"""


class UIComponent:
    def __init__(self, os_renderer):
        self.os_renderer = os_renderer  # 桥接系统渲染器

    def click(self):
        raise NotImplementedError


class Button(UIComponent):
    def click(self):
        print("按钮被点击：", end="")
        self.os_renderer.render_button()


class OSRenderer:
    def render_button(self):
        raise NotImplementedError


class WindowsRenderer(OSRenderer):
    def render_button(self):
        print("Windows 风格按钮（矩形边框，蓝色背景）")


class MacRenderer(OSRenderer):
    def render_button(self):
        print("Mac 风格按钮（圆角边框，灰色背景）")
        
