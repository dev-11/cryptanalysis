import unittest
import string
from Algorithms import Rot13Cipher


class Rot13CipherTests(unittest.TestCase):
    def test_decrypt_returns_correct_decoded_text_with_shift_13(self):
        encoded_text = 'vslbhnerbagurpragranelgenvyxrrcfbyivatgurpunyyratrf'
        alphabet = string.ascii_lowercase
        decoded_text = Rot13Cipher().decrypt(encoded_text, alphabet)
        self.assertEqual('ifyouareonthecentenarytrailkeepsolvingthechallenges', decoded_text)

    def test_encrypt_returns_correct_encoded_text_with_shift_13(self):
        plain_text = 'ifyouareonthecentenarytrailkeepsolvingthechallenges'
        alphabet = string.ascii_lowercase
        encoded_text = Rot13Cipher().encrypt(plain_text, alphabet)
        self.assertEqual('vslbhnerbagurpragranelgenvyxrrcfbyivatgurpunyyratrf', encoded_text)

    def test_encrypt_works_with_empty_text(self):
        plain_text = ''
        alphabet = string.ascii_lowercase
        encoded_text = Rot13Cipher().encrypt(plain_text, alphabet)
        self.assertEqual('', encoded_text)

    def test_decrypt_works_with_empty_text(self):
        encoded_text = ''
        alphabet = string.ascii_lowercase
        decoded_text = Rot13Cipher().decrypt(encoded_text, alphabet)
        self.assertEqual('', decoded_text)
