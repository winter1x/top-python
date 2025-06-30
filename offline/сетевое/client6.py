import socket
import os

# Функция для отправки строки с переводом строки
#
#

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8888))

# запросить у пользователя команду (UPLOAD или DOWNLOAD) и имя файла
# command = ...
# filename = ...

# Отправляем команду и имя файла
# send_line(client_socket, command)
# send_line(client_socket, filename)

# Здесь обработать команды
# Если команда UPLOAD:
#   - Проверить существует ли файл
#   - Если существует: открыть файл и отправить содержимое
#   - Получить и вывести ответ от сервера

# Если команда DOWNLOAD:
#   - Принять файл от сервера и сохранить его с префиксом "загружено_"

# Если команда неизвестна:
#   - Вывести сообщение об ошибке

client_socket.close()