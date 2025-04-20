import socket

"""s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("google.com", 80))
s.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
respone = s.recv(4096)
print(respone.decode())
s.close()
"""
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print(local_ip)

info = socket.getaddrinfo('localhost', 0)
for entry in info:
    print(entry[4][0])

import ipaddress
addr = ipaddress.ip_address('192.168.0.34')
print(addr.is_private)