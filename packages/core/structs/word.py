from dataclasses import dataclass


from .letter import Letter


@dataclass(frozen=True)
class Word:
    letters: list[Letter]

    def __post_init__(self):
        self.__validate_letters()

    def includes_letter(self, letter: Letter):
        for current_letter in self.letters:
            if letter.value == current_letter.value:
                return True

        return False

    @staticmethod
    def create(word_value: str):
        letters = [Letter(letter_value) for letter_value in word_value]

        return Word(letters)

    @property
    def length(self):
        return len(self.letters)

    @property
    def value(self):
        value = "".join([letter.value for letter in self.letters])
        return value

    def __validate_letters(self):
        are_valid_letters = isinstance(self.letters, list) and all(
            isinstance(letter, Letter) for letter in self.letters
        )

        if not are_valid_letters:
            raise ValueError("Word letters should be a list of valid letters")
