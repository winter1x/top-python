import socket
import os

filename = 'отправляемый_файл.txt'
filesize = os.path.getsize(filename)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 9000))

client_socket.send(f"{filename}\n".encode())

with open(filename, 'rb') as f:
    while chunk := f.read(1024):
        client_socket.send(chunk)

response = client_socket.recv(1024)
print('ответ сервера: ', response.decode())
print('файл отправлен')
client_socket.close()
