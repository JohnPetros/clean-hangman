from rich import box
from rich.panel import Panel
from rich.align import Align

from cli.utils import console


def title_view():
    title_panel = Panel(
        Align(" ", "center"),
        title="CLEAN HANGMAN",
        subtitle="A John Petros' game",
        box=box.DOUBLE_EDGE,
    )

    console.print(title_panel)
