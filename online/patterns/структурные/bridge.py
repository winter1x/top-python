"""
Структура:
abstraction абстракция
refined abstraction расширенная абстракция
impementor интерфейс реализации
concreteImplementor конкретные реализации

не используем
если реализация будет только одна
расширение абстракции и реализации может быть зависимым или небольшим
если использование усложнит понимание

adapter соединяет интерфейсы
decorator добавляет новые функции 
strategy замена поведения
absract factory может использоваться вместе с bridge
"""
class DrawingApi:
    def draw_circle(self, x: int, y: int, radius: int):
        raise NotImplemented

class OpenGLAPI(DrawingApi):
    def draw_circle(self, x: int, y: int, radius: int):
        print(f"[OpenGl] {x, y, radius}")

class DirectXAPI(DrawingApi):
    def draw_circle(self, x: int, y: int, radius: int):
        print(f"[DirectX] {x, y, radius}")

class Shape:
    def __init__(self, drawing_api: DrawingApi):
        self.drawing_api = drawing_api

    def draw(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, x: int, y: int, radius: int, drawing_api: DrawingApi):
        super().__init__(drawing_api)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        self.drawing_api.draw_circle(self.x, self.y, self.radius)

circle1 = Circle(10, 20, 5, OpenGLAPI())
circle2 = Circle(100, 200, 50, DirectXAPI())

circle1.draw()
circle2.draw()

"""
bridge
email, sms, pushchannel
типы уведомлений
ошибки регистрация подтверждение
"""

class NotifierChannel:
    def send_message(self, recipient: str, message: str):
        raise NotImplementedError("dfve")

class EmailChannel(NotifierChannel):
    def send_message(self, recipient: str, message: str):
        print(f"[EMAIL] {recipient} {message}")

class SMSChannel(NotifierChannel):
    def send_message(self, recipient: str, message: str):
        print(f"[SMS] {recipient} {message}")

class PushChannel(NotifierChannel):
    def send_message(self, recipient: str, message: str):
        print(f"[PUSH] {recipient} {message}")

class Notification:
    def __init__(self, channel: NotifierChannel):
        self.channel = channel

    def notify(self, recipient: str):
        raise NotImplementedError

class ErrorNotification(Notification):
    def notify(self, recipient: str):
        message = "ErrorNotification"
        self.channel.send_message(recipient, message)

class RegistrationNotification(Notification):
    def notify(self, recipient: str):
        message = "RegistrationNotification"
        self.channel.send_message(recipient, message)

class ConfirmationNotification(Notification):
    def notify(self, recipient: str):
        message = "ConfirmationNotification"
        self.channel.send_message(recipient, message)

email = EmailChannel()
sms = SMSChannel()
push = PushChannel()

notif1 = ErrorNotification(email)
notif2 = RegistrationNotification(sms)
notif3 = ConfirmationNotification(push)

notif1.notify('почта')
notif2.notify('телефон')
notif3.notify('юзер')

"""
Система тестирования

иерарахия вопросов
Question def check_answer(self, user_answer):
SingleChoiceQuestion один правильный ответ
MultipleChoiceQuestion несколько правильных ответов

интерфейс проверок
AnswerChecker def check()

реализации
StrictChecker точное совпадение
PartialChecker частичное совпадение

Question содержит ссылку на AnswerChecker
"""