class KeywordCipher:
    def encrypt(self, plain_text, alphabet, keyword):
        key = self.create_key(alphabet, keyword)
        return plain_text.translate(str.maketrans(alphabet, key))

    def decrypt(self, cipher_text, alphabet, keyword):
        key = self.create_key(alphabet, keyword)
        return cipher_text.translate(str.maketrans(key, alphabet))

    @staticmethod
    def create_key(alphabet, keyword):
        keyword_without_duplicates = ''.join(sorted(set(keyword), key=keyword.index))
        return keyword_without_duplicates + ''.join([x for x in alphabet if x not in keyword_without_duplicates])
