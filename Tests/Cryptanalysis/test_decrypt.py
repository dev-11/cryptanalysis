import Cryptanalysis
import unittest
import string


class EncryptTests(unittest.TestCase):
    def test_exhaust_finds_encoded_text(self):
        plain_text = 'BTEGRXFS'
        alphabet = string.ascii_uppercase
        candidates = list(Cryptanalysis.exhaust(plain_text, alphabet))
        self.assertEqual(len(alphabet), len(candidates))
        self.assertIn('ASDFQWER', candidates)
        self.assertEqual('ASDFQWER', candidates[25])
