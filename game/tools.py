from game2048 import Game2048
from game2048 import Direction
from abc import ABC

class Tools(ABC):
    def print_board(self, game: Game2048) -> None:
        """
        Send game board to Screen
        """
        pass

    def handle_buttons(self) -> Direction|None:
        """
        Handle movement by buttons

        This method should be non-blocking!
        """
        pass

    def handle_reset(self) -> bool:
        """
        This method should be non-blocking!

        :return True if game should be restarted
        """
        pass