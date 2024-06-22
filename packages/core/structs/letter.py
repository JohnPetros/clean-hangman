from dataclasses import dataclass


@dataclass(frozen=True)
class Letter:
    value: str

    def __post_init__(self):
        if not isinstance(self.value, str):
            raise ValueError("Letter error should be a string")
