from dataclasses import dataclass

from .word import Word
from .attempts_count import AtemptsCount
from .blanks_group import BlanksGroup
from .category import Category
from .letter import Letter
from ..constants import INITIAL_ATTEMPTS_COUNT


@dataclass(frozen=True)
class Game:
    correct_word: Word
    blanks_group: BlanksGroup
    attempts_count: AtemptsCount
    used_letters: list[str]

    @staticmethod
    def create(category: Category):
        correct_word = category.random_word

        blanks_group = BlanksGroup.create(word_value=correct_word.value)
        attempts_count = AtemptsCount(INITIAL_ATTEMPTS_COUNT)

        return Game(
            correct_word=correct_word,
            blanks_group=blanks_group,
            attempts_count=attempts_count,
            used_letters=[],
        )

    def input_letter(self, user_letter: str):
        letter = Letter(user_letter)

        used_letters = self.used_letters

        if user_letter in used_letters:
            raise ValueError(f"Letter {user_letter.upper()} has already been used")

        used_letters.append(letter.value)

        if self.correct_word.includes_letter(user_letter):
            return self.__reveal_letter(user_letter, used_letters)
        else:
            return self.__decrement_attempts_count(used_letters)

    def check_lose(self):
        return self.attempts_count.value == 0

    def check_win(self):
        return self.correct_word.value == self.blanks_group.formed_word

    def __reveal_letter(self, user_letter: str, used_letters: list[str]):
        return Game(
            correct_word=self.correct_word,
            attempts_count=self.attempts_count,
            blanks_group=self.blanks_group.reveal_letter(user_letter),
            used_letters=used_letters,
        )

    def __decrement_attempts_count(self, used_letters: list[str]):
        return Game(
            correct_word=self.correct_word,
            attempts_count=self.attempts_count.decrement(),
            blanks_group=self.blanks_group,
            used_letters=used_letters,
        )
