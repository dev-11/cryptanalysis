import unittest
import string
from Algorithms import KeywordCipher


class KeywordCipherTests(unittest.TestCase):
    def test_keyword_cipher_returns_correct_cipher(self):
        plain_text = 'LANGUAGE IS THE KEY TO THE HEART OF PEOPLE'
        keyword = 'THEGCHQPUZZLEBOOKII'
        cipher = KeywordCipher().encrypt(plain_text, string.ascii_uppercase, keyword)
        self.assertEqual('OTIPRTPC ZM NUC BCX NA NUC UCTJN AQ DCADOC', cipher)

    def test_keyword_cipher_returns_correct_cipher(self):
        plain_text = 'OTIPRTPC ZM NUC BCX NA NUC UCTJN AQ DCADOC'
        keyword = 'THEGCHQPUZZLEBOOKII'
        decrypted_text = KeywordCipher().decrypt(plain_text, string.ascii_uppercase, keyword)
        self.assertEqual('LANGUAGE IS THE KEY TO THE HEART OF PEOPLE', decrypted_text)

    def test_create_key_creates_key_from_alphabet_and_keyword(self):
        keyword = 'THEGCHQPUZZLEBOOKII'
        alphabet = string.ascii_uppercase
        key = KeywordCipher().create_key(alphabet, keyword)
        self.assertEqual('THEGCQPUZLBOKIADFJMNRSVWXY', key)
