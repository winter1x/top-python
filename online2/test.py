"""
Наследование, super()
миксин в отдельном классе

базовый Employee
атрибуты
name
salary

get_info()
calculate_bonus()

Manager от Employee
departament
calculate_bonus()
get_info()


Developer от Employee
programming_language
get_info()

миксин
send_email - выводит - для Manager Developer

Intern от Developer
calculate_bonus()
get_info()

"""

#миксин
class EmailMixin:
    def send_email(self, message):
        print(f"отправлено сообщение сотруднику {self.name}: {message}")

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_info(self):
        print(f"имя {self.name}")
        print(f"должность: сотрудник")

    def calculate_bonus(self):
        return self.salary * 0.10

class Manager(EmailMixin, Employee):
    def __init__(self, name, salary, departament):
        super().__init__(name, salary)
        self.departament = departament

    def get_info(self):
        super().get_info()
        print('должность: менеджер')
        print(f'отдел: {self.departament}')

    def calculate_bonus(self):
        return self.salary * 0.20

class Developer(EmailMixin, Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def get_info(self):
        super().get_info()
        print('должность: разработчик')
        print(f'язык: {self.programming_language}')

class Intern(Developer):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary, programming_language)

    def get_info(self):
        super().get_info()
        print('должность: стажер')

    def calculate_bonus(self):
        return 0

manager = Manager('анна', 100, "it")
developer = Developer('анна2', 1002, "it2")
intern = Intern('анна23', 10023, "it23")

manager.get_info()
manager.send_email('совещание')

intern.get_info()