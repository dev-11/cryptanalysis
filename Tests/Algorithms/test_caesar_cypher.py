import unittest
import Algorithms
import string


class CaesarCypherTests(unittest.TestCase):
    def test_decode_returns_correct_decoded_text_with_shift_13(self):
        encoded_text = 'vslbhnerbagurpragranelgenvyxrrcfbyivatgurpunyyratrf'
        shift = 13
        decoded_text = Algorithms.caesar_cypher.decode(encoded_text, shift)
        self.assertEqual('ifyouareonthecentenarytrailkeepsolvingthechallenges', decoded_text)

    def test_encode_returns_correct_encoded_text_with_shift_13(self):
        plain_text = 'ifyouareonthecentenarytrailkeepsolvingthechallenges'
        shift = 13
        encoded_text = Algorithms.caesar_cypher.encode(plain_text, shift)
        self.assertEqual('vslbhnerbagurpragranelgenvyxrrcfbyivatgurpunyyratrf', encoded_text)

    def test_encode_works_with_empty_text(self):
        plain_text = ''
        shift = 1
        encoded_text = Algorithms.caesar_cypher.encode(plain_text, shift)
        self.assertEqual('', encoded_text)

    def test_decode_works_with_empty_text(self):
        encoded_text = ''
        shift = 1
        decoded_text = Algorithms.caesar_cypher.decode(encoded_text, shift)
        self.assertEqual('', decoded_text)

    def test_decode_returns_original_text_on_zero_shift(self):
        encoded_text = string.ascii_lowercase
        shift = 0
        decoded_text = Algorithms.caesar_cypher.decode(encoded_text, shift)
        self.assertEqual(string.ascii_lowercase, decoded_text)

    def test_encode_returns_original_text_on_zero_shift(self):
        plain_text = string.ascii_lowercase
        shift = 0
        encoded_text = Algorithms.caesar_cypher.encode(plain_text, shift)
        self.assertEqual(string.ascii_lowercase, encoded_text)
