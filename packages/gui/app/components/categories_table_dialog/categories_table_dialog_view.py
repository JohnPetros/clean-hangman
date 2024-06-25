from flet import (
    AlertDialog,
    Text,
    TextAlign,
    Row,
    Column,
    Container,
    icons,
)

from gui.app.types import Callback

from .category_button_click.category_button_click_view import category_button_click_view
from .categories_table_dialog_controller import CategoriesTableDialogController


def categories_table_dialog_view(on_choose: Callback):
    dialog = AlertDialog(
        modal=True,
        title=Text(
            "Pick one of the following categories:",
            color="#9580FF",
            text_align=TextAlign.CENTER,
        ),
        bgcolor="#22212C",
    )

    categories_table_dialog_controller = CategoriesTableDialogController(
        dialog, on_choose
    )

    rows = [
        Row(
            [
                category_button_click_view(
                    "Programming",
                    icons.COMPUTER,
                    categories_table_dialog_controller.handle_category_button_click,
                ),
                category_button_click_view(
                    "Animals",
                    icons.PETS,
                    categories_table_dialog_controller.handle_category_button_click,
                ),
            ],
        ),
        Row(
            [
                category_button_click_view(
                    "Countries",
                    icons.PUBLIC,
                    categories_table_dialog_controller.handle_category_button_click,
                ),
                category_button_click_view(
                    "Fruits",
                    icons.RICE_BOWL,
                    categories_table_dialog_controller.handle_category_button_click,
                ),
            ],
        ),
        Row(
            [
                category_button_click_view(
                    "Sports",
                    icons.SPORTS_SOCCER,
                    categories_table_dialog_controller.handle_category_button_click,
                ),
                category_button_click_view(
                    "Objects",
                    icons.CHAIR,
                    categories_table_dialog_controller.handle_category_button_click,
                ),
            ],
        ),
    ]

    dialog.content = Container(Column(rows), expand=True, height=140)

    return dialog
