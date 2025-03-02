class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def calculate_bonus(self):
        if self.position == "Manager":
            return self.salary * 0.2
        elif self.position == "Developer":
            return self.salary * 0.1
        else:
            return self.salary * 0.05

    def generate_report(self):
        print(f"Employee: {self.name}, Position: {self.position}, Salary: {self.salary}")

    def save_to_database(self):
        print(f"Saving {self.name} to database...")

class HRSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def process_salaries(self):
        for emp in self.employees:
            print(f"Processing salary for {emp.name}: {emp.salary}")

    def send_salary_notifications(self):
        for emp in self.employees:
            print(f"Sending notification to {emp.name} about salary payment.")
