from flet import (
    Container,
    Text,
    Row,
    Column,
    MainAxisAlignment,
    colors,
    margin,
    alignment,
)

from core.constants import VALID_LETTERS

from gui.app.types import Callback
from ..reset_game_button.reset_game_button_view import reset_game_button_view


def get_letter_key(
    letter: str,
    correct_letters: list[str],
    used_letters: list[str],
    on_click: Callback,
):
    bgcolor = colors.WHITE
    if letter.lower() in correct_letters and letter.lower() in used_letters:
        bgcolor = colors.GREEN
    elif letter.lower() in used_letters:
        bgcolor = colors.RED

    return Container(
        Text(
            letter.upper(),
            color=colors.BLACK87,
            size=16,
        ),
        width=50,
        height=50,
        border_radius=4,
        alignment=alignment.center,
        bgcolor=bgcolor,
        on_click=on_click,
    )


def keyboard_view(
    correct_letters: str, used_letters: list[str], on_key_click: Callback
):
    fist_row_keys = [
        get_letter_key(letter, correct_letters, used_letters, on_key_click)
        for letter in VALID_LETTERS[:10]
    ]

    second_row_keys = [
        get_letter_key(letter, correct_letters, used_letters, on_key_click)
        for letter in VALID_LETTERS[10:19]
    ]

    third_row_keys = [
        get_letter_key(letter, correct_letters, used_letters, on_key_click)
        for letter in VALID_LETTERS[19:]
    ]

    first_row = Row(fist_row_keys, alignment=MainAxisAlignment.CENTER, spacing=16)
    second_row = Row(second_row_keys, alignment=MainAxisAlignment.CENTER, spacing=16)
    third_row = Row(third_row_keys, alignment=MainAxisAlignment.CENTER, spacing=16)

    keyboard = Container(
        Column(
            [
                first_row,
                second_row,
                third_row,
            ],
            spacing=16,
        ),
        margin=margin.only(top=24),
    )

    return keyboard
