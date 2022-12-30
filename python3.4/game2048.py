import random
from enum import IntEnum

class Direction(IntEnum):
    UP = 1
    LEFT = 2
    RIGHT = -2
    DOWN = -1

def zeros(n):
    arr = []
    for _ in range(n):
        arr.append([])
        for _ in range(n):
            arr[-1].append(0)
    return arr

def transpose(arr):
    output = []
    for i in range(len(arr[0])):
        row = []
        for item in arr:
            row.append(item[i])
        output.append(row)
    return output

def flip_hor(arr):
    output = []
    for i in range(len(arr)):
        output.append([])
        for j in reversed(range(len(arr[i]))):
            output[i].append(arr[i][j])
    return output

class Game2048:
    def __init__(self, n = 4):
        self.n = n
        self.fields = zeros(n)
        self._gen_random(2)
        self.win = False

    def _gen_random(self, x = 1):
        available = []
        for row in range(self.n):
            for field, value in enumerate(self.fields[row]):
                if value == 0:
                    available.append((row, field))

        if len(available) <= (x-1):
            raise Exception('Game lost - board blocked')

        random.shuffle(available)

        for i in range(x):
            pos = available[i]
            self.fields[pos[0]][pos[1]] = [2, 4][random.randint(0, 1)]

    def _shift(self, direction):
        counter = 0

        old_fields = self.fields
        if direction == Direction.RIGHT:
            old_fields = flip_hor(old_fields)
        elif direction == Direction.UP:
            old_fields = transpose(old_fields)
        elif direction == Direction.DOWN:
            old_fields = flip_hor(transpose(old_fields))
        self.fields = zeros(self.n)

        for i in range(self.n):
            pos = 0
            for j in range(self.n):
                if old_fields[i][j] != 0:
                    self.fields[i][pos] = old_fields[i][j]
                    if j != pos:
                        counter += 1
                    pos += 1

        if direction == Direction.RIGHT:
            self.fields = flip_hor(self.fields)
        elif direction == Direction.UP:
            self.fields = transpose(self.fields)
        elif direction == Direction.DOWN:
            self.fields = transpose(flip_hor(self.fields))

        return counter

    def _merge(self, direction):
        """
        Marge the same tiles in property direction

        :return Number of moved tiles, win indicator
        """
        counter = 0
        win = False

        if direction == Direction.RIGHT:
            self.fields = flip_hor(self.fields)
        elif direction == Direction.UP:
            self.fields = transpose(self.fields)
        elif direction == Direction.DOWN:
            self.fields = flip_hor(transpose(self.fields))

        for i in range(self.n):
            for j in range(self.n-1):
                if self.fields[i][j] == self.fields[i][j + 1] and self.fields[i][j] != 0:
                    self.fields[i][j] = self.fields[i][j] * 2
                    self.fields[i][j + 1] = 0
    
                    counter += 1
                    if self.fields[i][j] == 2048:
                        win = True

        if direction == Direction.RIGHT:
            self.fields = flip_hor(self.fields)
        elif direction == Direction.UP:
            self.fields = transpose(self.fields)
        elif direction == Direction.DOWN:
            self.fields = transpose(flip_hor(self.fields))

        return (counter, win)

    def move(self, direction):
        counter = self._shift(direction)
        i, win = self._merge(direction)
        counter += self._shift(direction)

        if (i+counter) >= 1:
            self._gen_random(1)
        # else move is impossible

        if not self.win and win:
            self.win = True
    
    def flatten(self):
        flatten = []
        for i in range(self.n):
            for j in range(self.n):
                flatten.append(self.fields[i][j])
        return flatten
