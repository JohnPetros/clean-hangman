from pytest import fixture

from ..blanks_group import BlanksGroup


def describe_blanks_group():

    @fixture
    def correct_word():
        return "python"

    def should_start_with_empty_value(correct_word):
        blanks_group = BlanksGroup.create(correct_word)

        assert blanks_group.value == ["_", "_", "_", "_", "_", "_"]

    def should_reveal_letter(correct_word):
        blanks_group = BlanksGroup.create(correct_word)

        blanks_group = blanks_group.reveal_letter("p")

        assert blanks_group.value == ["p", "_", "_", "_", "_", "_"]

        blanks_group = blanks_group.reveal_letter("y")

        assert blanks_group.value == ["p", "y", "_", "_", "_", "_"]

        blanks_group = blanks_group.reveal_letter("t")

        assert blanks_group.value == ["p", "y", "t", "_", "_", "_"]

        blanks_group = blanks_group.reveal_letter("h")

        assert blanks_group.value == ["p", "y", "t", "h", "_", "_"]

        blanks_group = blanks_group.reveal_letter("n")

        assert blanks_group.value == ["p", "y", "t", "h", "_", "n"]

        blanks_group = blanks_group.reveal_letter("o")

        assert blanks_group.value == ["p", "y", "t", "h", "o", "n"]
