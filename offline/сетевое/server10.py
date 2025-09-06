import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))
print("Server is listening...")

while True:
    data, client_address = server_socket.recvfrom(1024)
    print(f'Received data from {client_address}: {data.decode()}')

    response = 'Сообщение получено'
    server_socket.sendto(response.encode(), client_address)