from pynput.mouse import Listener
import pyautogui
import json
import SenderSocket.Socket as Socket
address = ('192.168.15.2', 6081)
s = Socket(address)




def on_move(x, y):
    s.send(json.dumps({'x':x, 'y':y}))
    

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Apertou' if pressed else 'Soltou',
        (x, y)))
    if not pressed:
        # Stop listener
        return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0}'.format(
        (x, y)))

with Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll
) as listener:
    listener.join()