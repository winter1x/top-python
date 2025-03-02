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

#solid

from abc import ABC, abstractmethod

#s
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

#o
class BonusCalculator(ABC):
    @abstractmethod
    def calculate_bonus(self, salary):
        pass

class ManagerBonus(BonusCalculator):
    def calculate_bonus(self, salary):
        return salary * 0.2

class DeveloperBonus(BonusCalculator):
    def calculate_bonus(self, salary):
        return  salary * 0.05

#l

#i
class ReportGenerator:
    @staticmethod
    def generate_report(employee):
        print(f"Employee: {employee.name}, Position: {employee.position}, Salary: {employee.salary}")

class DatabaseSaver:
    @staticmethod
    def save_to_database(employee):
        print(f"saving {employee.name} to db")

#d

class HRSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee, bonus_calculator):
        self.employees.append((employee, bonus_calculator))

    def process_salaries(self):
        for emp, bonus_calc in self.employees:
            bonus = bonus_calc.calculate_bonus(emp.salary)
            print(f"processing salary for {emp.name}: Base {emp.salary}, Bonus {bonus}")

    def send_salary_notification(self):
        for emp, _ in self.employees:
            print(f"Sending notification to {emp.name} s p")

