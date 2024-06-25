from flet import Text, Row, colors


def title_view():
    return Row(
        [Text(value="Hangman Game", size=32, color=colors.WHITE)],
        alignment="center",
    )
