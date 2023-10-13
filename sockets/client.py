import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(("127.0.0.1", 4443))
    while True:
        sock.sendall(input().encode())
        print(sock.recv(1024).decode())