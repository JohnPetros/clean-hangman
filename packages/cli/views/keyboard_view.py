from rich.panel import Panel
from rich.padding import Padding
from rich.align import Align
from rich.columns import Columns

from core.constants import VALID_LETTERS

from cli.utils import console
from cli.views.reset_game_view import reset_game_view


def get_letter_panel(letter: str, correct_letters: list[str], used_letters: list[str]):
    correct_letters = [letter.lower() for letter in correct_letters]
    used_letters = [letter.lower() for letter in used_letters]

    color = ""
    if letter.lower() in correct_letters and letter.lower() in used_letters:
        color = "green"
    elif letter.lower() in used_letters:
        color = "red"

    return Panel(letter.upper(), style=color)


def keyboard_view(correct_letters: str, used_letters: list[str]):
    fist_row_panels = [
        get_letter_panel(letter, correct_letters, used_letters)
        for letter in VALID_LETTERS[:10]
    ]

    second_row_panels = [
        get_letter_panel(letter, correct_letters, used_letters)
        for letter in VALID_LETTERS[10:19]
    ]

    third_row_panels = [
        get_letter_panel(letter, correct_letters, used_letters)
        for letter in VALID_LETTERS[19:]
    ]

    first_columns = Columns(fist_row_panels)
    second_columns = Padding(Columns(second_row_panels), pad=(0, 0, 0, 10))
    third_columns = Padding(Columns(third_row_panels), pad=(0, 0, 0, 16))

    console.print("\n")

    console.print(Align(first_columns, "center"))
    console.print(Align(second_columns, "center"))
    console.print(Align(third_columns, "center"))

    reset_game_view()
