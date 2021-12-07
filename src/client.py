from pynput.mouse import Listener
import pyautogui
import socket
address = ('192.168.15.2', 6081)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto('OI servidor'.encode(), address)


def on_move(x, y):
    print('Pointer moved to {}'.format(
        (x, y)))

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