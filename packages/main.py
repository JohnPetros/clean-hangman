from sys import argv

from gui import init_gui
from cli import init_cli


def main():
    if len(argv) > 1 and argv[1] == "gui":
        init_gui()
    else:
        init_cli()


if __name__ == "__main__":
    main()
