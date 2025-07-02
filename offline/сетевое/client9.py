import socket

def main():
    hostname = 'localhost'
    #hostname = input("Enter the hostname (name or ip): ").strip()

    try:
        ip_address = socket.gethostbyname(hostname)
        print(f"IP address of {hostname}: {ip_address}")

    except socket.gaierror:
        print("Hostname could not be resolved.")
        return
    
    port = 9000

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((ip_address, port))

        message = input("Enter your message: ")
        client_socket.send(message.encode())

        response = client_socket.recv(1024).decode()
        print(f"Server response: {response}")

        client_socket.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()