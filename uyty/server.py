import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("localhost", 12345))
print("Сервер запущен. Ожидание сообщений...")
while True:
    data, client_address = server_socket.recvfrom(1024)
    print("Получено сообщение от", client_address, ":", data.decode())

    response = "Сообщение успешно получено"
    server_socket.sendto(response.encode(), client_address)