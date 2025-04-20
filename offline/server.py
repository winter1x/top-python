'''
клиент сначала отправляет команду UPLOAD/DOWNLOAD
если UPLOAD - передает файл
если DOWNLOAD - сервер ищет файл и возвращает его содержимое
'''

import socket

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

filename = read_line(conn)
print(f'будем сохранять как {filename}')

with open(filename, 'wb') as f:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        f.write(data)

conn.send('файл получен успешно'.encode())
print('файл сохранен')
conn.close()
server_socket.close()
