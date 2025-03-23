"""
работаем с разными типами уведомлений mail, sms. Система отправляет уведомления. Abstract factory
"""

def send_alert(factory: NotificationFactory, message: str):
    sender = factory.create_sender()
    sender.send_notification(message)


factory = EmailNotificationFactiory() #SMSNotificationFactiory()
send_alert(factory, "тестовое уведомление")
