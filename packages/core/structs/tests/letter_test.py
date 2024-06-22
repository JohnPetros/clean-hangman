from pytest import raises

from ..letter import Letter


def describe_letter():

    def should_throw_error_if_value_is_not_valid():
        with raises(ValueError) as error:
            Letter(9999)

        assert str(error.value) == "Letter error should be a string"

    def should_have_value():
        value = "j"
        letter = Letter(value)

        assert letter.value == value
