import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8888))

client_socket.send("Hello from client!".encode())

data = client_socket.recv(1024)
print(f"Received data: {data.decode()}")

client_socket.close()