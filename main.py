from title import title_screen
from multiplayer import multiplayer


def main():
    mode = title_screen()

    if mode.game_mode == 2:
        multiplayer(mode)


if __name__ == "__main__":
    main()
