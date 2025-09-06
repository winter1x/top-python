import socket
import os

def read_line(conn):
    line = b''
    while True:
        char = conn.recv(1)
        if not char or char == b'\n':
            break
        line += char
    return line.decode('utf-8')

def handle_client(conn, addr):
    print(f"Клиент подключился: {addr}")
    try:
        while True:
            command = read_line(conn).strip()
            if not command:
                break
            print(f"Команда: {command}")

            if command == "EXIT":
                print("Клиент завершил соединение.")
                break

            filename = read_line(conn).strip()
            print(f"Имя файла: {filename}")

            if command == "UPLOAD":
                with open(filename, 'wb') as f:
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        f.write(data)
                print("Файл успешно получен.")
                conn.sendall("Файл получен\n".encode('utf-8'))
                break  

            elif command == "DOWNLOAD":
                if not os.path.exists(filename):
                    conn.sendall("ОШИБКА: файл не найден\n".encode('utf-8'))
                    continue

                filesize = os.path.getsize(filename)
                conn.sendall(f"{filesize}\n".encode('utf-8'))  

                with open(filename, 'rb') as f:
                    while chunk := f.read(1024):
                        conn.sendall(chunk)
                
                conn.sendall(b"END_OF_FILE\n")
                print("Файл отправлен.")



    except Exception as e:
        print("Ошибка:", e)
    finally:
        conn.close()
        print("Соединение закрыто.")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 9000))
server_socket.listen()
print("Сервер запущен. Ожидаем подключения...")

while True:
    conn, addr = server_socket.accept()
    handle_client(conn, addr)