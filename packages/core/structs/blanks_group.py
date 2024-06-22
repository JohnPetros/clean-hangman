from dataclasses import dataclass

from .word import Word


@dataclass(frozen=True)
class BlanksGroup:
    value: list[str]
    word: Word

    def __post_init__(self):
        self.__validate_value()

    @staticmethod
    def create(word_value: str, value: list[str] | None = None):
        word = Word.create(word_value)

        if value is None:
            value = ["_" for _ in range(word.length)]

        return BlanksGroup(word=word, value=value)

    @property
    def formed_word(self):
        return "".join(self.value)

    def reveal_letter(self, revealed_letter_value: str):
        current_value = self.value

        for index, letter in enumerate(self.word.letters):
            if letter.value == revealed_letter_value:
                current_value[index] = revealed_letter_value

        return BlanksGroup.create(self.word.value, current_value)

    def __validate_value(self):
        is_valid_value = isinstance(self.value, list) or all(
            isinstance(letter, str) for letter in self.value
        )

        if not is_valid_value:
            raise ValueError("Blanks group should be a list")
