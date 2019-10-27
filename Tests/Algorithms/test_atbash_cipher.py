import unittest
import string
from Algorithms import AtbashCipher


class AtbashCipherTests(unittest.TestCase):
    def test_01(self):
        plain_text = 'abc'
        alphabet = string.ascii_lowercase
        cipher = AtbashCipher().encrypt(plain_text, alphabet)
        self.assertEqual('zyx', cipher)

    def test_02(self):
        plain_text = 'zyx'
        alphabet = string.ascii_lowercase
        cipher = AtbashCipher().decrypt(plain_text, alphabet)
        self.assertEqual('abc', cipher)

    def test_create_key_creates_key_from_alphabet(self):
        alphabet = string.ascii_lowercase
        key = AtbashCipher().create_key(alphabet)
        self.assertEqual(alphabet[::-1], key)

