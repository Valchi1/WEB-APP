import socket
import ssl

# Set the server's host and port
host = 'localhost'
port = 4433  # Standard port for HTTPS is 443, but we'll use 4433 to avoid permissions issues

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Wrap the socket with SSL
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(certfile='/Users/valchi/SSL-TLSv1/certs/server.crt', keyfile='/Users/valchi/SSL-TLSv1/certs/server.key')  # Load your certificate and private key
ssl_context.set_ciphers('HIGH:!aNULL:!eNULL:!EXPORT:!DES:!MD5:!PSK:!RC4')  # Strong ciphers
ssl_context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1  # Disable lower versions of TLS
ssl_sock = ssl_context.wrap_socket(sock, server_side=True)

# Bind and listen
ssl_sock.bind((host, port))
ssl_sock.listen(5)
print(f'SSL server is running and listening on {(host, port)}...')

# Handle incoming connections
while True:
    client_sock, client_addr = ssl_sock.accept()
    print(f'Connection from {client_addr}')
    client_sock.sendall(b'Hello, SSL!\n')
    client_sock.close()
