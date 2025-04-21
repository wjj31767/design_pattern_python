"""
桥接模式适用于存在 两个独立变化维度 的场景，以下是几个典型且实用的扩展场景，结合具体场景说明抽象与实现的分离逻辑：
1. 图形渲染系统（形状 vs 渲染方式）
场景描述
设计一个支持多种形状（圆形、方形、三角形）和多种渲染风格（2D 渲染、3D 渲染、黑白渲染）的图形系统，要求两者可独立扩展。
抽象与实现分离
抽象部分（形状）：定义 Shape 抽象类，包含绘制逻辑，但不关心具体渲染方式。
"""


class Shape:
    def __init__(self, renderer):
        self.renderer = renderer  # 桥接渲染器

    def draw(self):
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius, renderer):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        print(f"绘制圆形（半径={self.radius}）：", end="")
        self.renderer.render_circle(self.radius)


class Renderer:
    def render_circle(self, radius):
        raise NotImplementedError


class Renderer2D(Renderer):
    def render_circle(self, radius):
        print(f"2D 渲染，半径={radius}")


class Renderer3D(Renderer):
    def render_circle(self, radius):
        print(f"3D 渲染，半径={radius}（带阴影）")