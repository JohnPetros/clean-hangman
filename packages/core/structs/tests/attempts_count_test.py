from pytest import raises

from ..attempts_count import AtemptsCount


def describe_attempts_count():

    def should_throw_error_if_value_is_not_integer():
        with raises(ValueError) as error:
            AtemptsCount("invalid integer")

        assert str(error.value) == "Attempts count value should be a integer"

    def should_throw_error_if_value_is_negative():
        with raises(ValueError) as error:
            AtemptsCount(-1)

        assert str(error.value) == "Attempts count value should be greater than zero"

    def should_decrement_value():
        attempts_count = AtemptsCount(5)

        assert attempts_count.decrement().value == 4
