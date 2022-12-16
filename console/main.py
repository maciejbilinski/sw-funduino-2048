from game.game2048 import Game2048
from console_tools import ConsoleTools

if __name__ == "__main__":
    tools = ConsoleTools()

    while True:
        game = Game2048(4)
        while True:
            tools.print_board(game)
            if not game.win:
                direction = tools.handle_buttons()
                if direction != None:
                    game.move(direction)
            if(tools.handle_reset()):
                break
