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

    def check_win(self):
        # check diagonal
        for r, row in enumerate(self.array[:len(self.array) - 4]):
            for t, tile in enumerate(row[:len(row) - 4]):
                # y = x
                condition = (self.array[r][t] == self.array[r + 1][t + 1] and
                             self.array[r + 1][t + 1] == self.array[r + 2][t + 2] and
                             self.array[r + 2][t + 2] == self.array[r + 3][t + 3] and
                             self.array[r + 3][t + 3] == self.array[r + 4][t + 4] and
                             tile != 0)

                if condition:
                    print(f"Player {tile} wins")

                # y = -x
                condition = (self.array[r][t + 4] == self.array[r + 1][t + 3] and
                             self.array[r + 1][t + 3] == self.array[r + 2][t + 2] and
                             self.array[r + 2][t + 2] == self.array[r + 3][t + 1] and
                             self.array[r + 3][t + 1] == self.array[r + 4][t] and
                             self.array[r][t + 4] != 0)

                if condition:
                    print(f"Player {self.array[r][t + 4]} wins")

        # check row
        for r, row in enumerate(self.array):
            for t, tile in enumerate(row[:len(row) - 4]):
                condition = (self.array[r][t] == self.array[r][t + 1] and
                             self.array[r][t + 1] == self.array[r][t + 2] and
                             self.array[r][t + 2] == self.array[r][t + 3] and
                             self.array[r][t + 3] == self.array[r][t + 4] and
                             tile != 0)

                if condition:
                    print(f"Player {tile} wins")

        # check column
        for r, row in enumerate(self.array[:len(self.array) - 4]):
            for t, tile in enumerate(row):

                condition = (self.array[r][t] == self.array[r + 1][t] and
                             self.array[r + 1][t] == self.array[r + 2][t] and
                             self.array[r + 2][t] == self.array[r + 3][t] and
                             self.array[r + 3][t] == self.array[r + 4][t] and
                             tile != 0)
                if condition:
                    print(f"Player {tile} wins")
