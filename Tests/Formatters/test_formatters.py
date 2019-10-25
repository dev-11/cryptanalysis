import unittest
import Formatters.formatters


class FormattersTests(unittest.TestCase):
    def test_respacing_text_to_equal_blocks(self):
        text = 'ABCDEFGHIJ'
        block_length = 5
        respaced_text = Formatters.formatters.respace_text(text, block_length)
        self.assertEqual(['ABCDE', 'FGHIJ'], respaced_text)

    def test_respacing_text_to_uneven_blocks(self):
        text = 'ABCDEFGHI'
        block_length = 5
        respaced_text = Formatters.formatters.respace_text(text, block_length)
        self.assertEqual(['ABCDE', 'FGHI'], respaced_text)

    def test_respacing_empty_text_to_empty_blocks(self):
        text = ''
        block_length = 5
        respaced_text = Formatters.formatters.respace_text(text, block_length)
        self.assertEqual([], respaced_text)

    def test_respace_text_throws_ValueError_on_zero_block_length(self):
        text = ''
        block_length = 0
        self.assertRaises(ValueError, Formatters.formatters.respace_text, text, block_length)

    def test_remove_punctuation_removes_non_alnum_chars(self):
        plain_text = 'as-df,qw\'er'
        clean_text = Formatters.formatters.remove_punctuation(plain_text)
        self.assertEqual('asdfqwer', clean_text)

    def test_remove_punctuation_removes_space_chars(self):
        plain_text = ' as    d f '
        clean_text = Formatters.formatters.remove_punctuation(plain_text)
        self.assertEqual('asdf', clean_text)

    def test_remove_punctuation_returns_empty_string_for_empty_string(self):
        plain_text = ''
        clean_text = Formatters.formatters.remove_punctuation(plain_text)
        self.assertEqual('', clean_text)
