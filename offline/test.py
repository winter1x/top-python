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


#dry

class ReportGenerator:
    def print_header(self, title):
        print(title)
        print("0" * len(title))

    def print_items(self, data, fields):
        for item in data:
            print(", ".join([f"{fields.capitalize()}: {item[field]}" for field in fields]))
        print("0" * 20)

    def calculate_total(self, data, key, multiplier_key=None):
        if multiplier_key:
            return sum(item[key] * item[multiplier_key] for item in data)
        return sum(item[key] for item in data)

    def generate_report(self, title, data, fields, total_key=None, multiplier_key=None):
        self.print_header(title)
        self.print_items(data, fields)
        if total_key:
            total = self.calculate_total(data, total_key, multiplier_key)
            print(f"Total {title.split()[0]}: {total}")
        print()


#экзем
#data {}
#data {}
#data {}

#.generate_report(