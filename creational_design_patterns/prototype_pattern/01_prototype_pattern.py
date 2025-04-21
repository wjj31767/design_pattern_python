"""
代码说明：
抽象原型类（Prototype）
定义了 clone() 接口，要求所有具体原型类必须实现对象克隆功能。
具体原型类（Circle/Square）
实现 clone() 方法，使用 copy.deepcopy() 进行深拷贝，确保克隆对象与原型对象的属性相互独立。
包含具体业务属性（如半径、边长、颜色），克隆时这些属性会被完整复制。
客户端逻辑
通过原型对象的 clone() 方法创建新对象，避免重复执行构造函数和初始化逻辑。
修改克隆对象的属性后，原始对象不受影响，验证了深拷贝的独立性。
原型模式核心特点：
通过复制现有对象创建新对象，而非通过构造函数新建，适用于对象初始化成本较高的场景（如复杂配置或数据加载）。
支持深拷贝和浅拷贝：深拷贝（deepcopy）复制对象及其嵌套对象，浅拷贝（copy）仅复制顶层对象引用（示例中使用深拷贝确保属性独立）。
减少子类化：无需为每个产品类型创建工厂类，直接通过原型实例克隆，简化对象创建逻辑。
适用场景：
对象创建成本高（如需要读取配置文件、数据库连接等），且现有对象可作为模板重复使用时。
需要快速生成大量相似对象（如游戏中的角色副本、文档中的段落复制）。
避免构造函数的复杂性，直接通过已有对象状态生成新对象。
"""
import copy

# 抽象原型类
class Prototype:
    def clone(self):
        raise NotImplementedError("克隆方法未实现")

# 具体原型类：圆形
class Circle(Prototype):
    def __init__(self, radius=1.0, color="red"):
        self.radius = radius
        self.color = color

    def clone(self):
        # 使用深拷贝确保属性独立
        return copy.deepcopy(self)

    def __str__(self):
        return f"Circle(radius={self.radius}, color={self.color})"

# 具体原型类：正方形
class Square(Prototype):
    def __init__(self, side_length=1.0, color="blue"):
        self.side_length = side_length
        self.color = color

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Square(side_length={self.side_length}, color={self.color})"

# 客户端代码
if __name__ == "__main__":
    # 创建原型实例
    original_circle = Circle(radius=2.0, color="green")
    original_square = Square(side_length=3.0, color="yellow")

    # 克隆对象
    cloned_circle = original_circle.clone()
    cloned_square = original_square.clone()

    # 修改克隆对象的属性（验证独立性）
    cloned_circle.radius = 2.5
    cloned_square.side_length = 3.5

    # 输出结果
    print("原始圆形:", original_circle)
    print("克隆圆形:", cloned_circle)
    print("原始正方形:", original_square)
    print("克隆正方形:", cloned_square)