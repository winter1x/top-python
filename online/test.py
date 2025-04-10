"""
adapter
старый интерфейс - pay(amount: float)
новый провайдер, интерфейс - make_payment(data: dict)

OldPaymentProcessor
NewPaymentProcessor
NewPaymentAdapter
process_payment(process, amount)
"""