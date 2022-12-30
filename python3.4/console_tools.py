from game2048 import Game2048
from game2048 import Direction

class ConsoleTools:
    def _transform_color(self, value):
        if value == 0:
            return [255, 255, 255]
        elif value == 2:
            return [128, 0, 0]
        elif value == 4:
            return [170, 255, 195]
        elif value == 8:
            return [128, 128, 0]
        elif value == 16:
            return [0, 128, 128]
        elif value == 32:
            return [0, 0, 128]
        elif value == 64:
            return [230, 25, 75]
        elif value == 128:
            return [245, 130, 48]
        elif value == 256:
            return [210, 245, 60]
        elif value == 512:
            return [145, 30, 180]
        elif value == 1024:
            return [70, 240, 240]
        elif value == 2048:
            return [240, 50, 230]

    def print_board(self, game):
        max_digits = len(str(max(game.flatten())))
        for row in game.fields:
            for field in row:
                transformed = self._transform_color(field)
                r = transformed[0]
                g = transformed[1]
                b = transformed[2]
                n_spaces = (max_digits - len(str(field)) + 1)
                end = ''
                for _ in range(n_spaces):
                    end += ' '
                print('\033[38;2;{r};{g};{b}m{field}\033[m'.format(r=r, g=g, b=b, field=field), end = end)
            print()

    def handle_buttons(self):
        d = input('[U/D/L/R/RESET]: ').upper()
        if d == 'U':
            return Direction.UP
        elif d == 'D':
            return Direction.DOWN
        elif d == 'L':
            return Direction.LEFT
        elif d == 'R':
            return Direction.RIGHT
        elif d == 'RESET':
            return -100
        return None

