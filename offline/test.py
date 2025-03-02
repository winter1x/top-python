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
