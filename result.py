import pygame
from tools import quit_game, blit_text_center

WIDTH = 400
HEIGHT = 200

BG_COLOR = (255, 255, 255)


def draw(window, winner):
    window.fill(BG_COLOR)
    blit_text_center(window, f"PLAYER {winner} WINS!")


def result_screen(winner):
    window = pygame.display.set_mode((WIDTH, HEIGHT))

    draw(window, winner)
    unpause = False
    while not unpause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
