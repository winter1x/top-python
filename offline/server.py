"""
bind
listen
accept
connect
send
recv
"""

import socket
import threading

def handle_client(conn, addr):
    print(f"новый клиент {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break
        message = data.decode()
        print(f"[{addr}] {message}")
        conn.send(f'принято {message}'.encode())
    conn.close()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 8888))
server_socket.listen()
print('ожидание подключения')

while True:
    conn, addr = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    print(f"активные соединения {threading.active_count() -1}")