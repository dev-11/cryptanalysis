import unittest
import string
from Algorithms import CaesarCipher


class CaesarCipherTests(unittest.TestCase):
    def test_decrypt_returns_correct_decoded_text_with_shift_13(self):
        encoded_text = 'vslbhnerbagurpragranelgenvyxrrcfbyivatgurpunyyratrf'
        shift = 13
        alphabet = string.ascii_lowercase
        decoded_text = CaesarCipher().decrypt(encoded_text, alphabet, shift)
        self.assertEqual('ifyouareonthecentenarytrailkeepsolvingthechallenges', decoded_text)

    def test_encrypt_returns_correct_encoded_text_with_shift_13(self):
        plain_text = 'ifyouareonthecentenarytrailkeepsolvingthechallenges'
        shift = 13
        alphabet = string.ascii_lowercase
        encoded_text = CaesarCipher().encrypt(plain_text, alphabet, shift)
        self.assertEqual('vslbhnerbagurpragranelgenvyxrrcfbyivatgurpunyyratrf', encoded_text)

    def test_encrypt_works_with_empty_text(self):
        plain_text = ''
        shift = 1
        alphabet = string.ascii_lowercase
        encoded_text = CaesarCipher().encrypt(plain_text, alphabet, shift)
        self.assertEqual('', encoded_text)

    def test_decrypt_works_with_empty_text(self):
        encoded_text = ''
        shift = 1
        alphabet = string.ascii_lowercase
        decoded_text = CaesarCipher().decrypt(encoded_text, alphabet, shift)
        self.assertEqual('', decoded_text)

    def test_decrypt_returns_original_text_on_zero_shift(self):
        encoded_text = string.ascii_lowercase
        shift = 0
        alphabet = string.ascii_lowercase
        decoded_text = CaesarCipher().decrypt(encoded_text, alphabet, shift)
        self.assertEqual(string.ascii_lowercase, decoded_text)

    def test_encrypt_returns_original_text_on_zero_shift(self):
        plain_text = string.ascii_lowercase
        shift = 0
        alphabet = string.ascii_lowercase
        encoded_text = CaesarCipher().encrypt(plain_text, alphabet, shift)
        self.assertEqual(string.ascii_lowercase, encoded_text)
