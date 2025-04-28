import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8888))
server_socket.listen(1)
print("Server started")

conn, addr = server_socket.accept()
print("Connection established")

data = conn.recv(1024)
print("Received:", data.decode())

conn.send("Hello, client!".encode())

conn.close()
server_socket.close()















