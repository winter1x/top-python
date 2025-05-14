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

class DiscountStrategy:
    def calculate(self, amount):
        return amount

    
class RegularDiscount(DiscountStrategy):
    def calculate(self, amount):
        return amount * 0.95

class VipDiscount(DiscountStrategy):
    def calculate(self, amount):
        return amount * 0.9

class EmployeeDiscount(DiscountStrategy):
    def calculate(self, amount):
        return amount * 0.85

class DiscountCalculator:
    def __init__(self, discount_strategy):
        self.discount_strategy = discount_strategy

    def calculate_discount(self, amount):
        return self.discount_strategy.calculate(amount)
    

vip = VipDiscount()
calc = DiscountCalculator(vip)
print(calc.calculate_discount(100))

employee = EmployeeDiscount()
calc = DiscountCalculator(employee)
print(calc.calculate_discount(100))

def get_discount_strategy(customer_type: str) -> DiscountStrategy:
    strategies = {
        'regular': RegularDiscount(),
        'vip': VipDiscount(),
        'employee': EmployeeDiscount(),
        'guest': DiscountStrategy(),
    }
    return strategies.get(customer_type, DiscountStrategy())

class StudentDiscount(DiscountStrategy):
    def calculate(self, amount):
        return amount * 0.9
        
