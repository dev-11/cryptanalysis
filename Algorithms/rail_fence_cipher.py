class RailFenceCipher:
    def encrypt(self, plain_text, key):
        return ''.join(plain_text[index] for index in range(len(plain_text)))

    def decrypt(self, encrypted_text, key):
        return ''.join(encrypted_text[index]
                       for index in range(len(encrypted_text)))

