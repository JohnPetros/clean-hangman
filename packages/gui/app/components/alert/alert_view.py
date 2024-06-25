from flet import Banner, Icon, Text, TextButton, ButtonStyle, icons, colors

from gui.app.types import Callback


def alert_view(message: str, on_close: Callback):
    banner = Banner(
        bgcolor=colors.RED_100,
        leading=Icon(icons.WARNING_AMBER_ROUNDED, color=colors.RED_600, size=40),
        content=Text(
            value=message,
            color=colors.RED_300,
        ),
        actions=[
            TextButton(
                text="OK",
                style=ButtonStyle(color=colors.BLACK),
                on_click=lambda _: on_close(banner),
            ),
        ],
    )

    return banner
