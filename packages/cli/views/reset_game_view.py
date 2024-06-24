from rich.text import Text
from rich.panel import Panel
from rich.align import Align
from rich.columns import Columns

from cli.utils import console


def reset_game_view():
    reset_game_text = Text(
        "Type 'reset' to reset the game", justify="center", style="cyan"
    )

    console.print(Align(Columns([Panel(reset_game_text, width=40)]), "center"))
