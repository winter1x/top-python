import socket

def read_line(conn):
    line = b""
    while True:
        char = conn.recv(1)
        if char == b"\n" or not char:
            break
        line += char
    return line.decode()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8888))
server_socket.listen(1)
print("Server started")

conn, addr = server_socket.accept()
print("Connection established", addr)

filename = read_line(conn)
print("Requested file:", filename)

with open(filename, "wb") as file:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        file.write(data)

print("File received")
conn.close()
server_socket.close()