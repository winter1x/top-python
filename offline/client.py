import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect(("127.0.0.1", 8888))
except ConnectionRefusedError:
    print("не удалось подключиться к серверу")

while True:
    msg = input('введите сообщение: ')
    client_socket.send(msg.encode())

    data = client_socket.recv(1024)
    print('сервер:', data.decode())

    if msg.lower() == 'выход':
        break

client_socket.close()