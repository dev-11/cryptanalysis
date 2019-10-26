from Algorithms.caesar_cipher import CaesarCipher


class Rot13Cipher:
    def __init__(self):
        self._cipher = CaesarCipher()

    def encrypt(self, plain_text, alphabet):
        return self._cipher.encrypt(plain_text, alphabet, 13)

    def decrypt(self, cipher_text, alphabet):
        return self._cipher.decrypt(cipher_text, alphabet, 13)
