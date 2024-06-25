from dataclasses import dataclass

from flet import AlertDialog

from core.structs import Game


@dataclass
class GameStore:
    _game: Game = None
    _category: str = None
    _categories_table_dialog: AlertDialog = None

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category: str):
        self._game = Game.create(new_category)
        self._category = new_category

    @property
    def attempts_count(self):
        return self._game.attempts_count.value

    @property
    def blanks_group(self):
        return self._game.blanks_group.value

    @property
    def correct_letters(self):
        return list(self._game.correct_word.value)

    @property
    def correct_word(self):
        return self._game.correct_word.value

    @property
    def used_letters(self):
        return self._game.used_letters

    @property
    def categories_table_dialog(self):
        return self._categories_table_dialog

    @categories_table_dialog.setter
    def categories_table_dialog(self, categories_table_dialog: AlertDialog):
        self._categories_table_dialog = categories_table_dialog

    def input_letter(self, letter: str):
        self._game = self._game.input_letter(letter)

    def check_win(self):
        return self._game.check_win()

    def check_lose(self):
        return self._game.check_lose()

    def reset_game(self):
        self._categories_table_dialog.open = True
        self._game = None
