import PyQt5.QtDesigner

import pickle

#data = {'name': "alice", 'age': 24, 'city': 'new york'}

class Person:
    health = 100
    @classmethod
    def print_health(cls):
        print(cls.health)

    def __init__(self, name, age, is_student=False):
        self.name = name
        self.age = age
        self.is_student = is_student
        self.__gender = None

    def invert_is_student(self):
        self.is_student = not self.is_student

    @staticmethod
    def to_learn():
        print('im learning')

    def __str__(self):
        return f"Person name={self.name}, age={self.age}"

person = Person("alice", 24)

with open('person.pkl', 'wb') as file:
    pickle.dump(person, file)

with open('person.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)

"""
Задание 1
Есть некоторый словарь, который хранит названия
стран и столиц. Название страны используется в качестве
ключа, название столицы в качестве значения. Необходимо
реализовать: добавление данных, удаление данных, поиск
данных, редактирование данных, сохранение и загрузку
данных (используя упаковку и распаковку).
"""

class CountryCapitalDatabase:
    def __init__(self, filename="data.pkl"):
        pass

    def add_country(self, country, capital):
        pass

    def search_country(self, country):
        pass

    def edit_country(self, country, new_capital):
        pass

    def load_data(self):
        pass

    def display_data(self):
        pass

    def remove_country(self, country):
        pass

    def save_data(self):
        pass

    def search_country(self, country):
        pass

db = CountryCapitalDatabase()

db.add_country('Россия', "Москва")
db.add_country('Россия2', "Москва")
db.display_data()

db.edit_country('Россия2', "Москва2")
db.display_data()

db.remove_country('Россия2')
db.display_data()

db.search_country('Россия')
db.search_country('Россия2')

db.save_data()
"""
Задание 2
Есть некоторый словарь, который хранит названия
музыкальных групп(исполнителей) и альбомов. Название группы используется в качестве ключа, название
альбомов в качестве значения. Необходимо реализовать:
добавление данных, удаление данных, поиск данных,
редактирование данных, сохранение и загрузку данных
(используя упаковку и распаковку)."""

import random
a = tuple([{"1": "13"}, ])
print(a)
print(random.sample(list({"ключ": "значение",
                          'b': 2,
                          "c": 3}
                         .keys()), 2))