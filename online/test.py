"""
bridge
email, sms, push +channel
ошибки регистрация подтверждение

NotifierChannel
send_message(recipient: str, message: str)

Notification


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