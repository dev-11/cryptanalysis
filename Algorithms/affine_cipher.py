class AffineCipher:
    def encrypt(self, plain_text, alphabet, a, b):
        self.validate_a(a, alphabet)
        key = self.create_key(alphabet, a, b)
        return plain_text.translate(str.maketrans(alphabet, key))

    def decrypt(self, cipher_text, alphabet, a, b):
        key = self.create_key(alphabet, a, b)
        return cipher_text.translate(str.maketrans(key, alphabet))

    @staticmethod
    def validate_a(a, alphabet):
        if (a % 2 == 0 and (a > 1 or a < len(alphabet))) or a < 1 or a > len(alphabet):
            raise ValueError(f'the value of "a" must be an odd number between 1 and {len(alphabet)}')

    @staticmethod
    def create_key(alphabet, a, b):
        return ''.join([chr(((a * (ord(t) - ord(alphabet[0])) + b) % 26) + ord(alphabet[0])) for t in alphabet])
