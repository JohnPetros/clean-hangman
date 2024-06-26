from pytest import raises

from ..letter import Letter


def describe_letter():
    def should_throw_error_if_value_is_not_text():
        with raises(ValueError) as error:
            Letter(9)

        assert str(error.value) == "Letter value should be a text"

    def should_throw_error_if_value_is_not_a_valid_letter():
        value = "ç"

        with raises(ValueError) as error:
            Letter(value)

        assert str(error.value) == f"{value} value should be a valid letter"

    def should_throw_error_if_value_is_not_equal_to_one():
        with raises(ValueError) as error:
            Letter("bbb")

        assert str(error.value) == "Letter value's length should equal to one"

    def should_have_value():
        value = "j"
        letter = Letter(value)

        assert letter.value == value
