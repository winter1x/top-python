import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(3)

server_address = ('localhost', 12345)
message = 'Hello World'
max_attempts = 3

for attempt in range(1, max_attempts + 1):
    try:
        print(f'Sending message {message} попытка {attempt} to server...')
        client_socket.sendto(message.encode(), server_address)

        data, _ = client_socket.recvfrom(4096)
        if data.decode() == 'ACK':
            print('Message received successfully!')
            break

    except socket.timeout:
        print('Timeout error. Retrying...')
    
    except Exception as e:
        print(f"An error occurred: {e}")
        break

else:
    print('Failed to receive a response from the server.')