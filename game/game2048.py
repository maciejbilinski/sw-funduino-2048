import random
from enum import IntEnum
import numpy as np

class Direction(IntEnum):
    UP = 1
    LEFT = 2
    RIGHT = -2
    DOWN = -1

class Game2048:
    def __init__(self, n: int = 4) -> None:
        """
        Init and set two random places
        """
        self.fields = np.zeros((n, n), dtype=int)
        self._gen_random(2)
        self.win = False

    @property
    def n(self):
        return self.fields.shape[0]

    def _gen_random(self, x: int = 1) -> None:
        """
        Set in 'x' random places with 2 or 4
        """
        available = []
        for row in range(self.n):
            for field, value in enumerate(self.fields[row]):
                if value == 0:
                    available.append((row, field))

        if len(available) <= (x-1):
            raise Exception('Game lost')

        random.shuffle(available)

        for i in range(x):
            pos = available[i]
            self.fields[pos[0], pos[1]] = [2, 4][random.randint(0, 1)]

    def _shift(self, direction: Direction) -> int:
        """
        Shift tiles in property direction

        :return Number of moved tiles
        """
        counter = 0

        old_fields = self.fields
        if direction == Direction.RIGHT:
            old_fields = np.flip(old_fields, 1)
        elif direction == Direction.UP:
            old_fields = old_fields.T
        elif direction == Direction.DOWN:
            old_fields = np.flip(old_fields.T, 1)
        self.fields = np.zeros((self.n, self.n), dtype=int)

        for i in range(self.n):
            pos = 0
            for j in range(self.n):
                if old_fields[i, j] != 0:
                    self.fields[i, pos] = old_fields[i, j]
                    if j != pos:
                        counter += 1
                    pos += 1

        if direction == Direction.RIGHT:
            self.fields = np.flip(self.fields, 1)
        elif direction == Direction.UP:
            self.fields = self.fields.T
        elif direction == Direction.DOWN:
            self.fields = np.flip(self.fields, 1).T

        return counter

    def _merge(self, direction: Direction) -> tuple[int, bool]:
        """
        Marge the same tiles in property direction

        :return Number of moved tiles, win indicator
        """
        counter = 0
        win = False

        if direction == Direction.RIGHT:
            self.fields = np.flip(self.fields, 1)
        elif direction == Direction.UP:
            self.fields = self.fields.T
        elif direction == Direction.DOWN:
            self.fields = np.flip(self.fields.T, 1)

        for i in range(self.n):
            for j in range(self.n-1):
                if self.fields[i, j] == self.fields[i, j + 1] and self.fields[i, j] != 0:
                    self.fields[i, j] = self.fields[i, j] * 2
                    self.fields[i][j + 1] = 0
    
                    counter += 1
                    if self.fields[i, j] == 2048:
                        win = True

        if direction == Direction.RIGHT:
            self.fields = np.flip(self.fields, 1)
        elif direction == Direction.UP:
            self.fields = self.fields.T
        elif direction == Direction.DOWN:
            self.fields = np.flip(self.fields, 1).T

        return counter, win

    def move(self, direction: Direction) -> None:
        """
        Execute move in property direction & set win property
        """
        counter = self._shift(direction)
        i, win = self._merge(direction)
        counter += self._shift(direction)
        if (i+counter) >= 1:
            self._gen_random(1)

        if not self.win and win:
            self.win = True
    
    def flatten(self) -> list[int]:
        """
        :return Flatten 2d array of fields
        """
        return self.fields.flatten().tolist()

