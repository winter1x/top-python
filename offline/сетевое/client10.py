import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = "Hello, UDP Server!"

client_socket.sendto(message.encode(), ("localhost", 12345))

data, server_address = client_socket.recvfrom(4096)

print("Received from server:", data.decode())