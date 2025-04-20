'''
клиент узнает ip адрес сервера по имени хоста (DNS)
сервер выводит ip адрес каждого подключившего клиента
сообщения передаются по TCP
логируется ip и порт всех входящих соединений
socket
'''

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("0.0.0.0", 9000))
server_socket.listen(1)
print('("0.0.0.0", 9000)')

conn, addr = server_socket.accept()
print(f'ip {addr[0]} порт {addr[1]}')

data = conn.recv(1024)
print('получено', data.decode())
conn.send('принято'.encode())

conn.close()
server_socket.close()