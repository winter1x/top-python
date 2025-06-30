import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8888))

server_socket.listen(1)
print("Server is listening...")

conn, addr = server_socket.accept()
print(f"Connection from {addr}")

data = conn.recv(1024)
print(f"Received data: {data.decode()}")

conn.send("Server received your data!".encode())

conn.close()
server_socket.close()