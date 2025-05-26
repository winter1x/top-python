"""
структура

subject - интерфейс - издатель - уведомляет observers при изменении своего состояния
observers- подписчики - update() - вызывается при получении уведомления
"""
"""
+
отделяет subject observers
можно добавлять observers
нет жесткой зависимости между классами
расширяемость
"""
"""
-
производительность при большом количестве подписчиков
подписчики должны правильно удаляться
"""

#import logging
"""class NewsChannel:
    def __init__(self):
        self.news = ''

    def publish_news(self, news):
        self.news = news
        self.notify_users()

    def notify_users(self):
        print(f"новость {self.news}")

channel = NewsChannel()
channel.publish_news('new')"""

from abc import ABC, abstractmethod
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

class User(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f'{self.name} получил уведомление {message}')

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

class NewsChannel(Subject):
    def __init__(self):
        self.subscribers = []
        self.news = ''

    def attach(self, observer):
        self.subscribers.append(observer)

    def detach(self, observer):
        self.subscribers.remove(observer)

    def notify(self):
        for subscriber in self.subscribers:
            subscriber.update(self.news)

    def publish_news(self, news):
        self.news = news
        self.notify()

channel1 = NewsChannel()
user1 = User('alise')
user2 = User('matvey')

channel1.attach(user1)
channel1.attach(user2)

channel1.publish_news('new')