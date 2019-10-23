import unittest
import Algorithms.formatters


class FormattersTests(unittest.TestCase):
    def test_respacing_text_to_equal_blocks(self):
        text = "ABCDEFGHIJ"
        block_length = 5
        respaced_text = Algorithms.formatters.respace_text(text, block_length)
        self.assertEqual(['ABCDE', 'FGHIJ'], respaced_text)

    def test_respacing_text_to_uneven_blocks(self):
        text = "ABCDEFGHI"
        block_length = 5
        respaced_text = Algorithms.formatters.respace_text(text, block_length)
        self.assertEqual(['ABCDE', 'FGHI'], respaced_text)
