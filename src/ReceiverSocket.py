import socket
class Socket:
    def __init__(self, bind_addr):
        self.bind_addr = bind_addr
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind(bind_addr)
    
    def recv(self, size):
        message, address = self.s.recvfrom(size)
        return message.decode(),address
    
        

        