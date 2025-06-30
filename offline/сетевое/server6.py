import socket
import os

def read_line(conn):
    line = b''
    while True:
        char = conn.recv(1)
        if char == b'\n' or not char:
            break
        line += char
    return line.decode()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8888))
server_socket.listen(1)
print("Сервер запущен, ожидаем подключение...")

conn, addr = server_socket.accept()
print(f"Клиент подключился: {addr}")

# - Прочитать команду (UPLOAD или DOWNLOAD)
# - Прочитать имя файла

# Если команда UPLOAD:
#   - Открыть файл для записи
#   - Читать данные из сокета и записывать в файл
#   - После окончания отправить клиенту сообщение об успешной загрузке

# Если команда DOWNLOAD:
#   - Проверить существует ли файл
#   - Если нет — отправить сообщение об ошибке
#   - Если да — открыть файл и отправить его содержимое клиенту

# Если команда неизвестна:
#   - Отправить сообщение об ошибке

conn.close()
server_socket.close()