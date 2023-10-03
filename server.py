import socket

ADDRESS = 'localhost', 1234 # machine address and a port

if __name__ == '__main__':

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_NET is IPv4, SOCK_STREAM is TCP/IP, AD_INET6 is IPv6

    server_socket.bind(ADDRESS)

    server_socket.listen(5) # Queue of 5 requests

    while True:
        client_socket, client_address = server_socket.accept()
        print(f'{client_address = }')
        client_socket.send("Hello World".encode('utf-8'))
        client_socket.close()
