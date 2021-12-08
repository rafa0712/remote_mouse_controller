import mouse
from pynput.mouse import Controller, Button
mouseC = Controller()
def move(command):
    mouse.move(command['x'], command['y'])

def press(command):
    possibles = {
        'left':Button.left,
        'right':Button.right,
    }
    print(command)
    side = command.get('side')
    chosen = possibles.get(side)
    if (chosen):
        mouseC.press(Button.left)

def release(command):
    side = command.get('side')
    if side == 'left':
        mouseC.release(Button.left)
    else:
        mouseC.release(Button.right)

def scroll(command):
    dy = command.get('dy')
    mouseC.scroll(0, dy)

options = {
    "move":move,
    "press":press,
    "release":release,
    "scroll":scroll
}

def handler(type):
    return options.get(type)