import Algorithms
import unittest
import string


class EncryptTests(unittest.TestCase):
    def test_encrypt(self):
        plain_text = 'BTEGRXFS'
        alphabet = string.ascii_uppercase
        candidates = Algorithms.exhaust(plain_text, alphabet)
        self.assertEqual(len(alphabet), len(candidates))
        self.assertIn('ASDFQWER', candidates)
        self.assertEqual('ASDFQWER', candidates[25])
