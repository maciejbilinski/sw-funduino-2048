from game2048 import Game2048
from game2048 import Direction

# Print output in terminal but use keypad input
class KeypadTools:
    def __init__(self, keypad):
        self.keypad = keypad

    def handle_buttons(self):
        button = self.keypad.readline()
        button = button.strip()
        if button == '2':
            return Direction.UP
        elif button == '4':
            return Direction.LEFT
        elif button == '6':
            return Direction.RIGHT
        elif button == '8':
            return Direction.DOWN
        elif button == 'D':
            return -100
        return None
