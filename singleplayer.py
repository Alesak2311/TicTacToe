import pygame
from tools import quit_game, get_tile, draw
from random import randint


def computer_tile(board):
    x = randint(0, board.size - 1)
    y = randint(0, board.size - 1)
    while board.array[x][y] != 0:
        x = randint(0, board.size - 1)
        y = randint(0, board.size - 1)

    return y, x


def single_player(mode):
    width = height = mode.board.size * 40
    window = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    done = False
    winner = None
    while not done:
        clock.tick(30)

        tile = get_tile()
        draw(window, mode.board, tile)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

            if event.type == pygame.MOUSEBUTTONDOWN:
                y, x = tile
                if mode.board.array[x][y] == 0:
                    mode.board.array[x][y] = 1

                    y, x = computer_tile(mode.board)
                    mode.board.array[x][y] = 2

                    winner = mode.board.check_win()

        if winner is not None:
            pygame.display.quit()
            return winner
