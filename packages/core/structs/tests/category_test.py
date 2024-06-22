from pytest import raises

from ..category import Category
from ...constants import CATEGORIES_WORDS


def describe_category():
    def should_raise_value_error_if_category_does_not_exist():
        with raises(ValueError) as error:
            Category("non exist category")

        assert str(error.value) == "Category does not exist"

    def should_get_random_word():
        category = Category("programming")

        assert category.random_word.value in CATEGORIES_WORDS.programming
