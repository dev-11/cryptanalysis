import unittest
import string
from Algorithms import VigenereCipher


class VigenereCipherTests(unittest.TestCase):
    def test_generate_key_generates_correct_key_when_keyword_is_shorter_than_plain_text(self):
        plain_text = 'ATTACKATDAWN'
        keyword = 'LEMON'
        key = VigenereCipher().generate_key(keyword, len(plain_text))
        self.assertEqual('LEMONLEMONLE', key)

    def test_generate_key_generates_correct_key_when_keyword_is_longer_than_plain_text(self):
        plain_text = 'ATT'
        keyword = 'LEMON'
        key = VigenereCipher().generate_key(keyword, len(plain_text))
        self.assertEqual('LEM', key)

    def test_generate_key_generates_correct_key_when_keyword_length_is_equal_to_plain_text_length(self):
        plain_text = 'ATTAC'
        keyword = 'LEMON'
        key = VigenereCipher().generate_key(keyword, len(plain_text))
        self.assertEqual('LEMON', key)

    def test_generate_tabula_recta_creates_correct_matrix(self):
        alphabet = string.ascii_lowercase
        tabula_recta = VigenereCipher().generate_tabula_recta(alphabet)
        self.assertEqual(26, len(alphabet))
        for i in range(26):
            self.assertEqual(alphabet[i:] + alphabet[:i], tabula_recta[i])

    def test_encrypt_returns_correct_cipher(self):
        plain_text = 'ATTACKATDAWN'
        alphabet = string.ascii_uppercase
        keyword = 'LEMON'
        cipher = VigenereCipher().encrypt(plain_text, alphabet, keyword)
        self.assertEqual('LXFOPVEFRNHR', cipher)

    def test_decrypt_returns_correct_plain_text(self):
        cipher_text = 'LXFOPVEFRNHR'
        alphabet = string.ascii_uppercase
        keyword = 'LEMON'
        cipher = VigenereCipher().decrypt(cipher_text, alphabet, keyword)
        self.assertEqual('ATTACKATDAWN', cipher)
