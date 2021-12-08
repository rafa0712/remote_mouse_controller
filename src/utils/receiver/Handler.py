import mouse
from pynput.mouse import Controller, Button

def move(command):
    mouse.move(command['x'], command['y'])
options = {
    "move":move
}

def handler(type):
    return options.get(type)