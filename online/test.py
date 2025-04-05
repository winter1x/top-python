"""
mediator
реализовать чат

разные роли + модерация сообщений:

user - может отправлять сообщения
moderator - может удалять
admin - может блокировать пользователей

ChatRoom управляет всеми пользователями и сообщениями

модерация сообщений:
ban_word_list = ['слово', "еще"]
"""
from abc import ABC, abstractmethod

class ChatMediator(ABC):
    @abstractmethod
    def send_message(self, message, sender):
        pass

    @abstractmethod
    def remove_message(self, message, moderator):
        pass

    @abstractmethod
    def block_user(self, user, admin):
        pass

class ChatRoom(ChatMediator):
    def __init__(self):
        self.users = []
        self.banned_users = set()
        self.messages = []
        self.ban_word_list = {"спам", "оскорбление"}

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, message, sender):
        if sender in self.banned_users:
            print(f"{sender.name} заблокирован и не может отправлять сообщения.")
            return

        if any(word in message.lower() for word in self.ban_word_list):
            print(f"Сообщение от {sender.name} содержит запрещенные слова и не отправлено.")
            return

        self.messages.append((sender, message))
        for user in self.users:
            if user != sender:
                user.receive_message(message, sender)

    def remove_message(self, message, moderator):
        for msg in self.messages:
            if msg[1] == message:
                self.messages.remove(msg)
                print(f"Модератор {moderator.name} удалил сообщение: {message}")
                return
        print(f"Сообщение не найдено.")

    def block_user(self, user, admin):
        self.banned_users.add(user)
        print(f"Админ {admin.name} заблокировал пользователя {user.name}.")

class User(ABC):
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator
        mediator.add_user(self)

    @abstractmethod
    def send_message(self, message):
        pass

    def receive_message(self, message, sender):
        print(f"{self.name} получил сообщение от {sender.name}: {message}")

class RegularUser(User):
    def send_message(self, message):
        print(f"{self.name} отправил сообщение: {message}")
        self.mediator.send_message(message, self)

class Moderator(User):
    def send_message(self, message):
        print(f"{self.name} (Модератор) отправил сообщение: {message}")
        self.mediator.send_message(message, self)

    def remove_message(self, message):
        self.mediator.remove_message(message, self)

class Admin(User):
    def send_message(self, message):
        print(f"{self.name} (Админ) отправил сообщение: {message}")
        self.mediator.send_message(message, self)

    def block_user(self, user):
        self.mediator.block_user(user, self)

chat = ChatRoom()

alice = RegularUser("Алиса", chat)
bob = RegularUser("Боб", chat)
charlie = Moderator("Чарли", chat)
diana = Admin("Диана", chat)

alice.send_message("Всем привет!")
bob.send_message("Привет, Алиса!")
charlie.send_message("Я буду следить за порядком.")
alice.send_message("Оскорбление!")

charlie.remove_message("Оскорбление!")

diana.block_user(bob)

bob.send_message("Я еще здесь!")