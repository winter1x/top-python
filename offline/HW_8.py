import json
import os


class Employee:
    def __init__(self, first_name, last_name, age, position):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.position = position

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "position": self.position
        }

    @staticmethod
    def from_dict(data):
        return Employee(data["first_name"], data["last_name"], data["age"], data["position"])


class EmployeeManagementSystem:
    def __init__(self, filename="employees.json"):
        self.filename = filename
        self.employees = self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as file:
                try:
                    return [Employee.from_dict(emp) for emp in json.load(file)]
                except json.JSONDecodeError:
                    return []
        return []

    def save_data(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump([emp.to_dict() for emp in self.employees], file, indent=4, ensure_ascii=False)

    def add_employee(self, first_name, last_name, age, position):
        self.employees.append(Employee(first_name, last_name, age, position))
        self.save_data()

    def edit_employee(self, last_name, new_data):
        for emp in self.employees:
            if emp.last_name == last_name:
                emp.first_name = new_data.get("first_name", emp.first_name)
                emp.age = new_data.get("age", emp.age)
                emp.position = new_data.get("position", emp.position)
                self.save_data()
                return True
        return False

    def delete_employee(self, last_name):
        self.employees = [emp for emp in self.employees if emp.last_name != last_name]
        self.save_data()

    def search_by_last_name(self, last_name):
        return [emp.to_dict() for emp in self.employees if emp.last_name == last_name]

    def filter_by_age_or_letter(self, age=None, letter=None):
        return [emp.to_dict() for emp in self.employees if
                (age and emp.age == age) or (letter and emp.last_name.startswith(letter))]

    def display_employees(self):
        return [emp.to_dict() for emp in self.employees]



def main():
    system = EmployeeManagementSystem()
    while True:
        print("\nМеню:")
        print("1. Добавить сотрудника")
        print("2. Редактировать сотрудника")
        print("3. Удалить сотрудника")
        print("4. Поиск сотрудника по фамилии")
        print("5. Вывести всех сотрудников")
        print("6. Фильтр по возрасту или букве фамилии")
        print("7. Выйти (данные сохраняются автоматически)")

        choice = input("Выберите действие: ")
        if choice == "1":
            first_name = input("Имя: ")
            last_name = input("Фамилия: ")
            age = int(input("Возраст: "))
            position = input("Должность: ")
            system.add_employee(first_name, last_name, age, position)
            print("Сотрудник добавлен.")
        elif choice == "2":
            last_name = input("Введите фамилию сотрудника для редактирования: ")
            new_data = {}
            new_first_name = input("Новое имя (оставьте пустым для пропуска): ")
            if new_first_name:
                new_data["first_name"] = new_first_name
            new_age = input("Новый возраст (оставьте пустым для пропуска): ")
            if new_age:
                new_data["age"] = int(new_age)
            new_position = input("Новая должность (оставьте пустым для пропуска): ")
            if new_position:
                new_data["position"] = new_position
            if system.edit_employee(last_name, new_data):
                print("Сотрудник обновлен.")
            else:
                print("Сотрудник не найден.")
        elif choice == "3":
            last_name = input("Введите фамилию сотрудника для удаления: ")
            system.delete_employee(last_name)
            print("Сотрудник удален.")
        elif choice == "4":
            last_name = input("Введите фамилию: ")
            results = system.search_by_last_name(last_name)
            print(results if results else "Сотрудник не найден.")
        elif choice == "5":
            print(system.display_employees())
        elif choice == "6":
            age = input("Введите возраст (оставьте пустым для поиска по букве фамилии): ")
            age = int(age) if age else None
            letter = input("Введите начальную букву фамилии (оставьте пустым для поиска по возрасту): ")
            results = system.filter_by_age_or_letter(age, letter)
            print(results if results else "Совпадений не найдено.")
        elif choice == "7":
            print("Выход. Данные сохранены.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()
