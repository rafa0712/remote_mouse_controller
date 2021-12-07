import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 6081))
msg = s.recv(2048)
print(msg)