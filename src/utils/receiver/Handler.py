import mouse
from pynput.mouse import Controller, Button
mouseC = Controller()
def move(command):
    mouse.move(command['x'], command['y'])
def press(command):
    side = command.get('side')
    if side == 'left':
        mouseC.press(Button.left)
    else:
        mouseC.press(Button.right)
def release(command):
    side = command.get('side')
    if side == 'left':
        mouseC.release(Button.left)
    else:
        mouseC.release(Button.right)

options = {
    "move":move,
    "press":press,
    "release":release
}

def handler(type):
    return options.get(type)