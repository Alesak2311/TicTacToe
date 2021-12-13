import pygame
import sys
from math import ceil

BLACK = (0, 0, 0)
BG_COLOR = (255, 255, 255)

HIGHLIGHT = pygame.image.load("assets/tile-highlight.png")

pygame.font.init()
MAIN_FONT = pygame.font.SysFont("consolas", 22)


def quit_game():
    pygame.quit()
    sys.exit()


def blit_text_center(window, string, font=MAIN_FONT):
    text = font.render(string, True, BLACK)

    text_pos = ((window.get_width() - text.get_width()) / 2,
                (window.get_height() - text.get_height()) / 2)

    window.blit(text, text_pos)
    pygame.display.update()


def blit_text(window, string, text_pos, font=MAIN_FONT):
    text = font.render(string, True, BLACK)

    window.blit(text, text_pos)
    pygame.display.update()


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
