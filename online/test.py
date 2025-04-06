"""
state
чат
пользователь - гость/авторизован/модератор
"""

from abc import ABC, abstractmethod

class UserState(ABC):
    @abstractmethod
    def view_messages(self, context):
        pass

    @abstractmethod
    def send_message(self, context, message: str):
        pass

    @abstractmethod
    def delete_message(self, context, message_id: int):
        pass

class GuestState(UserState):
    def view_messages(self, context):
        print("гость смотрит")

    def send_message(self, context, message: str):
        print('гость не может отправить')

    def delete_message(self, context, message_id: int):
        print('гость не может удалить')

class AuthenticatedState(UserState):
    def view_messages(self, context):
        print("пользователь смотрит")

    def send_message(self, context, message: str):
        print(f'пользователь отправил {message}')

    def delete_message(self, context, message_id: int):
        print('пользователь не может удалить')

class ModeratorState(UserState):
    def view_messages(self, context):
        print("модератор смотрит")

    def send_message(self, context, message: str):
        print(f'модератор отправил {message}')

    def delete_message(self, context, message_id: int):
        print(f'модератор удалил сообщение с id {message_id}')

class User:
    def __init__(self):
        self._state: UserState = GuestState()

    def set_state(self, state: UserState):
        self._state = state
        print(f"состояние стало {type(state).__name__}")

    def view_messages(self):
        self._state.view_messages(self)

    def send_message(self, message: str):
        self._state.send_message(self, message)

    def delete_message(self, message_id: int):
        self._state.delete_message(self, message_id)


user = User()
user.view_messages()
user.send_message('hi')
user.delete_message(1)

user.set_state(AuthenticatedState())
user.view_messages()
user.send_message('hii')
user.delete_message(1)

user.set_state(ModeratorState())
user.view_messages()
user.send_message('hiii')
user.delete_message(1)