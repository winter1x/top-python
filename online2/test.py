"""
обычные 5%
постоянные 10%
VIP 20% скидки

сумму заказа, тип клиента
"""
#пример кода с нарушением dry
def calculate_regular_price(price):
    discount = price * 0.05
    return price - discount

def calculate_loyal_price(price):
    discount = price * 0.10
    return price - discount
    
def calculate_vip_price(price):
    discount = price * 0.20
    return price - discount

print(calculate_regular_price(100))
print(calculate_loyal_price(100))
print(calculate_vip_price(100))