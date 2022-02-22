import pygame
from tools import blit_text_center, quit_game


WIDTH = 200
HEIGHT = 100

BG_COLOR = (255, 255, 255)


def victory_screen(board):
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    done = False
    while not done:
        clock.tick(30)

        window.fill(BG_COLOR)
        blit_text_center(window, f"PLAYER {board.winner} WINS!")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
