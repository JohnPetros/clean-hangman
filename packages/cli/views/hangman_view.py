from rich.align import Align


from cli.utils import console
from cli.constants import HANGMAN_PARTS


def hangman_view(attempts_count: int):
    hangman_part = HANGMAN_PARTS[-attempts_count + 5]

    console.print(Align(f"[b]{hangman_part}[/b]", "center"))
    console.print(Align(f"Left attempts: {attempts_count}", "center"))
