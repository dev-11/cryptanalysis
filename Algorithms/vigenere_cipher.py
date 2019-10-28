class VigenereCipher:
    def encrypt(self, plain_text, alphabet, keyword):
        key = self.generate_key(keyword, len(plain_text))
        tabula_recta = self.generate_tabula_recta(alphabet)
        cipher = ''

        for index, initial_char in enumerate(key):
            row = list(filter(lambda x: x[0] == initial_char, tabula_recta))[0]
            char_index = alphabet.index(plain_text[index])
            cipher += row[char_index]

        return cipher

    def decrypt(self, cipher_text, alphabet, keyword):
        key = self.generate_key(keyword, len(cipher_text))
        tabula_recta = self.generate_tabula_recta(alphabet)
        plain_text = ''

        for index, initial_char in enumerate(key):
            row = list(filter(lambda x: x[0] == initial_char, tabula_recta))[0]
            char_index = row.index(cipher_text[index])
            plain_text += alphabet[char_index]

        return plain_text

    @staticmethod
    def generate_key(keyword, key_length):
        len_keyword = len(keyword)
        return ''.join([keyword[index % len_keyword] for index in range(key_length)])

    @staticmethod
    def generate_tabula_recta(alphabet):
        return [alphabet[i:] + alphabet[:i] for i in range(len(alphabet))]
