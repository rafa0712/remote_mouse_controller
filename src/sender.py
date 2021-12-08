from pynput.mouse import Listener
import json
from SenderSocket import *
address = ('192.168.15.2', 6081)
s = Socket(address)




def on_move(x, y):
    s.send(json.dumps({'type':'move', 'x':x, 'y':y}))

def on_click(x, y, button, pressed):
    print(button)
    if pressed:
        s.send(json.dumps({'type':'press'}))
    else:
        s.send(json.dumps({'type':'hold'}))

def on_scroll(x, y, dx, dy):
    print('Scrolled {0}'.format(
        (x, y)))

with Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll
) as listener:
    listener.join()