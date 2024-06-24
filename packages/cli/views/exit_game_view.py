from time import sleep

from rich.align import Align

from cli.utils import console


def exit_game_view():
    with console.status(Align("Exiting...", "center"), spinner="monkey"):
        sleep(2)

    console.print("[yellow on blue]By by 👋🏻![/]")
