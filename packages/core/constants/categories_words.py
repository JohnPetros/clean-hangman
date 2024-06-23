from collections import namedtuple

categories_tuple = namedtuple("CATEGORIES_WORDS", ["programming", "animals"])

CATEGORIES_WORDS = categories_tuple(["python", "javascript"], ["dog", "cat"])
