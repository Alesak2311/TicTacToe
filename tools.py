import pygame
import sys

BLACK = (0, 0, 0)

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
