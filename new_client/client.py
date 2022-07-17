import socket

ip = "192.168.178.55"
port = 8050

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((ip, port))
    s.sendall(b"Hello!")
    data = s.recv(1024)

print(f"Received: {data!r}")