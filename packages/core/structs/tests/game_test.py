from pytest import fixture, raises

from ..game import Game
from ..category import Category
from ..word import Word
from .mocks import CategoryMock

from ...constants import INITIAL_ATTEMPTS_COUNT, CATEGORIES_WORDS


def describe_game():

    @fixture
    def category_mock():
        fake_word = Word.create("fake")
        return CategoryMock(fake_random_word=fake_word)

    def should_create_with_initial_attempts_count():
        game = Game.create(Category("programming"))

        assert game.attempts_count.value == INITIAL_ATTEMPTS_COUNT

    def should_create_with_correct_word():
        game = Game.create(Category("programming"))

        assert game.correct_word.value in CATEGORIES_WORDS.programming

    def should_create_with_blanks_group():
        game = Game.create(Category("programming"))

        assert game.blanks_group.value == ["_" for _ in range(game.correct_word.length)]

    def should_throw_error_on_input_already_used_letter(category_mock):
        game = Game.create(category_mock)

        game = game.input_letter("f")

        with raises(ValueError) as error:
            game.input_letter("f")

            assert str(error) == "Letter F has already been used"

    def should_store_used_letter_on_input_letter(category_mock):
        game = Game.create(category_mock)

        game = game.input_letter("f")
        game = game.input_letter("a")
        game = game.input_letter("k")
        game = game.input_letter("e")

        assert game.used_letters == ["f", "a", "k", "e"]

    def should_decrement_attempts_count_letter_on_incorrect_guess(category_mock):
        game = Game.create(category_mock)

        original_attempts_count = game.attempts_count

        game = game.input_letter("z")

        assert game.attempts_count.value == original_attempts_count.value - 1

    def should_reveal_letter_on_correct_guess(category_mock):
        game = Game.create(category_mock)

        game = game.input_letter("f")

        assert game.blanks_group.value == ["f", "_", "_", "_"]

    def should_return_false_if_attempts_count_is_not_equal_to_zero_on_check_lose(
        category_mock,
    ):
        game = Game.create(category_mock)

        assert not game.check_lose()

    def should_return_true_if_attempts_count_is_equal_to_zero_on_check_lose(
        category_mock,
    ):
        game = Game.create(category_mock)

        game = game.input_letter("z")
        game = game.input_letter("x")
        game = game.input_letter("y")
        game = game.input_letter("w")
        game = game.input_letter("u")

        assert game.check_lose()

    def should_return_true_if_formed_word_is_equal_to_correct_word_on_check_win(
        category_mock,
    ):
        game = Game.create(category_mock)

        game = game.input_letter("f")
        game = game.input_letter("a")
        game = game.input_letter("k")
        game = game.input_letter("e")

        assert game.check_win()
