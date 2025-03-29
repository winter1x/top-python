"""
гибкого выбора алгоритмов
"""
"""
когда используем (+)

несколько вариантов алгоритма
алгоритмы могут меняться, динамически
без дублирования кода
передавать алгоритм как параметр
"""

"""
когда не используем (-)
статическое переключение алгоритмов

"""
"""
структура

context
strategy interface
concrete strategies
"""

from abc import ABC, abstractmethod

"""
фикс
в зависимости от суммы заказа
для vip
"""

#strategy interface
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, total_amount: float) -> float:
        pass
#concrete strategies
class PercentageDiscount(DiscountStrategy):
    def apply_discount(self, total_amount: float) -> float:
        if total_amount > 1000:
            return total_amount * 0.95

class VipDiscount(DiscountStrategy):
    def apply_discount(self, total_amount: float) -> float:
        return total_amount * 0.85

class FixedDiscount(DiscountStrategy):
    def apply_discount(self, total_amount: float) -> float:
        return total_amount * 0.9
#context
class Order:
    def __init__(self, total_amount: float, discount_strategy: DiscountStrategy):
        self.total_amount = total_amount
        self.discount_strategy = discount_strategy

    def get_final_price(self) -> float:
        return self.discount_strategy.apply_discount(self.total_amount)

order1 = Order(1200, FixedDiscount())
order2 = Order(1200, PercentageDiscount())
order3 = Order(1200, VipDiscount())

print(order1.get_final_price())
print(order2.get_final_price())
print(order3.get_final_price())


"""
def ......(amount)
    :return скидка
"""