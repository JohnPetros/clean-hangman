from dataclasses import dataclass


@dataclass(frozen=True)
class AtemptsCount:
    value: int

    def __post_init__(self):
        self.__validate_value()

    def decrement(self):
        return AtemptsCount(self.value - 1)

    def __validate_value(self):
        if not isinstance(self.value, int):
            raise ValueError("Attempts count value should be a integer")

        if self.value < 0:
            raise ValueError("Attempts count value should be greater than zero")
