import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(3)

server_address = ('localhost', 12345)
message = 'привет сервер'
max_attempts = 3

for attempt in range(1, max_attempts + 1):
    try:
        print(f"попытка {attempt}: отправка")
        client_socket.sendto(message.encode(), server_address)

        data, _ = client_socket.recvfrom(1024)
        if data.decode() == 'ACK':
            print("подтвердили")
            break

    except socket.timeout:
        print("ответ от сервера не получен, пробуем снова")

    except Exception as e:
        print(f"ошибка клиента {e}")
        break

else:
    print('сервер не ответил после 3 попыток')