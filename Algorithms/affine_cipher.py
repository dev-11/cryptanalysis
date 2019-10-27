class AffineCipher:
    def encrypt(self, plain_text, alphabet, a, b):
        key = self.create_key(alphabet, a, b)
        print(key)
        return plain_text.translate(str.maketrans(alphabet, key))

    def decrypt(self, cipher_text, alphabet, a, b):
        key = self.create_key(alphabet, a, b)
        print(key)
        return cipher_text.translate(str.maketrans(key, alphabet))

    @staticmethod
    def create_key(alphabet, a, b):
        return ''.join([chr(((a * (ord(t) - ord(alphabet[0])) + b) % 26) + ord(alphabet[0])) for t in alphabet])
