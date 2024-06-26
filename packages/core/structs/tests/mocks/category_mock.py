from core.structs import Word


class CategoryMock:
    def __init__(self, fake_random_word: Word):
        self.fake_random_word = fake_random_word

    @property
    def random_word(self):
        return self.fake_random_word
