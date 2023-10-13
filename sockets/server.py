import socket

HOST = "0.0.0.0"
PORT = 4443
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen()

    print(f"Server listening on {HOST}:{PORT}")

    # Accept connection
    conn, addr = sock.accept()
    print(f"Connected to {addr}")
    while True:
        print(f"Client says: {conn.recv(1024).decode()}")