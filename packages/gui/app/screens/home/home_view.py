from flet import CrossAxisAlignment

from gui.app.types import UI
from gui.app.components import (
    categories_table_dialog_view,
)

from .home_controller import HomeController


def home_view(ui: UI):
    ui.title = "Hangman - A John Petros' Game"
    ui.bgcolor = "#34495E"
    ui.horizontal_alignment = CrossAxisAlignment.CENTER
    ui.window_height = 820

    home_controller = HomeController(ui)

    categories_table_dialog = categories_table_dialog_view(
        on_choose=home_controller.handle_categories_dialog_choose
    )

    ui.on_keyboard_event = home_controller.handle_key_press

    ui.overlay.append(categories_table_dialog)
    categories_table_dialog.open = True

    ui.update()
