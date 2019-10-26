from Algorithms.caesar_cipher import CaesarCipher
from Formatters import formatters


def exhaust(cipher, alphabet):
    merged_cipher = formatters.merge_cipher_blocks(cipher)
    caesar_cipher = CaesarCipher()
    for shift in range(len(alphabet)):
        yield caesar_cipher.decrypt(merged_cipher, shift, alphabet)
