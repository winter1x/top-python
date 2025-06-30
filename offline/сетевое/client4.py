import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8888))

with open('отправляемый_файл.txt', 'rb') as f:
    while chunk := f.read(1024):
        client_socket.send(chunk)

print('файл отправлен')
client_socket.close()