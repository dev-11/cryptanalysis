from Algorithms.caesar_cipher import CaesarCipher
from Formatters import sanitiser


def exhaust(cipher, alphabet):
    merged_cipher = sanitiser.merge_cipher_blocks(cipher)
    caesar_cipher = CaesarCipher()
    for shift in range(len(alphabet)):
        yield caesar_cipher.decrypt(merged_cipher, alphabet, shift)
