from Algorithms.vigenere_cipher import VigenereCipher


class AutokeyCipher:
    def __init__(self):
        self._vigenere_cipher = VigenereCipher()

    def encrypt(self, plain_text, alphabet, keyword):
        key = self.generate_key(keyword, plain_text)
        tabula_recta = self.generate_tabula_recta(alphabet)
        cipher = ''

        for index, initial_char in enumerate(key):
            row = list(filter(lambda x: x[0] == initial_char, tabula_recta))[0]
            char_index = alphabet.index(plain_text[index])
            cipher += row[char_index]

        return cipher

    def decrypt(self, cipher_text, alphabet, keyword):
        key = self.generate_key(keyword, cipher_text)
        tabula_recta = self.generate_tabula_recta(alphabet)
        plain_text = ''

        for index, initial_char in enumerate(key):
            row = list(filter(lambda x: x[0] == initial_char, tabula_recta))[0]
            char_index = row.index(cipher_text[index])
            plain_text += alphabet[char_index]

        return plain_text

    @staticmethod
    def generate_key(keyword, text):
        len_text = len(text)
        len_keyword = len(keyword)

        return keyword + text[:len_text - len_keyword]
            if len_keyword < len_text
            else keyword[:len_text]

    def generate_tabula_recta(self, alphabet):
        return self._vigenere_cipher.generate_tabula_recta(alphabet)

