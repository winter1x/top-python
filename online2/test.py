"""
Что вы выигрываете, используя полиморфизм здесь?
Какой код вы будете менять, если появится новый тип покупателя?
как это связано с o принципом?
почему такой подход лучше при работе в команде?
"""
class DiscountCalculator:
    def calculate(self, customer_type, amount):
        if customer_type == 'vip':
            return amount * 0.9
        elif customer_type == 'regular':
            return amount * 0.95
        elif customer_type == 'guest':
            return amount * 0.98
        else:
            return amount
