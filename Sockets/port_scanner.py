# start a local server
# TERMINAL: python -m http.server 8000

import socket

# INET: allows us to talk to IPv4 addresses
# SOCK_STREAM: TCP connection (establish connection, guarantee delivery)

ip = '127.0.0.1' #localhost ip

for port in range (1, 100):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        print(f'Port {port} Connected')
    except socket.error as e:
        print(f'Error {e}')

# OR

for port in range(1, 100):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection = sock.connect_ex((ip, port))

    if connection == 0:
        print(f'Port {port} is open.')
    sock.close()
