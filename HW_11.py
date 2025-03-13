class Car:
    def __init__(self, model, year, manufacturer, engine_volume, color, price):
        self.__model = model
        self.__year = year
        self.__manufacturer = manufacturer
        self.__engine_volume = engine_volume
        self.__color = color
        self.__price = price

    def display_info(self):
        print(f"Модель: {self.__model},\nГод: {self.__year},\nПроизводитель: {self.__manufacturer},\nОбъем двигателя: {self.__engine_volume} л,\nЦвет: {self.__color},\nЦена: {self.__price} руб.")

    def get_price(self):
        return self.__price
        
    def set_price(self, new_price):
        if new_price >= 2000000:
            self.__price = new_price
        else: 
            print("\nНе дешевле 2кк")



car = Car("Toyota Supra", 2002, "Toyota", 3, "Черный", 3000000)
car.display_info()
car.set_price(1000000)
print(f"\nОбновленная цена: {car.get_price()} руб.\n")


class Book:
    def __init__(self, title, year, publisher, genre, author, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def display_info(self):
        print(f"Название: {self.title},\nГод: {self.year},\nИздатель: {self.publisher},\nЖанр: {self.genre},\nАвтор: {self.author},\nЦена: {self.price} руб.")

    def set_price(self, new_price):
        self.price = new_price

    def get_price(self):
        return self.price

book1 = Book("Война и мир", 1869, "Русский вестник", "Роман", "Лев Толстой", 1500)
book1.display_info()
book1.set_price(1300)
print(f"\nОбновленная цена: {book1.get_price()} руб.\n")


class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.__name = name
        self.__opening_date = opening_date
        self.__country = country
        self.__city = city
        self.__capacity = capacity

    def display_info(self):
        print(f"Стадион: {self.__name},\nДата открытия: {self.__opening_date},\nСтрана: {self.__country},\nГород: {self.__city},\nВместимость: {self.__capacity} человек")

    def set_capacity(self, new_capacity):
        if 40000 < new_capacity < 90000:
            self.__capacity = new_capacity

    def get_capacity(self):
        return self.__capacity


stadium1 = Stadium("Лужники", "31 июля 1956", "Россия", "Москва", 81000)
stadium1.display_info()
stadium1.set_capacity(85000)
print(f"\nОбновленная вместимость: {stadium1.get_capacity()} человек.")
