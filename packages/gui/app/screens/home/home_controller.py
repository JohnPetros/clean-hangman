from flet import ControlEvent, KeyboardEvent, Banner

from gui.app.types import UI
from gui.app.components import (
    title_view,
    hangman_view,
    blanks_group_view,
    keyboard_view,
    reset_game_button_view,
    end_game_dialog_view,
    alert_view,
)
from gui.app.stores import game_store


class HomeController:
    def __init__(self, ui: UI):
        self.ui = ui

    def get_game_ui(self):
        category = game_store.category
        blanks_group = game_store.blanks_group
        correct_letters = game_store.correct_letters
        used_letters = game_store.used_letters
        attempts_count = game_store.attempts_count

        return (
            title_view(),
            hangman_view(attempts_count),
            blanks_group_view(category, blanks_group),
            keyboard_view(
                correct_letters=correct_letters,
                used_letters=used_letters,
                on_key_click=self.handle_key_click,
            ),
            reset_game_button_view(on_click=self.handle_reset_button_click),
        )

    def handle_categories_dialog_choose(self):
        self.__update_game_ui(should_remove_previous_ui=False)

    def handle_key_click(self, event: ControlEvent):
        letter = event.control.content.value
        self.__input_letter(letter)

    def handle_key_press(self, event: KeyboardEvent):
        letter = event.key
        self.__input_letter(letter)

    def handle_reset_button_click(self, _):
        self.__remove_previous_game_ui()
        game_store.reset_game()
        self.ui.update()

    def handle_close_alert(self, banner: Banner):
        self.ui.close(banner)

    def __input_letter(self, letter: str):
        try:
            game_store.input_letter(letter.lower())
        except ValueError as error:
            self.ui.open(alert_view(error, on_close=self.handle_close_alert))

        if game_store.check_win():
            self.__open_end_game_dialog(is_win=True)
        elif game_store.check_lose():
            self.__open_end_game_dialog(is_win=False)
        else:
            self.__update_game_ui()

    def __open_end_game_dialog(self, is_win: bool):
        self.__remove_previous_game_ui()

        self.ui.add(
            end_game_dialog_view(
                is_win,
                correct_word=game_store.correct_word,
                on_reset=self.handle_reset_button_click,
            )
        )
        self.ui.update()

    def __update_game_ui(self, should_remove_previous_ui: bool = True):
        if should_remove_previous_ui:
            self.__remove_previous_game_ui()

        game_ui = self.get_game_ui()
        self.ui.add(*game_ui)
        self.ui.update()

    def __remove_previous_game_ui(self):
        for _ in range(len(self.ui.controls)):
            self.ui.controls.pop()
