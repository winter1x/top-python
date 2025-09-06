import socket
import threading
from datetime import datetime

LOG_FILE = 'connections.log'

def log_connection(ip, port):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] подключение с {ip}: порт {port}\n"
    with open(LOG_FILE, 'a') as file:
        file.write(log_entry)
    print(log_entry.strip())

def handle_client(conn, addr):
    ip, port = addr
    log_connection(ip, port)

    try:
        data = conn.recv(1024).decode()
        print(f"Received from client {ip}: data: {data}")
        response = f"Received from ip {ip}: data: {data}"
        conn.send(response.encode())  
    except Exception as e:
        print(f"Error handling client {ip}: {e}")
    finally:
        conn.close()

def start_server():
    host = '0.0.0.0'
    port = 9000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server started on {host}:{port} and listening for connections...")

    while True:
        conn, addr = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
