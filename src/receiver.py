import ReceiverSocket as Socket
print('Listening ...')
s = Socket(('', 6081))
while True:
    message, address = s.recv(2048)
    print(message, address)
