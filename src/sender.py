from pynput.mouse import Listener, Button
import json
from SenderSocket import *
address = ('192.168.15.2', 6081)
s = Socket(address)




def on_move(x, y):
    s.send(json.dumps({'type':'move', 'x':x, 'y':y}))

def on_click(x, y, button, pressed):
    button = button._name_
    
    if pressed:
        s.send(json.dumps({'type':'press', 'side':button}))
    else:
        s.send(json.dumps({'type':'release', 'side':button}))

def on_scroll(x, y, dx, dy):
    print('Scrolled {0}'.format(
        (x, y)))

with Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll
) as listener:
    listener.join()