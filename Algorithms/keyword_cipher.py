class KeywordCipher:
    def encrypt(self, plain_text, alphabet, keyword):
        key = self.create_key(alphabet, keyword)
        return str.translate(plain_text, str.maketrans(alphabet, key))

    def create_key(self, alphabet, keyword):
        keyword_without_duplicates = ''.join(sorted(set(keyword), key=keyword.index))
        return keyword_without_duplicates + ''.join([x for x in alphabet if x not in keyword_without_duplicates])
