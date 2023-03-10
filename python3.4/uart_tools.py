from game2048 import Game2048
from game2048 import Direction

class UARTTools:
    def __init__(self, funduino, keypad):
        self.fuduino = funduino
        self.keypad = keypad

    def _translate(self, fields):
        """
        Translate numbers to serial bytes understanded by Screen
        """
        out = b''
        for e in fields:
            if e == 0:
                out += b'0'
            elif e == 2:
                out += b'1'
            elif e == 4:
                out += b'2'
            elif e == 8:
                out += b'3'
            elif e == 16:
                out += b'4'
            elif e == 32:
                out += b'5'
            elif e == 64:
                out += b'6'
            elif e == 128:
                out += b'7'
            elif e == 256:
                out += b'8'
            elif e == 512:
                out += b'9'
            elif e == 1024:
                out += b'A'
            elif e == 2048:
                out += b'B'
        return out

    def print_board(self, game):
        self.fuduino.write(self._translate(game.flatten()))

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
