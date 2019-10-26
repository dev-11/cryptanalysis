from abc import ABC


class Cipher(ABC):

    @classmethod
    def decrypt(cls, cipher_text, alphabet, key):
        pass

    @classmethod
    def encrypt(cls, plain_text, alphabet, key):
        pass
