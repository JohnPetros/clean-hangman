from typing import Callable

from flet import (
    Text,
    Row,
    Container,
    MainAxisAlignment,
    Icon,
    colors,
    alignment,
)


def category_button_view(title: str, icon: str, on_click: Callable):
    return Container(
        Row(
            [
                Icon(icon, size=24, color=colors.WHITE),
                Text(title, size=16, color=colors.WHITE),
            ],
            alignment=MainAxisAlignment.CENTER,
        ),
        height=48,
        bgcolor="#34495E",
        border_radius=8,
        expand=1,
        alignment=alignment.center,
        on_click=on_click,
    )
