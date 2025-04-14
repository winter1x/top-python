"""
реализовать систему управления транспортом, подумать над общими и уникальными методами/атрибутами, использовать наследование

Transport

Car
Bike
"""
class Transport:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        print(f"движемся {self.speed} ", end='')

class Car(Transport):
    def __init__(self, speed, engine):
        super().__init__(speed)
        self.engine = engine

    def move(self):
        super().move()
        print(f"с {self.engine}")

class Bike(Transport):
    def __init__(self, speed, pedals):
        super().__init__(speed)
        self.pedals = pedals

    def move(self):
        super().move()
        print(f"с {self.pedals}")


car = Car(100, 'v6')
bike = Bike(120, 'standart pedals')

car.move()
bike.move()