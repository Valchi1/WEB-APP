import socket
import ssl

# Set the server's host and port
host = 'localhost'
port = 4433

# Create a socket and wrap it with SSL
ssl_context = ssl.create_default_context()

# The CA certificate that issued the server's certificate, for server verification
ssl_context.load_verify_locations('/Users/valchi/SSL-TLSv1/certs/ca.pem')

# Load the client's certificate and key for mutual TLS authentication
ssl_context.load_cert_chain(certfile='/Users/valchi/SSL-TLSv1/certs/client.crt', keyfile='/Users/valchi/SSL-TLSv1/certs/client.key')

# Since it's a local test, we'll not check the hostname (in production, set this to True)
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_REQUIRED  # Require server certificate verification

# Create a secure socket
ssl_sock = ssl_context.wrap_socket(socket.socket(socket.AF_INET),
                                   server_hostname=host)

try:
    # Connect to the server
    ssl_sock.connect((host, port))
    print('Client connected to SSL server...')

    # Receive data from the server
    data = ssl_sock.recv(1024)
    print(f'Server said: {data.decode()}')
except Exception as e:
    print(f'An error occurred: {e}')
finally:
    # Close the connection
    ssl_sock.close()
