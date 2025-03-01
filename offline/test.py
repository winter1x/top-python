class ReportGenerator:
    def generate_sales_report(self, data):
        total = 0
        for item in data:
            total += item['price'] * item['quantity']
        print("Sales Report")
        print("------------")
        for item in data:
            print(
                f"Product: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}, Total: {item['price'] * item['quantity']}")
        print("------------")
        print(f"Total Sales: {total}")

    def generate_inventory_report(self, data):
        print("Inventory Report")
        print("---------------")
        for item in data:
            print(f"Product: {item['name']}, Quantity: {item['quantity']}")
        print("---------------")

    def generate_expense_report(self, data):
        total_expense = 0
        for expense in data:
            total_expense += expense['amount']
        print("Expense Report")
        print("--------------")
        for expense in data:
            print(f"Category: {expense['category']}, Amount: {expense['amount']}")
        print("--------------")
        print(f"Total Expenses: {total_expense}")
