import socket
HOST='120.98.0.1'
PORT=1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr =s.accept()
    with conn:
        print(f"Connect by {addr}")
        while True:
            data =conn.recv(1024)
            if not data:
                break
            conn.sendall(all)
