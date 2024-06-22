from dataclasses import dataclass
from random import choice

from ..constants import CATEGORIES_WORDS
from .word import Word


@dataclass
class Category:
    value: str

    def __post_init__(self):
        if self.value not in CATEGORIES_WORDS._fields:
            raise ValueError("Category does not exist")

    @property
    def random_word(self):
        category_word_value = choice(getattr(CATEGORIES_WORDS, self.value))
        return Word.create(category_word_value)
