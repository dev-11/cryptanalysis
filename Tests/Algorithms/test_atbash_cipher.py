import unittest
import string
from Algorithms import AtbashCipher


class AtbashCipherTests(unittest.TestCase):
    def test_encrypt_returns_correct_cipher(self):
        plain_text = 'abc'
        alphabet = string.ascii_lowercase
        cipher = AtbashCipher().encrypt(plain_text, alphabet)
        self.assertEqual('zyx', cipher)

    def test_encrypt_returns_correct_plain_text(self):
        cipher = 'zyx'
        alphabet = string.ascii_lowercase
        plain_text = AtbashCipher().decrypt(cipher, alphabet)
        self.assertEqual('abc', plain_text)

    def test_create_key_creates_key_from_alphabet(self):
        alphabet = string.ascii_lowercase
        key = AtbashCipher().create_key(alphabet)
        self.assertEqual(alphabet[::-1], key)

