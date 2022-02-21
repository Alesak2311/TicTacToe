import numpy as np
import pygame.image

SPRITE = {0: pygame.image.load("assets/tile-empty.png"),
          1: pygame.image.load("assets/tile-o.png"),
          2: pygame.image.load("assets/tile-x.png")}


class Board:
    def __init__(self, size):
        self.size = size

        self.array = np.zeros((size, size), dtype=np.int64)
        self.search_area = self.array

    def draw_board(self, window):
        for r, row in enumerate(self.array):
            for t, tile in enumerate(row):
                window.blit(SPRITE[tile], (t * 40, r * 40))

    def place_o(self, tile):
        self.array[tile[1]][tile[0]] = 1

    def place_x(self, tile):
        self.array[tile[1]][tile[0]] = 2

    def shrink_top(self):
        for r, row in enumerate(self.array):
            if 1 in row or 2 in row:
                return r

    def shrink_bottom(self):
        for r, row in reversed(list(enumerate(self.array))):
            if 1 in row or 2 in row:
                return r + 1

    def shrink_left(self):
        for column in range(len(self.array[0])):
            for row in self.array:
                if row[column] == 1 or row[column] == 2:
                    return column

    def shrink_right(self):
        for column in reversed(range(len(self.array[0]))):
            for row in self.array:
                if row[column] == 1 or row[column] == 2:
                    return column + 1

    def shrink_area(self):
        top = self.shrink_top()
        bottom = self.shrink_bottom()
        left = self.shrink_left()
        right = self.shrink_right()

        self.search_area = self.array[top:bottom, left:right]


class MultiBoard(Board):
    def __init__(self, size):
        super().__init__(size)

        self.turn = 1

    def place_tile(self, tile):
        if not self.array[tile[1]][tile[0]] == 0:
            return

        if self.turn == 1:
            self.place_o(tile)
            self.turn = 2
        else:
            self.place_x(tile)
            self.turn = 1

        self.shrink_area()


class SingleBoard(Board):
    pass
