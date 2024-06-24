from dataclasses import dataclass

from core.constants import VALID_LETTERS


@dataclass(frozen=True)
class Letter:
    value: str

    def __post_init__(self):
        self.__validate_value()

    def __validate_value(self):
        if not isinstance(self.value, str):
            raise ValueError("Letter value should be a string")

        if not self.value.isalpha():
            raise ValueError("Letter value should be a text")

        if len(self.value) != 1:
            raise ValueError("Letter value's length should equal to one")

        if self.value not in VALID_LETTERS:
            raise ValueError(f"{self.value} value should be a valid letter")
