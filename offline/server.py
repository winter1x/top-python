import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))
print('запущен и ждет сообщений')

while True:
    data, client_address = server_socket.recvfrom(1024)
    print(f'получено {client_address}: {data.decode()}')

    response = 'сообщение получено'
    server_socket.sendto(response.encode(), client_address)