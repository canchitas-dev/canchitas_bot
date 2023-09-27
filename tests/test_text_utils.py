from canchitas_bot.text_utils import is_haiku


class TestTextUtils:

    def setup_method(self):
        self.valid_haiku = """adios chamaco\nbuenos dias muchacho\nhastsa la vista"""

        self.not_valid_len = self.valid_haiku + "\nhasta luego"
        self.not_haiku_sillables = """dios gringo\nbuenos dias muchacho\nbye"""

        self.valid_haiku_broken_y = """Son mariposas\ny flores en el jardin.\nUn benedición."""

    def test_valid_haiku(self):
        """
        Ensure haiku detection is working for valid input
        """
        assert is_haiku(self.valid_haiku)

    def test_invalid_len_haiku(self):
        """
        Ensure haikus of invalid len are evaluated correctly
        """
        assert not is_haiku(self.not_valid_len)

    def test_invalid_sylable_count_haiku(self):
        """
        Ensure haikus of right len but wrong syllable count are evaluated correctly
        """
        assert not is_haiku(self.not_haiku_sillables)

    def test_broken_line_starts_with_y(self):
        """
        Ensure lines starting with single y are parsed correctly.
        """
        assert is_haiku(self.valid_haiku_broken_y)
