"""
компонент
concretecomponent
декоратор
конкретный декоратор
"""
class MessageSender:
    def send(self, message: str):
        raise NotImplementedError

class SimpleSender(MessageSender):
    def send(self, message: str):
        print(f"sending {message}")

class SenderDecorator(MessageSender):
    def __init__(self, wrappee: MessageSender):
        self._wrappee = wrappee

    def send(self, message: str):
        self._wrappee.send(message)

class EncryptedSender(SenderDecorator):
    def send(self, message: str):
        encrypted = self._encrypt(message)
        print('encr')
        self._wrappee.send(encrypted)

    def _encrypt(self, text):
        return ''.join(chr(ord(c) + 1) for c in text)