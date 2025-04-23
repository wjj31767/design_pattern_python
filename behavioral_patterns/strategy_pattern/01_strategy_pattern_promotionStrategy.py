"""
策略模式（Strategy Pattern）是一种行为型设计模式，它定义了一系列的算法，并将每个算法封装起来，使它们可以相互替换。策略模式让算法的变化独立于使用算法的客户端。通过使用策略模式，你可以在运行时根据需要选择不同的算法，而不需要修改客户端的代码。
"""
from abc import ABC, abstractmethod

# 抽象策略类
class PromotionStrategy(ABC):
    @abstractmethod
    def discount(self, price):
        pass

# 具体策略类：无折扣
class NoDiscount(PromotionStrategy):
    def discount(self, price):
        return price

# 具体策略类：八折优惠
class TwentyPercentDiscount(PromotionStrategy):
    def discount(self, price):
        return price * 0.8

# 具体策略类：满 200 减 50
class FiftyOffTwoHundred(PromotionStrategy):
    def discount(self, price):
        if price >= 200:
            return price - 50
        return price

# 上下文类
class ShoppingCart:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def checkout(self, price):
        return self.strategy.discount(price)


# 客户端代码
if __name__ == "__main__":
    # 无折扣策略
    cart = ShoppingCart(NoDiscount())
    total_price = 300
    final_price = cart.checkout(total_price)
    print(f"无折扣时，总价 {total_price} 元，最终需支付 {final_price} 元")

    # 八折优惠策略
    cart.set_strategy(TwentyPercentDiscount())
    final_price = cart.checkout(total_price)
    print(f"八折优惠时，总价 {total_price} 元，最终需支付 {final_price} 元")

    # 满 200 减 50 策略
    cart.set_strategy(FiftyOffTwoHundred())
    final_price = cart.checkout(total_price)
    print(f"满 200 减 50 时，总价 {total_price} 元，最终需支付 {final_price} 元")
