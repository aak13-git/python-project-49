from brain_games.common.utils import (
    get_name,
    greet,
    welcome,
)


def main():
    welcome()
    name = get_name()
    greet(name)


if __name__ == "__main__":
    main()
