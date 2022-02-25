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

        self.o_lines = []
        self.x_lines = []

        self.winner = None

    def draw_board(self, window):
        for r, row in enumerate(self.array):
            for t, tile in enumerate(row):
                window.blit(SPRITE[tile], (t * 40, r * 40))

    def place_o(self, tile):
        self.array[tile[1]][tile[0]] = 1

        self.scan_lines()
        self.check_win()

    def place_x(self, tile):
        self.array[tile[1]][tile[0]] = 2

        self.scan_lines()
        self.check_win()

    def scan_o_lines(self):
        for r, row in enumerate(self.array):
            for c, column in enumerate(row):
                if column == 1:
                    for direction in range(8):
                        line = OLine(self.array, (r, c), direction)
                        if line.value > 0:
                            self.o_lines.append(line)

    def scan_x_lines(self):
        for r, row in enumerate(self.array):
            for c, column in enumerate(row):
                if column == 2:
                    for direction in range(8):
                        line = XLine(self.array, (r, c), direction)
                        if line.value > 0:
                            self.x_lines.append(line)

    def scan_lines(self):
        self.o_lines = []
        self.x_lines = []

        self.scan_o_lines()
        self.scan_x_lines()

        self.o_lines.sort(key=lambda x: x.value, reverse=True)
        self.x_lines.sort(key=lambda x: x.value, reverse=True)

    def check_win(self):
        if len(self.o_lines) > 0:
            if self.o_lines[0].value >= 5:
                self.winner = 1

        if len(self.x_lines) > 0:
            if self.x_lines[0].value >= 5:
                self.winner = 2


class MultiBoard(Board):
    def __init__(self, size):
        super().__init__(size)

        self.turn_o = True

    def place_tile(self, tile):
        if self.array[tile[1]][tile[0]] != 0:
            return

        if self.turn_o:
            self.place_o(tile)
        else:
            self.place_x(tile)
        self.turn_o = not self.turn_o


class SingleBoard(Board):
    def place_tile(self, tile):
        if self.array[tile[1]][tile[0]] != 0:
            return

        self.place_o(tile)

        if self.winner is not None:
            return

        self.place_x(self.computer_move())

    def computer_move(self):
        if len(self.x_lines) == 0:
            return self.o_lines[0].get_free()

        o_best = self.o_lines[0]
        x_best = self.x_lines[0]

        if o_best.value > x_best.value:
            move = o_best.get_free()
        else:
            move = x_best.get_free()

        return move
