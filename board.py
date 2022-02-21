import numpy as np
import pygame.image

SPRITE = {0: pygame.image.load("assets/tile-empty.png"),
          1: pygame.image.load("assets/tile-o.png"),
          2: pygame.image.load("assets/tile-x.png")}


class Board:
    def __init__(self, size):
        self.size = size

        self.array = np.zeros((size, size), dtype=np.int64)

    def draw_board(self, window):
        for r, row in enumerate(self.array):
            for t, tile in enumerate(row):
                window.blit(SPRITE[tile], (t * 40, r * 40))

    def place_o(self, tile):
        self.array[tile[1]][tile[0]] = 1

    def place_x(self, tile):
        self.array[tile[1]][tile[0]] = 2


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


class SingleBoard(Board):
    pass
