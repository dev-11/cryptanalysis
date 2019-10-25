import Algorithms
import unittest
import string


class EncryptTests(unittest.TestCase):
    def test_encrypt_creates_respaced_cipher_from_plain_text(self):
        plain_text = 'asdfqwer'
        key = 1
        alphabet = string.ascii_uppercase
        block_length = 5
        cipher = Algorithms.encrypt(plain_text, alphabet, key, block_length)
        self.assertEqual(2, len(cipher))
        self.assertEqual(5, len(cipher[0]))
        self.assertEqual(3, len(cipher[1]))
        self.assertEqual(['BTEGR', 'XFS'], cipher)
