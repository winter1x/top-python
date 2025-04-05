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

class ChatRoom(ChatMediator):
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, message, sender):
        for user in self.users:
            if user != sender:
                user.receive_massage(message, sender)

class User:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator
        mediator.add_user(self)

    def send_message(self, message):
        print(f"{self.name} отправляет сообщение {message}")
        self.mediator.send_message(message, self)

    def receive_massage(self, message, sender):
        print(f'{self.name} получил сообщение от {sender.name} {message}')

chat = ChatRoom()

alice = User("alice", chat)
bob = User("bob", chat)
matvey = User('matvey', chat)

alice.send_message('hi')
bob.send_message('hi')