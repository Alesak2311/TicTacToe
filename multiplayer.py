import pygame
from tools import quit_game

BG_COLOR = (255, 255, 255)


def draw(window, mode):
    window.fill(BG_COLOR)

    mode.board.draw_board(window)

    pygame.display.update()


def multiplayer(mode):
    width = height = mode.board.size * 40
    window = pygame.display.set_mode((width, height))

    draw(window, mode)

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
