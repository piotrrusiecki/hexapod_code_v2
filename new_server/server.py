import socket

#ip = socket.gethostbyname(socket.gethostname())
ip = "0.0.0.0"
port = 8050

print(f"IP Address: {ip}")
print(f"Port: {port}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(((ip, port)))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connecte3d by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
