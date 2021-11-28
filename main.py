from title import title_screen
from multiplayer import multiplayer
from result import result_screen


def main():
    mode = title_screen()

    if mode.game_mode == 2:
        winner = multiplayer(mode)
    else:
        winner = None

    result_screen(winner)


if __name__ == "__main__":
    main()
