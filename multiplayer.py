import pygame
from tools import quit_game, get_tile, draw


def multiplayer(mode):
    width = height = mode.board.size * 40
    window = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    done = False
    player_o = True
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
                    if player_o:
                        mode.board.array[x][y] = 1
                    else:
                        mode.board.array[x][y] = 2
                    winner = mode.board.check_win()

                    player_o = not player_o
        if winner is not None:
            pygame.display.quit()
            return winner
