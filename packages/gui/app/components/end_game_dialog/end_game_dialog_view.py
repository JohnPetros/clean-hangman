from flet import (
    AlertDialog,
    Text,
    Row,
    TextAlign,
    FontWeight,
    ElevatedButton,
    MainAxisAlignment,
    colors,
)

from gui.app.types import Callable


def end_game_dialog_view(is_win: bool, correct_word: str, on_reset: Callable):
    correct_word_text = Text(
        correct_word.upper(), size=24, color=colors.WHITE, weight=FontWeight.W_700
    )

    message = None

    if is_win:
        message = Text("You won 😆! The word was: ", size=24, color=colors.GREEN_400)
    else:
        message = Text("You lost 😢! The word was: ", size=24, color=colors.RED_400)

    dialog = AlertDialog(
        modal=True,
        title=Text(
            "Game Over",
            color="#9580FF",
            text_align=TextAlign.CENTER,
        ),
        content=Row([message, correct_word_text]),
        bgcolor="#22212C",
        actions=[ElevatedButton("Reset Game", on_click=on_reset)],
        actions_alignment=MainAxisAlignment.CENTER,
    )

    dialog.open = True

    return dialog
