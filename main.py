from title import title_screen
from multiplayer import multiplayer
from singleplayer import single_player
from result import result_screen


def main():
    mode = title_screen()

    if mode.game_mode == 2:
        winner = multiplayer(mode)
    else:
        winner = single_player(mode)

    result_screen(winner)


if __name__ == "__main__":
    main()
