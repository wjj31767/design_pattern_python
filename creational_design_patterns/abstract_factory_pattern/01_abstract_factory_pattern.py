"""
抽象工厂模式（Abstract Factory Pattern）是一种创建型设计模式，它提供了一个创建一系列相关或相互依赖对象的接口，而无需指定它们具体的类。该模式通过将对象的创建逻辑抽象化，使得客户端代码可以在不依赖具体实现的情况下生成不同类型的对象家族。
核心思想
分离对象创建：将对象的创建过程封装在工厂类中，客户端只需与抽象工厂和抽象产品交互，无需关心具体实现。
支持多产品家族：可以创建多个相关产品（如 “Windows 按钮” 和 “Windows 文本框” 属于同一产品家族），确保同一家族的产品协同工作。
模式结构
抽象工厂（Abstract Factory）
定义创建抽象产品的接口，声明一组创建不同产品的方法（如 createButton()、createTextField()）。
具体工厂（Concrete Factory）
实现抽象工厂接口，负责创建具体产品（如 WindowsFactory 创建 Windows 风格的按钮和文本框）。
抽象产品（Abstract Product）
定义产品的通用接口（如 Button、TextField）。
具体产品（Concrete Product）
实现抽象产品接口，是具体工厂创建的实际对象（如 WindowsButton、MacButton）。
示例代码
假设我们需要为不同操作系统（Windows 和 Mac）创建界面组件（按钮和文本框），使用抽象工厂模式实现：
"""


# 抽象按钮
class Button:
    def click(self):
        raise NotImplementedError


# 抽象文本框
class TextField:
    def enter_text(self, text):
        raise NotImplementedError


class WindowsButton(Button):
    def click(self):
        print("Windows 按钮被点击")


class WindowsTextField(TextField):
    def enter_text(self, text):
        print(f"在 Windows 文本框中输入：{text}")


class MacButton(Button):
    def click(self):
        print("Mac 按钮被点击")


class MacTextField(TextField):
    def enter_text(self, text):
        print(f"在 Mac 文本框中输入：{text}")


class UIFactory:
    def create_button(self):
        raise NotImplementedError

    def create_text_field(self):
        raise NotImplementedError


class WindowsFactory(UIFactory):
    def create_button(self):
        return WindowsButton()

    def create_text_field(self):
        return WindowsTextField()


class MacFactory(UIFactory):
    def create_button(self):
        return MacButton()

    def create_text_field(self):
        return MacTextField()


def create_ui(factory: UIFactory):
    button = factory.create_button()
    text_field = factory.create_text_field()
    button.click()
    text_field.enter_text("Hello, World!")


# 使用 Windows 工厂创建界面
create_ui(WindowsFactory())  # 输出：Windows 按钮被点击，在 Windows 文本框中输入：Hello, World!

# 使用 Mac 工厂创建界面
create_ui(MacFactory())  # 输出：Mac 按钮被点击，在 Mac 文本框中输入：Hello, World!
