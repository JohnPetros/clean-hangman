from flet import Column, Image, Row, Text, MainAxisAlignment, colors

from gui.app.constants import DIRECTORIES

HANGMAN_LIMBS = ["hang", "head", "right-hand", "left-hand", "right-leg", "left-leg"]


def hangman_view(attempts_count: int):
    limb = HANGMAN_LIMBS[-attempts_count + 5]

    image = Image(src=f"{DIRECTORIES.assets}/{limb}.svg", height=250)

    attempts_count_text = Row(
        [
            Text("Left attempts: ", color=colors.WHITE, size=16),
            Text(attempts_count, color=colors.CYAN_400, size=16),
        ]
    )

    return Row(
        [
            Column(
                [
                    image,
                    attempts_count_text,
                ],
            )
        ],
        alignment=MainAxisAlignment.CENTER,
    )
