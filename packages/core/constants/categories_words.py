from collections import namedtuple

categories_tuple = namedtuple("Tuple", ["programming", "animals"])

CATEGORIES_WORDS = categories_tuple(["python", "javascript"], ["dog", "cat"])
