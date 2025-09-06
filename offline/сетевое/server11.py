import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))

print('Server started.')

while True:
    try:
        data, client_address = server_socket.recvfrom(1024)
        message = data.decode()
        print(f"Received message from {client_address}: {message}")

        ack = 'ACK'
        server_socket.sendto(ack.encode(), client_address)

    except Exception as e:
        print(f"Error: {e}")