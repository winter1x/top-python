"""
структура
handler обработчик
concrete handler конкретный обработчик
client клиент

используем когда
несколько объектов обрабатывают запрос
обработчики автоматически определяются
без привязки отправителя и получателя

(+) 
гибкость 
снижение связанности
простота
динамичность

(-)
сложность отслеживания
сложность конечной обработки
неэффективность при большом количестве объектов
"""

from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        pass

class LowLevelSupport(Handler):
    def handle(self, request):
        if request == 'reset password':
            return "LowLevelSupport: reset password"
        elif self._next_handler:
            return self._next_handler.handle(request)
        return "LowLevelSupport не может обработать"

class MidLevelSupport(Handler):
    def handle(self, request):
        if request == 'account blocked':
            return "MidLevelSupport: account blocked"
        elif self._next_handler:
            return self._next_handler.handle(request)
        return "MidLevelSupport не может обработать"

class HighLevelSupport(Handler):
    def handle(self, request):
        if request == 'server down':
            return "HighLevelSupport: server down"
        elif self._next_handler:
            return self._next_handler.handle(request)
        return "HighLevelSupport не может обработать"

low = LowLevelSupport()
mid = MidLevelSupport()
high = HighLevelSupport()

low.set_next(mid).set_next(high)

print(low.handle("reset password"))
print(low.handle("account blocked"))
print(low.handle("server down"))
print(low.handle("else"))

def handler1(request):
    if request == 'ping':
        return 'pong'
    return None

def handler2(request):
    if request == 'hi':
        return 'hello'
    return None

def chain(request, handlers):
    for handler in handlers:
        result = handler(request)
        if result:
            return result
    return "no handler found"

print(chain('ping', [handler1, handler2]))
print(chain('hi', [handler1, handler2]))
print(chain('bye', [handler1, handler2]))


"""
chain of responsibility
для обработки заказов (оплата, упаковка, доставка)
"""

from abc import ABC, abstractmethod

class OrderHandler(ABC):
    def __init__(self):
        self._next = None

    def set_next(self, handler):
        self._next = handler
        return handler

    @abstractmethod
    def handle(self, order):
        pass

class PaymentHandler(OrderHandler):
    def handle(self, order):
        if not order.get("paid", False):
            return "заказ не оплачен"
        print('оплата есть')
        if self._next:
            return self._next.handle(order)
        return "обработка завершена"

class PackagingHandler(OrderHandler):
    def handle(self, order):
        if not order.get("items", False):
            return "нет товаров"
        print(f"упаковка {len(order['items'])} товаров")
        if self._next:
            return self._next.handle(order)
        return "обработка завершена"

class ShippingHandler(OrderHandler):
    def handle(self, order):
        if not order.get("address", False):
            return "адрес не указан"
        print(f"отправка на {order['address']}")
        return "заказ обработан"

payment = PaymentHandler()
packaging = PackagingHandler()
shipping = ShippingHandler()

payment.set_next(packaging).set_next(shipping)

order1 = {
    "paid": True,
    "items": ['мышь', "ноутбук"],
    "address": 'адрес'
}

order2 = {
    "paid": False,
    "items": ['мышь', "ноутбук"],
    "address": 'адрес'
}

order3 = {
    "paid": True,
    "items": [],
    "address": 'адрес'
}

order4 = {
    "paid": True,
    "items": ['мышь', "ноутбук"],
    "address": ''
}

print(payment.handle(order1))
print(payment.handle(order2))
print(payment.handle(order3))
print(payment.handle(order4))


"""
фильтрация и модерация пользовательского контента в социальной сети

публикуют текстовые сообщения
цепочка фильтров
проверка на цензуру - маскировка плохих слов
проверка на спам
проверка на размер текста - заблокировать слишком большие сообщения
проверка на чувствительные данные 
"""