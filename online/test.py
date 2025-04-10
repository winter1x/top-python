"""
adapter
старый интерфейс - pay(amount: float)
новый провайдер, интерфейс - make_payment(data: dict)

OldPaymentProcessor
NewPaymentProcessor
NewPaymentAdapter
process_payment(process, amount)
"""

old = OldPaymentProcessor()
new = NewPaymentProcessor()
process_payment(old, 150.0)
process_payment(new, 150.0)