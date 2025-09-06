import socket
ip = socket.gethostbyname("google.com")
print(ip)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('google.com', 80))
s.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
response = s.recv(4096)
print(response.decode("utf-8"))
s.close()

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print(f"Local IP address: {local_ip}")

info = socket.getaddrinfo('localhost', 0)
for entry in info:
    print(entry[4][0])

import ipaddress
addr = ipaddress.ip_address('127.0.0.1')
print(addr.is_private)