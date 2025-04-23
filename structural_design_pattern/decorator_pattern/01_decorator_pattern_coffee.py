"""
装饰器模式（Decorator Pattern）是一种结构型设计模式，它允许向一个现有的对象添加新的功能，同时又不改变其结构。这种模式创建了一个装饰类，用来包装原有的类，并在保持类方法签名完整性的前提下，提供了额外的功能。装饰器模式以对客户端透明的方式扩展对象的功能，是继承关系的一个替代方案。通过使用不同的具体装饰器类及这些装饰器类的排列组合，可以创造出很多不同行为的组合。
"""
from abc import ABC, abstractmethod

# 抽象组件类
class Coffee(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def cost(self):
        pass

# 具体组件类
class SimpleCoffee(Coffee):
    def get_description(self):
        return "Simple Coffee"

    def cost(self):
        return 2.0

# 抽象装饰器类
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee

    def get_description(self):
        return self.coffee.get_description()

    def cost(self):
        return self.coffee.cost()

# 具体装饰器类：添加牛奶
class Milk(CoffeeDecorator):
    def get_description(self):
        return self.coffee.get_description() + ", Milk"

    def cost(self):
        return self.coffee.cost() + 0.5

# 具体装饰器类：添加糖
class Sugar(CoffeeDecorator):
    def get_description(self):
        return self.coffee.get_description() + ", Sugar"

    def cost(self):
        return self.coffee.cost() + 0.2

# 客户端代码
if __name__ == "__main__":
    coffee = SimpleCoffee()
    print(f"{coffee.get_description()}: ${coffee.cost()}")

    coffee_with_milk = Milk(coffee)
    print(f"{coffee_with_milk.get_description()}: ${coffee_with_milk.cost()}")

    coffee_with_milk_and_sugar = Sugar(coffee_with_milk)
    print(f"{coffee_with_milk_and_sugar.get_description()}: ${coffee_with_milk_and_sugar.cost()}")