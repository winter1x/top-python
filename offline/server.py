'''
клиент сначала отправляет команду UPLOAD/DOWNLOAD
если UPLOAD - передает файл
если DOWNLOAD - сервер ищет файл и возвращает его содержимое
'''

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
server_socket.bind(('127.0.0.1', 9000))
server_socket.listen(1)
print('ожидание подключения')

conn, addr = server_socket.accept()
print(f'подключился клиент {addr}')

command = read_line(conn)
print(f'получена команда {command}')

filename = read_line(conn)
print(f'имя файла {filename}')

if command == 'UPLOAD':
    with open(filename, 'wb') as f:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)
    print('файл принят')
    conn.send('файл загружен'.encode())

elif command == 'DOWNLOAD':
    if not os.path.exists(filename):
        conn.send('[ERROR] - файл не найден'.encode())
    else:
        with open(filename, 'rb') as f:
            while chunk := f.read(1024):
                conn.send(chunk)
            print('файл отправлен клиенту')

else:
    conn.send('[ERROR] - неизвестная команда'.encode())

conn.close()
server_socket.close()
