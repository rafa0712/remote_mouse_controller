import mouse
from pynput.mouse import Controller, Button
mouseC = Controller()
def move(command):
    mouse.move(command['x'], command['y'])

def press(command):
    possibles = {
        'left':Button.left,
        'right':Button.right,
        'button8':Button.button8,
        'button9':Button.button9
    }
    side = command.get('side')
    chosen = possibles.get(side)
    if (chosen):
        mouseC.press(chosen)

def release(command):
    side = command.get('side')
    if side == 'left':
        mouseC.release(Button.left)
    else:
        mouseC.release(Button.right)

def scroll(command):
    dy = command.get('dy')
    dx = command.get('dx')
    mouseC.scroll(dx or 0, dy or 0)

options = {
    "move":move,
    "press":press,
    "release":release,
    "scroll":scroll
}

def handler(type):
    return options.get(type)