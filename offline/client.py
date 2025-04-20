import socket
import os

def send_line(sock, line):
    sock.send(f'{line}\n'.encode())

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 9000))

command = input('команда '.strip().upper())
filename = input('имя файла ').strip()

send_line(client_socket, command)
send_line(client_socket, filename)

if command == 'UPLOAD':
    if not os.path.exists(filename):
        print('файл не найден')
        client_socket.close()
    else:
        with open(filename, 'rb') as f:
            while chunk := f.read(1024):
                client_socket.send(chunk)
            response = client_socket.recv(1024)
            print('ответ от сервера ', response.decode())

elif command == 'DOWNLOAD':
    with open(f"загружено_{filename}", 'wb') as f:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            f.write(data)
    print('файл сохранен как:', f"загружено_{filename}")

else:
    print('неизвестная команда')

client_socket.close()
