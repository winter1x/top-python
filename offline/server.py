"""
добавьте в сообщение клиента уникальный идентификатор, например номер пакета
сервер записывает, какие пакеты уже видел и не отвечает на повторные

на клиенте
время отправки и получения - измерять задержку
ожидает разные ответы - OK / ERROR в зависимости от содержимого
"""

import socket
from time import sleep
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))
print('запущен и ждет сообщений')

while True:
    try:
        data, client_address = server_socket.recvfrom(1024)
        message = data.decode()
        print(f'[{client_address}] => {message}')

        ack = 'ACK'
        #sleep(10) # для выбрасывания ошибки
        server_socket.sendto(ack.encode(), client_address)

    except Exception as e:
        print(f"ошибка на сервере {e}")