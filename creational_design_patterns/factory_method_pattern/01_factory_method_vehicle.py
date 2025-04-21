"""
这个示例完整展示了工厂方法模式的核心结构：
产品体系：定义了统一接口Vehicle，具体产品（汽车 / 自行车 / 飞机）实现该接口
工厂体系：抽象工厂VehicleFactory声明创建接口，具体工厂（汽车工厂 / 自行车工厂 / 飞机工厂）实现具体创建逻辑
客户端调用：通过具体工厂创建对应产品，无需知道产品具体实现类
模式优势：
解耦对象创建：客户端只需依赖抽象工厂和抽象产品，无需关心具体类
易于扩展：新增产品时只需添加新的具体产品和具体工厂，符合开闭原则
统一接口：所有产品遵循相同接口，客户端可以一致地处理不同产品
典型应用场景：
日志系统（根据配置创建不同日志处理器）
数据库访问（根据数据库类型创建不同连接对象）
跨平台开发（根据操作系统创建不同的界面组件）
"""


class Vehicle:
    """所有交通工具的抽象基类"""

    def run(self):
        raise NotImplementedError("子类必须实现run方法")


class Car(Vehicle):
    def run(self):
        return "汽车以60km/h速度行驶"


class Bike(Vehicle):
    def run(self):
        return "自行车以20km/h速度骑行"


class Airplane(Vehicle):
    def run(self):
        return "飞机以800km/h速度飞行"


class VehicleFactory:
    """创建交通工具的抽象工厂"""

    def create_vehicle(self):
        raise NotImplementedError("子类必须实现create_vehicle方法")


# 具体工厂（Concrete Factories）
class CarFactory(VehicleFactory):
    def create_vehicle(self):
        return Car()


class BikeFactory(VehicleFactory):
    def create_vehicle(self):
        return Bike()


class AirplaneFactory(VehicleFactory):
    def create_vehicle(self):
        return Airplane()


# 客户端使用
if __name__ == '__main__':
    # 通过具体工厂创建产品
    car_factory = CarFactory()
    car = car_factory.create_vehicle()
    print(car.run())
    bike_factory = BikeFactory()
    bike = bike_factory.create_vehicle()
    print(bike.run())
    airplane_factory = AirplaneFactory()
    airplane = airplane_factory.create_vehicle()
    print(airplane.run())
   