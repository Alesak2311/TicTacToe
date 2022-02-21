import pygame
from tools import blit_text_center, blit_text, quit_game
from mode import Mode
from board import MultiBoard, SingleBoard

WIDTH = 800
HEIGHT = 400

BG_COLOR = (255, 255, 255)

OPTIONS = ("Quit", "Single-player", "Multiplayer")


def draw(window, selected):
    window.fill(BG_COLOR)
    blit_text_center(window, "Title screen")
    blit_text(window, "Use arrows to select and space to confirm", (0, 0))

    for i, option in enumerate(OPTIONS):
        text_pos = (10, HEIGHT - (i + 1) * 22)

        blit_text(window, option, text_pos)

        if i == selected:
            indicator_pos = (0, HEIGHT - (i + 1) * 22)
            blit_text(window, ">", indicator_pos)


def title_screen():
    if not pygame.get_init():
        pygame.init()

    window = pygame.display.set_mode((WIDTH, HEIGHT))

    selected = len(OPTIONS) - 1

    done = False
    while not done:
        draw(window, selected)

        unpause = False
        while not unpause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game()

                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()

                    if keys[pygame.K_UP]:
                        if selected == len(OPTIONS) - 1:
                            selected = 0
                        else:
                            selected += 1
                        unpause = True
                        break

                    if keys[pygame.K_DOWN]:
                        if selected == 0:
                            selected = len(OPTIONS) - 1
                        else:
                            selected -= 1
                        unpause = True
                        break

                    if keys[pygame.K_SPACE]:
                        unpause = True
                        done = True
                        break
    pygame.display.quit()

    if selected == 0:
        quit_game()

    size = 20

    if selected == 2:
        return MultiBoard(size)
    else:
        return SingleBoard(size)
