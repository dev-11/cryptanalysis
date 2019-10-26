from Algorithms.cipher import Cipher


class CaesarCipher(Cipher):
    def decrypt(self, cipher_text, alphabet, key):
        key %= len(alphabet)
        shifted_alphabet = alphabet[key:] + alphabet[:key]
        return str.translate(cipher_text, str.maketrans(alphabet, shifted_alphabet))

    def encrypt(self, plain_text, alphabet, key):
        return self.decrypt(plain_text, alphabet, key)
