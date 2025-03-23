"""
работаем с разными типами уведомлений mail, sms. Система отправляет уведомления. Abstract factory
"""
from abc import ABC, abstractmethod

class NotificationSender(ABC):
    @abstractmethod
    def send_notification(self, message: str):
        pass

class EmailSender(NotificationSender):
    def send_notification(self, message: str):
        print(f"отправка email {message}")

class SMSSender(NotificationSender):
    def send_notification(self, message: str):
        print(f"отправка sms {message}")

class NotificationFactory(ABC):
    @abstractmethod
    def create_sender(self) -> NotificationSender:
        pass

class EmailNotificationFactiory(NotificationFactory):
    def create_sender(self) -> NotificationSender:
        return EmailSender()

class SMSNotificationFactiory(NotificationFactory):
    def create_sender(self) -> NotificationSender:
        return SMSSender()

def send_alert(factory: NotificationFactory, message: str):
    sender = factory.create_sender()
    sender.send_notification(message)


factory = EmailNotificationFactiory() #SMSNotificationFactiory()
send_alert(factory, "тестовое уведомление")
