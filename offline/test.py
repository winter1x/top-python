class Order:
    def __init__(self, order_id, customer_name, items):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items  # список товаров в заказе

    def calculate_total(self):
        """Рассчитывает общую стоимость заказа"""
        total = sum(item['price'] * item['quantity'] for item in self.items)
        return total

    def print_invoice(self):
        """Генерирует и печатает счет-фактуру"""
        print(f"Invoice for Order {self.order_id}")
        for item in self.items:
            print(f"{item['name']} - {item['quantity']} x {item['price']}")
        print(f"Total: {self.calculate_total()}")

    def save_to_database(self):
        """Сохраняет заказ в базу данных"""
        print(f"Saving order {self.order_id} to database...")
