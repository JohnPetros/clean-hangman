from typing import Callable

from flet import AlertDialog, ControlEvent

from gui.app.stores import game_store


class CategoriesTableDialogController:
    def __init__(self, dialog: AlertDialog, on_choose: Callable):
        self.dialog = dialog
        self.on_choose = on_choose

    def handle_category_button_click(self, event: ControlEvent):
        text = event.control.content.controls[1]
        category = text.value.lower()

        game_store.category = category
        game_store.categories_table_dialog = self.dialog

        self.dialog.open = False
        self.on_choose()
