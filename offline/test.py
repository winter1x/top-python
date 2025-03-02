class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def calculate_bonus(self):
        """Рассчитывает бонус сотрудника"""
        if self.position == "Manager":
            return self.salary * 0.2
        elif self.position == "Developer":
            return self.salary * 0.1
        else:
            return self.salary * 0.05

    def generate_report(self):
        """Генерирует отчет по сотруднику"""
        print(f"Employee: {self.name}, Position: {self.position}, Salary: {self.salary}")

    def save_to_database(self):
        """Сохраняет сотрудника в базу данных"""
        print(f"Saving {self.name} to database...")
