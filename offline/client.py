import socket

hostname = 'google.com'
ip_address = socket.gethostbyname(hostname)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip_address, 80))
request = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
client_socket.send(request.encode())

respone = client_socket.recv(4096)
print("ответ сервера", respone.decode(errors='ignore'))

client_socket.close()