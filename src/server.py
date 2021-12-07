import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 6081))
print('Listening ...')

while True:
    message, address = s.recvfrom(2048)
    print(message, address)
