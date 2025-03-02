class DiscountCalculator:
    def calculate_discount(self, order_amount, customer_type):
        """Рассчитывает скидку в зависимости от типа клиента"""
        if customer_type == "Regular":
            return order_amount * 0.05  # 5% скидка
        elif customer_type == "VIP":
            return order_amount * 0.1  # 10% скидка
        elif customer_type == "New":
            return order_amount * 0.02  # 2% скидка
        else:
            return 0  # Без скидки

#o
from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, order_amount):
        pass

class RegularCustomerDiscount(DiscountStrategy):
    def calculate(self, order_amount):
        return order_amount * 0.05

class VIPCustomerDiscount(DiscountStrategy):
    def calculate(self, order_amount):
        return order_amount * 0.1

class NewCustomerDiscount(DiscountStrategy):
    def calculate(self, order_amount):
        return order_amount * 0.02

class NoDiscount(DiscountStrategy):
    def calculate(self, order_amount):
        return 0

class DiscountCalculator:
    def __init__(self, discount_strategy: DiscountStrategy):
        self.discount_strategy = discount_strategy

    def calculate_discount(self, order_amount):
        return self.discount_strategy.calculate(order_amount)