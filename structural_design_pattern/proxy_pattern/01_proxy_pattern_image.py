"""
代理模式（Proxy Pattern）是一种结构型设计模式，它允许你通过创建一个代理对象来控制对另一个对象（即真实对象）的访问。代理对象充当了真实对象的接口，客户端与代理对象交互，而不是直接与真实对象交互。代理模式可以在不改变真实对象的情况下，对其功能进行增强或控制，比如进行访问控制、延迟加载、日志记录等。
"""


# 抽象主题类
class Image:
    def display(self):
        pass


# 真实主题类
class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load_from_disk()

    def load_from_disk(self):
        print(f"Loading {self.filename}")

    def display(self):
        print(f"Displaying {self.filename}")


# 代理类
class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()


# 客户端代码
if __name__ == "__main__":
    image = ProxyImage("test.jpg")

    # 第一次调用，会加载图片
    image.display()

    # 第二次调用，不会再次加载图片
    image.display()
