"""
factoryMethod
инкапсулирует процесс создания объекта в отдельных подклассах

струтура:
Product подукт- абстрактный класс, создаваемый объекта
ConcreteProduct конкретный продукт- классы которые наследуются от Product
Creator создатель - абстрактный класс, создает объект с помощью метода factoryMethod
ConcreteCreator конкретный создатель - классы которые наследуются от Creator. Создает конкретный продукт

+
ocp
упрощает тестирование
инкапсуляция создания объекта

-
много классов
повышение абстракции

simple factory просто функция
Abstract Factory создает несколько продуктов, определяя семейство продуктов
"""

from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass

class Truck(Transport):
    def deliver(self):
        print('Доставлено грузовиком')

class Ship(Transport):
    def deliver(self):
        print('Доставлено кораблем')

class Logistics(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        pass

    def plan_delivery(self):
        transport = self.create_transport()
        transport.deliver()

class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()

class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()

def client_code(logistics: Logistics):
    logistics.plan_delivery()

client_code(RoadLogistics())
client_code(SeaLogistics())
print('#------------------------------------------------------------------------------')


"""
factoryMethod
создание пользовательских уведомлений
типы пользователей:
гость - простые текстовые уведомления
зарегистрированный пользователь - текстовое и фото уведомления
администратор - доп метка внимание (логирование)

Notification - абстрактный класс уведомления send(message)
GuestNotification - простой текстовый уведомление
UserNotification - текстовое и фото уведомление
AdminNotification - текстовое и фото уведомление + доп метка внимание + log

User create_notification - абстрактный фабричный метод
Guest RegisteredUser Admin - реализация фабричного метода, возвращают соответсвующие уведомления

клиентский код
"""

#from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class GuestNotification(Notification):
    def send(self, message):
        print(f"Guest: {message}")

class UserNotification(Notification):
    def send(self, message):
        print(f"User: {message}")

class AdminNotification(Notification):
    log = []

    def send(self, message):
        full_message = f"Admin: внимание {message}"
        print(full_message)
        AdminNotification.log.append(full_message)

class User(ABC):
    @abstractmethod
    def create_notification(self) -> Notification:
        pass

class Guest(User):
    def create_notification(self) -> Notification:
        return GuestNotification()

class RegisteredUser(User):
    def create_notification(self) -> Notification:
        return UserNotification()

class Admin(User):
    def create_notification(self) -> Notification:
        return AdminNotification()

users = [Guest(), RegisteredUser(), Admin()]

messages = ["Привет", "Сообщение", "Внимание!"]

for user in users:
    notifier = user.create_notification()
    for message in messages:
        notifier.send(message)
        
print(AdminNotification.log)