import socket
import os

def send_line(sock, line):
    sock.sendall(f"{line}\n".encode('utf-8'))

def recv_line(sock):
    line = b''
    while True:
        char = sock.recv(1)
        if not char or char == b'\n':
            break
        line += char
    return line.decode('utf-8')

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 9000))
print("Подключено к серверу. Введите команды (UPLOAD / DOWNLOAD / EXIT)")

while True:
    command = input("\nВведите команду: ").strip().upper()
    send_line(client_socket, command)

    if command == "EXIT":
        print("Завершаем соединение.")
        break

    elif command in ["UPLOAD", "DOWNLOAD"]:
        filename = input("Введите имя файла: ").strip()
        send_line(client_socket, filename)

        if command == "UPLOAD":
            if not os.path.exists(filename):
                print("Файл не найден.")
                continue
            with open(filename, 'rb') as f:
                while chunk := f.read(1024):
                    client_socket.sendall(chunk)
            client_socket.shutdown(socket.SHUT_WR)

            response = recv_line(client_socket)
            print("Ответ сервера:", response)

            client_socket.close()
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(('127.0.0.1', 9000))

        elif command == "DOWNLOAD":
            file_size_str = recv_line(client_socket)
            if file_size_str.startswith("ОШИБКА:"):
                print(file_size_str)
                continue

            try:
                expected_bytes = int(file_size_str)
            except ValueError:
                print("Ошибка: сервер вернул некорректный размер файла.")
                continue

            received_bytes = 0
            with open(f"загружено_{filename}", 'wb') as f:
                while received_bytes < expected_bytes:
                    data = client_socket.recv(min(1024, expected_bytes - received_bytes))
                    if not data:
                        break
                    if data == b"END_OF_FILE\n":  
                        break
                    f.write(data)
                    received_bytes += len(data)

            if received_bytes == expected_bytes:
                print(f"Файл успешно сохранён как загружено_{filename}")
            else:
                print("Файл получен не полностью.")


    else:
        print("Неизвестная команда.")

client_socket.close()