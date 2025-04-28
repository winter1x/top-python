import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8888))
server_socket.listen(1)
print("Server started")

conn, addr = server_socket.accept()
print("Connected to client:", addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    message = data.decode()
    print("Received message:", message)

    if message.lower() == 'exit':
        print("Connection closed")
        break
    
    conn.send(f"Server received: {message}".encode())

conn.close()
server_socket.close()














