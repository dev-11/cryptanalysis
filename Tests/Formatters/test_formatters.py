import unittest
from Formatters import formatters, sanitiser


class FormattersTests(unittest.TestCase):
    def test_respacing_text_to_equal_blocks(self):
        text = 'ABCDEFGHIJ'
        block_length = 5
        respaced_text = formatters.respace_text(text, block_length)
        self.assertEqual(['ABCDE', 'FGHIJ'], respaced_text)

    def test_respacing_text_to_uneven_blocks(self):
        text = 'ABCDEFGHI'
        block_length = 5
        respaced_text = formatters.respace_text(text, block_length)
        self.assertEqual(['ABCDE', 'FGHI'], respaced_text)

    def test_respacing_empty_text_to_empty_blocks(self):
        text = ''
        block_length = 5
        respaced_text = formatters.respace_text(text, block_length)
        self.assertEqual([], respaced_text)

    def test_respace_text_returns_single_block_for_zero_block_length(self):
        text = ' asdf\ta s d f\t'
        block_length = 0
        self.assertEqual(text, formatters.respace_text(text, block_length))

    def test_remove_punctuation_removes_non_alnum_chars(self):
        plain_text = 'as-df,qw\'er'
        clean_text = sanitiser.remove_punctuation(plain_text)
        self.assertEqual('asdfqwer', clean_text)

    def test_remove_punctuation_removes_space_chars(self):
        plain_text = ' as    d f '
        clean_text = sanitiser.remove_punctuation(plain_text)
        self.assertEqual('asdf', clean_text)

    def test_remove_punctuation_returns_empty_string_for_empty_string(self):
        plain_text = ''
        clean_text = sanitiser.remove_punctuation(plain_text)
        self.assertEqual('', clean_text)
