from dataclasses import dataclass

from .word import Word
from .attempts_count import AtemptsCount
from .blanks_group import BlanksGroup
from .category import Category
from ..constants import INITIAL_ATTEMPTS_COUNT


@dataclass(frozen=True)
class Game:
    correct_word: Word
    blanks_group: BlanksGroup
    attempts_count: AtemptsCount

    @staticmethod
    def create(category_value: str):
        category = Category(category_value)
        correct_word = category.random_word

        blanks_group = BlanksGroup.create(word_value=correct_word.value)
        attempts_count = AtemptsCount(INITIAL_ATTEMPTS_COUNT)

        return Game(
            correct_word=correct_word,
            blanks_group=blanks_group,
            attempts_count=attempts_count,
        )

    def input_letter(self, user_letter: str):
        if self.correct_word.includes_letter(user_letter):
            return self.clone(
                {"blanks_group": self.blanks_group.reveal_letter(user_letter)}
            )
        else:
            return self.clone({"attempts_count": self.attempts_count.decrement()})

    def check_lose(self):
        return self.attempts.value == 0

    def check_win(self):
        return self.correct_word.value == self.blanks_group.formed_word
