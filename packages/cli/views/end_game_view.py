from rich.text import Text
from rich.panel import Panel
from rich.align import Align

from cli.utils import console


def end_game_view(is_win: bool, correct_word: str):
    correct_word_text = Text(correct_word.upper(), style="blink b")

    if is_win:
        console.print(
            Panel(
                Align(f"You won 😆! The word was: {correct_word_text}", "center"),
                style="green",
            ),
        )
        return

    console.print(
        Panel(
            Align(f"You lost 😢! The word was: {correct_word_text}", "center"),
            style="red",
        )
    )
