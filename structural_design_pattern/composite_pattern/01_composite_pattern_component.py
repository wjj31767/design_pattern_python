"""
组合模式是一种结构型设计模式，它允许你将对象组合成树形结构以表示 “部分 - 整体” 的层次结构。下面是一个简单的组合模式的 Python 代码示例：
"""
from abc import ABC, abstractmethod


# 抽象组件类
class Component(ABC):
    @abstractmethod
    def operation(self):
        pass


# 叶子节点类
class Leaf(Component):
    def __init__(self, name):
        self.name = name

    def operation(self):
        return f"Leaf {self.name} operation"


# 组合节点类
class Composite(Component):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def operation(self):
        results = [child.operation() for child in self.children]
        return f"Composite {self.name} operation: {', '.join(results)}"


# 客户端代码
if __name__ == "__main__":
    # 创建叶子节点
    leaf1 = Leaf("Leaf1")
    leaf2 = Leaf("Leaf2")

    # 创建组合节点
    composite1 = Composite("Composite1")
    composite1.add(leaf1)
    composite1.add(leaf2)

    leaf3 = Leaf("Leaf3")
    composite2 = Composite("Composite2")
    composite2.add(leaf3)
    composite2.add(composite1)

    # 执行操作
    print(composite2.operation())