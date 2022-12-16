from game.tools import Tools
from game.game2048 import Game2048
from game.game2048 import Direction

class ConsoleTools(Tools):
    def _transform_color(self, value: int) -> str:
        if value == 0:
            return (255, 255, 255)
        elif value == 2:
            return (128, 0, 0)
        elif value == 4:
            return (170, 255, 195)
        elif value == 8:
            return (128, 128, 0)
        elif value == 16:
            return (0, 128, 128)
        elif value == 32:
            return (0, 0, 128)
        elif value == 64:
            return (230, 25, 75)
        elif value == 128:
            return (245, 130, 48)
        elif value == 256:
            return (210, 245, 60)
        elif value == 512:
            return (145, 30, 180)
        elif value == 1024:
            return (70, 240, 240)
        elif value == 2048:
            return (240, 50, 230)

    def print_board(self, game: Game2048) -> None:
        max_digits = len(str(max(game.flatten())))
        for row in game.fields:
            for field in row:
                r, g, b = self._transform_color(field)
                print(f'\033[38;2;{r};{g};{b}m{field}\033[m', end = ' ' * (max_digits - len(str(field)) + 1))
            print()

    def handle_buttons(self) -> Direction|None:
        d = input('[U/D/L/R]: ').upper()
        if d == 'U':
            return Direction.UP
        elif d == 'D':
            return Direction.DOWN
        elif d == 'L':
            return Direction.LEFT
        elif d == 'R':
            return Direction.RIGHT
        return None

    def handle_reset(self) -> bool:
        d = input('Do you want to reset? [Y/N]: ').upper()
        return d == 'Y'

