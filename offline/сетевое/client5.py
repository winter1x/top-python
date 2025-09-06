import socket
import os

filename = 'отправляемый_файл.txt'
filesize = os.path.getsize(filename)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8888))

client_socket.send(f"{filename}\n".encode())

with open(filename, 'rb') as file:
    while chunk := file.read(1024):
        client_socket.send(chunk)

print('файл отправлен')
client_socket.close()