import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))

processed_ids = set()

print('Server started.')

while True:
    try:
        data, client_address = server_socket.recvfrom(1024)
        message = data.decode()
        print(f"Received message from {client_address}: {message}")

        message_parts = message.split(":")
        message_id = message_parts[0]
        message_content = message_parts[1] if len(message_parts) > 1 else ""

        if message_id in processed_ids:
            print(f"Message ID {message_id} has already been processed.")
            continue

        processed_ids.add(message_id)

        if "ERROR" in message_content:
            response = "ERROR"
        else:
            response = "OK"

        server_socket.sendto(response.encode(), client_address)

    except Exception as e:
        print(f"Error: {e}")