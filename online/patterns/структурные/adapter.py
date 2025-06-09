"""
адаптер позволяет объектам с несовместимыми
интерфейсами работать вместе

+
старую систему с новыми объектами
интегрируем внешнюю библиотеку
унифицировать интерфейсы
перевести объект в понятный формат

подходы
адаптер на уровне объектов - композиция
адаптер на уровне классов - через множественное наследование

структура
target - целевой интерфейс
adaptee - адаптируемый объект
adapter

не используем когда:
можем поменять старый код
приходится адаптировать много объектов/методов

facade - не меняет интерфейс
decorator - добавляет функционал
bridge - отделяет абстракцию от реализации
"""

class OldPrinter:
    def print_text(self, text: str):
        print(f'[OLD] {text}')

class NewPrinter:
    def send(self, data: str):
        print(f"[NEW] {data}")

class PrintAdapter:
    def __init__(self, adaptee: NewPrinter):
        self.adaptee = adaptee

    def print_text(self, text: str):
        self.adaptee.send(text)

def client_code(printer):
    printer.print_text("hi")

old = OldPrinter()
client_code(old)

new = NewPrinter()
adapter = PrintAdapter(new)
client_code(adapter)

"""
adapter
старый интерфейс - pay(amount: float)
новый провайдер, интерфейс - make_payment(data: dict)

OldPaymentProcessor
NewPaymentProvider
NewPaymentAdapter
process_payment(process, amount)
"""
class OldPaymentProcessor:
    def pay(self, amount: float):
        print(f'[old] Оплата {amount} руб.')

class NewPaymentProvider:
    def make_payment(self, data: dict):
        amount = data.get('amount')
        print(f'[new] Оплата {amount} руб.')

class NewPaymentAdapter():
    def __init__(self, new_provider: NewPaymentProvider):
        self.new_provider = new_provider

    def pay(self, amount: float):
        payment_data = {'amount': amount}
        self.new_provider.make_payment(payment_data)

def process_payment(processor, amount):
    processor.pay(amount)

old = OldPaymentProcessor()
new = NewPaymentAdapter(NewPaymentProvider())
process_payment(old, 150.0)
process_payment(new, 150.0)

"""
реализовано
Rectangle (координаты левого верхнего угла, ширину и высоту)

надо добавить
LegacySquare (координаты центра и длина стороны)

Rectangle 
    x 
    y
    width
    height
LegacySquare
    cx
    cy
    side

создать интерфейс или базовый класс Drawable с draw()
Rectangle реализует Drawable
Reactangle.draw()

SquareAdapter принимает объект LegacySquare и реализует интерфейс Drawable
"""
shapes = [
    Rectangle(0, 0, 100, 50),
    SquareAdapter(LegacySquare(50, 50, 40))
]

for shape in shapes:
    shape.draw()
    