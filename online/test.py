"""
observer
издатель хранит температуру WeatherStation
MobileApp Website - подписчики
"""

from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, temperature):
        pass

class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass

class WeatherStation(Subject):
    def __init__(self):
        self.subscribers = []
        self.temperature = 0

    def attach(self, observer):
        self.subscribers.append(observer)

    def detach(self, observer):
        self.subscribers.remove(observer)

    def notify(self):
        for subscriber in self.subscribers:
            subscriber.update(self.temperature)

    def set_temperature(self, temperature):
        print(f"новая температура {temperature}")
        self.temperature = temperature
        self.notify()

class MobileApp(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, temperature):
        print(f"{self.name} получил уведомление {temperature}")

class Website(Observer):
    def update(self, temperature):
        print(f'сайт обновил {temperature}')

weather_station = WeatherStation()

mobile_app1 = MobileApp('приложение 1')
mobile_app2 = MobileApp('приложение 2')
website = Website()

weather_station.attach(mobile_app1)
weather_station.attach(mobile_app2)
weather_station.attach(website)

weather_station.set_temperature(25)
weather_station.set_temperature(30)

weather_station.detach(mobile_app1)

weather_station.set_temperature(20)