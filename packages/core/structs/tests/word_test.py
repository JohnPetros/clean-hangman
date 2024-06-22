from pytest import raises


from ..word import Word
from ..letter import Letter


def describe_word():
    def should_throw_error_if_value_is_not_valid():
        with raises(ValueError) as error:
            Word(["a", "b", "c"])

            assert str(error.value) == "Word letters should be a list of valid letters"

    def should_have_letters():
        word = Word.create("abc")

        assert word.letters == [Letter("a"), Letter("b"), Letter("c")]

    def should_have_length():
        word = Word.create("python")

        assert word.length == 6

    def should_check_if_a_letter_is_included():
        word = Word.create("python")

        assert word.includes_letter(Letter("p"))
        assert not word.includes_letter(Letter("z"))
