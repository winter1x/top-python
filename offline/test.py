class Employer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Print(self):
        print("this is employer class")

    def __str__(self):
        return f"Employee: {self.name}, Age: {self.age}"

    def __int__(self):
        return self.age

class President(Employer):
    def Print(self):
        print("pres")

    def __str__(self):
        return f"President: {self.name}, Age: {self.age}"

class Manager(Employer):
    def Print(self):
        print("mana")

    def __str__(self):
        return f"Manager: {self.name}, Age: {self.age}"

class Worker(Employer):
    def Print(self):
        print("Worker")

    def __str__(self):
        return f"Worker: {self.name}, Age: {self.age}"

employees = [
    President('a', 50),
    Manager('b', 40),
    Worker("c", 30)
]

for employee in employees:
    employee.Print()
    print(employee)
    print(f"Age as integer: {int(employee)}\n")