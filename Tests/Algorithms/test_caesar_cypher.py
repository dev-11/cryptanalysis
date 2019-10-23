import unittest
import Algorithms


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
