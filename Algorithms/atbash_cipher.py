class AtbashCipher:
    def encrypt(self, plain_text, alphabet):
        key = self.create_key(alphabet)
        return str.translate(plain_text, str.maketrans(alphabet, key))

    def decrypt(self, cipher_text, alphabet):
        return self.encrypt(cipher_text, alphabet)

    @staticmethod
    def create_key(alphabet):
        return alphabet[::-1]
