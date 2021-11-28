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
