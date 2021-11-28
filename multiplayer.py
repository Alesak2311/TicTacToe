import pygame
from math import ceil
from tools import quit_game

BG_COLOR = (255, 255, 255)

HIGHLIGHT = pygame.image.load("assets/tile-highlight.png")


def highlight_tile(window):
    mouse_pos = pygame.mouse.get_pos()
    tile = tuple(map(lambda coord: ceil(coord / 40) - 1, mouse_pos))
    highlight_pos = tuple(map(lambda coord: coord * 40, tile))

    window.blit(HIGHLIGHT, highlight_pos)


def draw(window, board):
    window.fill(BG_COLOR)

    board.draw_board(window)

    highlight_tile(window)

    pygame.display.update()


def multiplayer(mode):
    width = height = mode.board.size * 40
    window = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    done = False
    while not done:
        clock.tick(30)

        draw(window, mode.board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
