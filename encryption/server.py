import socket
import ssl
import logging

# Setup basic logging
logging.basicConfig(level=logging.INFO)

# Set the server's host and port
host = 'localhost'
port = 4433  # Consider using port 443 for production with appropriate permissions

print("Setting up the socket...")

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print("Socket created.")

# Wrap the socket with SSL
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(certfile='/Users/valchi/SSL-TLSv1/certs/server.crt', keyfile='/Users/valchi/SSL-TLSv1/certs/server.key')
ssl_context.set_ciphers('HIGH:!aNULL:!eNULL:!EXPORT:!DES:!MD5:!PSK:!RC4')
ssl_context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1  # Disabling older versions
ssl_context.options |= ssl.OP_NO_SSLv2 | ssl.OP_NO_SSLv3  # Explicitly disable SSLv2 and SSLv3
ssl_context.minimum_version = ssl.TLSVersion.TLSv1_2  # Explicitly set minimum TLS version

print("SSL context created.")

try:
    ssl_sock = ssl_context.wrap_socket(sock, server_side=True)
    print("SSL socket wrapped.")
    
    ssl_sock.bind((host, port))
    print(f"Socket bound to {(host, port)}.")

    ssl_sock.listen(5)
    print(f"Server is now listening on {(host, port)}.")
except Exception as e:
    logging.error(f"Failed to bind or listen on {(host, port)}: {e}")
    exit(1)

# Handle incoming connections
while True:
    try:
        print("Waiting for a connection...")
        client_sock, client_addr = ssl_sock.accept()
        print(f"Connection from {client_addr}")

        client_sock.sendall(b'Hello, SSL!\n')
        print("Sent greeting to the client.")
    except Exception as e:
        logging.error(f"Error handling client {client_addr}: {e}")
    finally:
        client_sock.close()
        print("Closed the client socket.")
