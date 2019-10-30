import unittest
import Algorithms


class RailFenceCipherTests(unittest.TestCase):
    def test_01(self):
        plain_text = '123456789'
        key = 1
        cipher = Algorithms.RailFenceCipher().encrypt(plain_text, key)
        self.assertEqual('123456789', cipher)

    def test_02(self):
        plain_text = '123456789'
        key = 2
        cipher = Algorithms.RailFenceCipher().encrypt(plain_text, key)
        self.assertEqual('123456789', cipher)

    def test_03(self):
        plain_text = '123456789'
        key = 3
        cipher = Algorithms.RailFenceCipher().encrypt(plain_text, key)
        self.assertEqual('123456789', cipher)
