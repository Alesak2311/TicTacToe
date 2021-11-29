import pygame
from math import ceil
from tools import quit_game
from random import randint

BG_COLOR = (255, 255, 255)

HIGHLIGHT = pygame.image.load("assets/tile-highlight.png")


def get_tile():
    mouse_pos = pygame.mouse.get_pos()
    tile = tuple(map(lambda coord: ceil(coord / 40) - 1, mouse_pos))
    return tile


def highlight_tile(window, tile):
    highlight_pos = tuple(map(lambda coord: coord * 40, tile))
    window.blit(HIGHLIGHT, highlight_pos)


def draw(window, board, tile):
    window.fill(BG_COLOR)

    board.draw_board(window)

    highlight_tile(window, tile)

    pygame.display.update()


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
