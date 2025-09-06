import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(3)

server_address = ('localhost', 12345)
message_base = 'привет сервер этот пакет с ид'
max_attempts = 3

for attempt in range(1, max_attempts + 1):
    message_id = f"{attempt}"
    message = f"{message_id}:{message_base} {attempt}"
    try:
        start_time = time.time()

        print(f'Sending message {message} попытка {attempt} to server...')
        client_socket.sendto(message.encode(), server_address)

        data, _ = client_socket.recvfrom(4096)

        end_time = time.time()
        delay = end_time - start_time

        print(f'Received response from server: {data.decode()}')
        print(f"Delay: {delay:.4f} seconds")

        if data.decode() == "OK":
            print(f"Server received message {message} with id {message_id} successfully.")
            break
        elif data.decode() == "ERROR":
            print("Server responded with ERROR")
            break

    except socket.timeout:
        print('Timeout error. Retrying...')
    
    except Exception as e:
        print(f"An error occurred: {e}")
        break

else:
    print('Failed to receive a response from the server.')