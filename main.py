from title import title_screen
from game import game
from victory import victory_screen


def main():
    board = title_screen()

    game(board)

    victory_screen(board)


if __name__ == "__main__":
    main()
