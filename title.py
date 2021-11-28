import pygame
from tools import blit_text_center, quit_game

WIDTH = 800
HEIGHT = 400

BG_COLOR = (255, 255, 255)


def title_screen():
    if not pygame.get_init():
        pygame.init()

    window = pygame.display.set_mode((WIDTH, HEIGHT))

    window.fill(BG_COLOR)
    blit_text_center(window, "title screen")

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

    pygame.display.update()
