from time import sleep

from art import tprint

from rich.align import Align

from cli.utils import console


def exit_game_view():
    console.print("\n")

    with console.status(Align("Exiting...", "center", width=50), spinner="monkey"):
        sleep(2)

    tprint("BY BY")
    tprint("Made by Petros", space=2)
