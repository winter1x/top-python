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

print(payment.handle(order1))