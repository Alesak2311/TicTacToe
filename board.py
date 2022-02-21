import numpy as np
import pygame.image
from line import OLine, XLine

SPRITE = {0: pygame.image.load("assets/tile-empty.png"),
          1: pygame.image.load("assets/tile-o.png"),
          2: pygame.image.load("assets/tile-x.png")}


class Board:
    def __init__(self, size):
        self.size = size

        self.array = np.zeros((size, size), dtype=np.int64)
        self.search_area = self.array

        self.o_lines = []
        self.x_lines = []

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

        self.search_area = np.zeros((bottom - top + 8, right - left + 8), dtype=np.int64)
        self.search_area[4:-4, 4:-4] = self.array[top:bottom, left:right]

    def scan_lines(self):
        self.o_lines = []
        self.x_lines = []

        for r, row in enumerate(self.search_area):
            for c, column in enumerate(row):
                if column == 1:
                    for direction in range(8):
                        self.o_lines.append(OLine(self.search_area, (r, c), direction))
                if column == 2:
                    for direction in range(8):
                        self.x_lines.append(XLine(self.search_area, (r, c), direction))


class MultiBoard(Board):
    def __init__(self, size):
        super().__init__(size)

        self.turn_o = True

    def place_tile(self, tile):
        if not self.array[tile[1]][tile[0]] == 0:
            return

        if self.turn_o:
            self.place_o(tile)
        else:
            self.place_x(tile)
        self.turn_o = not self.turn_o

        self.shrink_area()
        self.scan_lines()


class SingleBoard(Board):
    pass
