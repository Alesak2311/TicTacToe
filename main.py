from title import title_screen
from game import game


def main():
    board = title_screen()

    game(board)


if __name__ == "__main__":
    main()
