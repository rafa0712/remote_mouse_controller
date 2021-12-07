import socket
class Socket:
    def __init__(self, target_add):
        self.target_addr = target_add
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def send(self, data):
        data = data.encode()
        self.s.sendto(data, self.target_addr)
        

        