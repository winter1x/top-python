import socket

def read_line(conn):
    line = b''
    while True:
        char = conn.recv(1)
        if char == b'\n' or not char:
            break
        line += char
    return line.decode()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8888))
server_socket.listen(1)
print("Server is listening...")

conn, addr = server_socket.accept()
print("Connected by", addr)

filename = f'2{read_line(conn)}'
print("Filename:", filename)

with open(filename, 'wb') as f:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        f.write(data)

print('File received!')
conn.close()
server_socket.close()