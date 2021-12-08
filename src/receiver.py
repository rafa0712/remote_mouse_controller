import json
from ReceiverSocket import *
from utils.receiver.Handler import handler
#from pynput.mouse import Controller, Button


print('Listening ...')
s = Socket(('', 6081))
cont = 0
while True:
    cont+=1
    message, address = s.recv(2048)
    message = json.loads(message)
    chosen = handler(message['type'])
    if not chosen:
        continue
    chosen(message)
    
