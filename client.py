import socket
from server import ADDRESS

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(ADDRESS)

full_msg = bytearray()
while True:
    msg = client_socket.recv(8)
    if not msg:
        break
    full_msg += msg

print(full_msg.decode())