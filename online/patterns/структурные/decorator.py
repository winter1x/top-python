"""
структура:
component компонент
concreteComponent
Decorator декоратор
concreteDecorator конкретный декоратор

Client -> Decorator1 -> Decorator2 -> ... -> ConcreteComponent

применяем когда:
расширяет функционал не изменяя код 
необходимость добавления дополнительного функционала во множество объектов
отделить основный функционал от дополнительного


@functools.lru_cache
@staticmethod
@login_required

(-)
увеливает количество классов
может быть сложно понять стек оберток
иногда проще наследование или функции


adapter меняет интерфейс
proxy тоже обораивает, но для контроля доступа или отложенной загрузки
composite строит иерархии 
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

class LoggingSender(SenderDecorator):
    def send(self, message: str):
        print(f"[LOG] {message}")
        self._wrappee.send(message)

base = SimpleSender()
logged = LoggingSender(base)
secure = EncryptedSender(logged)

secure.send("hi")

"""
decorator
выводить текст, оборачивая его
    жирный
    курсив
    зачеркнут
TextComponent render() - просто возвращает строку
PlainText - просто текст
    BoldDecorator **текст**
    курсивdecorator *текст*
    зачеркнутdecorator ~~текст~~
"""

class TextComponent:
    def render(self) -> str:
        raise NotImplementedError

class PlainText(TextComponent):
    def __init__(self, text: str):
        self.text= text

    def render(self) -> str:
        return self.text

class TextDecorator(TextComponent):
    def __init__(self, component: TextComponent):
        self._component = component

    def render(self) -> str:
        return self._component.render()

class BoldDecorator(TextDecorator):
    def render(self) -> str:
        return f"**{super().render()}**"

class ItalicDecorator(TextDecorator):
    def render(self) -> str:
        return f"*{super().render()}*"

class StrikethroughDecorator(TextDecorator):
    def render(self) -> str:
        return f"~~{super().render()}~~"

class UnderlineDecorator(TextDecorator):
    def render(self) -> str:
        return f"__{super().render()}__"

base = PlainText("hi")
decorated = ItalicDecorator(BoldDecorator(StrikethroughDecorator(base)))
print(decorated.render())

"""
система расчета стоимости билетов
у билета базовая цена
    vip
    страховка
    срочная покупка
к цене добавляются надбавки

интерфейс Ticket
class BaseTicket
    get_price
    get_description

декораторы-наценки
наследуются от интерфейса Ticket с ссылкой на объект Ticket
VipAccessDecorator - цена * 1.5 с вип доступом
InsuranceDecorator - цена + 100 со страховкой
LastMinuteDecorator - цена * 1.3 за срочную покупку
"""