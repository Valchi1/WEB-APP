import socket
import ssl

# Set the server's host and port
host = 'localhost'
port = 4433

# Create a socket and wrap it with SSL
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

try:
    sock = socket.create_connection((host, port))
    ssl_sock = ssl_context.wrap_socket(sock, server_hostname=host)
    print('Client connected to SSL server...')
    data = ssl_sock.recv(1024)
    print(f'Server said: {data.decode()}')
except Exception as e:
    print(f'An error occurred: {e}')
finally:
    ssl_sock.close()
