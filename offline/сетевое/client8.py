import socket

hostname = 'google.com'
ip_address = socket.gethostbyname(hostname)
print(f'IP address of {hostname} is {ip_address}')

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip_address, 80))
request = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
client_socket.send(request.encode())

response = client_socket.recv(4096)
print('Response:', response.decode(errors='ignore'))

client_socket.close()