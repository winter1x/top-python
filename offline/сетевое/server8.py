import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 8888))
server_socket.listen(1)
print("Server is listening...")

conn, addr = server_socket.accept()
print(f'Connection from IP: {addr[0]} Port: {addr[1]}')

data = conn.recv(1024)
print('Data received: ', data.decode())
conn.send('принято'.encode())

conn.close()
server_socket.close()