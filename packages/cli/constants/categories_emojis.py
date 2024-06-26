from collections import namedtuple

categories_tuple = namedtuple(
    "CATEGORIES_EMOJIS",
    ["programming", "animals", "countries", "fruits", "sports", "objects"],
)

CATEGORIES_EMOJIS = categories_tuple("🖥️", "🐶", "🌏", "🍎", "⚽", "🪑")
