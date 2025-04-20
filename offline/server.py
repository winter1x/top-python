import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 9000))
server_socket.listen(1)
print('ожидание подключения')
conn, addr = server_socket.accept()
print(f'подключился клиент {addr}')

with open('полученный_файл.txt', 'wb') as f:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        f.write(data)

print('файл сохранен')
conn.close()
server_socket.close()
