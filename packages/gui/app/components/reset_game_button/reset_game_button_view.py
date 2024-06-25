from flet import Container, ElevatedButton, Row, colors, margin

from gui.app.types import Callback


def reset_game_button_view(on_click: Callback):
    button = ElevatedButton(
        "Reset game",
        color=colors.WHITE,
        bgcolor=colors.BLACK54,
        height=40,
        on_click=on_click,
    )

    return Container(
        Row(
            [button],
            alignment="center",
        ),
        margin=margin.only(top=32),
    )
