import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8888))

while True:
    msg = input("Введите сообщение: ")
    client_socket.send(msg.encode())

    data = client_socket.recv(1024)
    print("сервер:", data.decode())

    if msg.lower() == "exit":
        break

client_socket.close()