"""
这个示例通过建造者模式实现了两种不同类型汽车（跑车和 SUV）的构建过程：
产品类（Car）：定义了汽车的具体部件（引擎、座椅、轮胎、颜色）
抽象建造者（CarBuilder）：声明了构建各部件的接口方法
具体建造者（SportsCarBuilder/SUVBuilder）：实现了具体车型的部件构建逻辑
导演类（Director）：定义了标准化的构建流程，可以复用相同的构建逻辑创建不同表示的产品
运行结果会输出两辆不同配置的汽车：
建造者模式的核心优势在于：
将复杂对象的构建过程分解为多个步骤，方便扩展新的产品类型
分离了构建算法（导演类）和具体实现（建造者），符合开闭原则
可以精细控制对象的构建过程，允许客户端自定义构建步骤顺序
"""


class Car:
    """产品类：具体的汽车对象"""

    def __init__(self):
        self.engine = None
        self.seats = None
        self.wheels = None
        self.color = None

    def __str__(self):
        return (f"Car: Engine={self.engine}, Seats={self.seats}, "
                f"Wheels={self.wheels}, Color={self.color}")


class CarBuilder:
    """抽象建造者: 定义构建步骤的接口"""

    def __init__(self):
        self.car = Car()

    def build_engine(self):
        raise NotImplementedError

    def build_seats(self):
        raise NotImplementedError

    def build_wheels(self):
        raise NotImplementedError

    def build_color(self):
        raise NotImplementedError

    def get_result(self):
        return self.car


class SportsCarBuilder(CarBuilder):
    """具体建造者:构建跑车"""

    def build_engine(self):
        self.car.engine = "V8 Turbo"
        return self

    def build_seats(self):
        self.car.seats = "Leather Sports Seats (2)"
        return self

    def build_wheels(self):
        self.car.wheels = "20-inch Alloy Wheels"
        return self

    def build_color(self):
        self.car.color = "Red"
        return self


class SUVBuilder(CarBuilder):
    """具体建造者：构建SUV"""

    def build_engine(self):
        self.car.engine = "V6 Hybrid"
        return self

    def build_seats(self):
        self.car.seats = "Cloth Seats (7)"
        return self

    def build_wheels(self):
        self.car.wheels = "18-inch Off-Road Wheels"
        return self

    def build_color(self):
        self.car.color = "Black"
        return self


class Director:
    """导演类：指导建造过程"""

    @staticmethod
    def construct_sports_car(builder):
        return (builder.build_engine()
                .build_seats()
                .build_wheels()
                .build_color()
                .get_result())

    @staticmethod
    def construct_suv(builder):
        return (builder.build_engine()
                .build_seats()
                .build_wheels()
                .build_color()
                .get_result())


if __name__ == '__main__':
    sports_car_builder = SportsCarBuilder()
    sports_car = Director.construct_sports_car(sports_car_builder)
    print(sports_car)
    suv_builder = SUVBuilder()
    suv = Director.construct_suv(suv_builder)
    print(suv)
