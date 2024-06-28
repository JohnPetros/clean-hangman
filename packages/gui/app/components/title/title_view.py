from flet import Text, Row, colors


def title_view():
    return Row(
        [Text(value="Clean Hangman", size=32, color=colors.WHITE)],
        alignment="center",
    )
