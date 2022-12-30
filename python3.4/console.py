from game2048 import Game2048
from console_tools import ConsoleTools

if __name__ == "__main__":
    tools = ConsoleTools()

    while True:
        game = Game2048(4)
        while True:
            tools.print_board(game)
            button = tools.handle_buttons()
            if button == -100:
                break
            elif not game.win:
                if button != None:
                    game.move(button)

