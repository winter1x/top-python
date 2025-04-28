import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 8888))

while True:
    msg = input()
    client_socket.send(msg.encode())
    data = client_socket.recv(1024)
    print(data.decode())

    if msg == 'exit':
        break

client_socket.close()