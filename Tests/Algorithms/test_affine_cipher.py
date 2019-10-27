import unittest
import string
from Algorithms import AffineCipher


class AffineCipherTests(unittest.TestCase):
    def test_encrypt_returns_correct_cipher(self):
        plain_text = 'abcd'
        alphabet = string.ascii_lowercase
        a, b = 1, 1
        cipher = AffineCipher().encrypt(plain_text, alphabet, a, b)
        self.assertEqual('bcde', cipher)

    def test_encrypt_returns_correct_plain_text(self):
        cipher = 'bcde'
        alphabet = string.ascii_lowercase
        a, b = 1, 1
        plain_text = AffineCipher().decrypt(cipher, alphabet, a, b)
        self.assertEqual('abcd', plain_text)

    def test_encrypt_returns_correct_cipher_for_not_equal_a_b(self):
        plain_text = 'AFFINECIPHER'
        alphabet = string.ascii_uppercase
        print(alphabet)
        a, b = 5, 8
        cipher = AffineCipher().encrypt(plain_text, alphabet, a, b)
        self.assertEqual('IHHWVCSWFRCP', cipher)

    def test_encrypt_returns_correct_plain_text_for_not_equal_a_b(self):
        plain_text = 'IHHWVCSWFRCP'
        alphabet = string.ascii_uppercase
        print(alphabet)
        a, b = 5, 8
        cipher = AffineCipher().decrypt(plain_text, alphabet, a, b)
        self.assertEqual('AFFINECIPHER', cipher)

    def test_validate_a_throws_exception_on_invalid_value(self):
        invalid_a = 2
        alphabet = string.ascii_lowercase
        self.assertRaises(ValueError, AffineCipher().validate_a, invalid_a, alphabet)

    def test_validate_a_does_not_throw_exception_on_valid_value(self):
        valid_a = 3
        alphabet = string.ascii_lowercase
        try:
            AffineCipher().validate_a(valid_a, alphabet)
        except ValueError:
            self.assertTrue(False)
