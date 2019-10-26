from Algorithms.cipher import Cipher


class CaesarCipher(Cipher):
    def decrypt(self, cipher_text, alphabet, key):
        shifted_alphabet = self.create_shifted_alphabet(alphabet, key)
        return str.translate(cipher_text, str.maketrans(alphabet, shifted_alphabet))

    def encrypt(self, plain_text, alphabet, key):
        return self.decrypt(plain_text, alphabet, key)

    @staticmethod
    def create_shifted_alphabet(alphabet, key):
        key %= len(alphabet)
        return alphabet[key:] + alphabet[:key]
