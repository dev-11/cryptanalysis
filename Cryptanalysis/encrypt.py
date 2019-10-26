from Formatters import formatters
from Algorithms.caesar_cipher import CaesarCipher


def encrypt(plain_text, alphabet, key, respace_block_length):
    cleaned_text = formatters.remove_punctuation(plain_text).upper()
    cypher_text = CaesarCipher().encrypt(cleaned_text, key, alphabet)
    return formatters.respace_text(cypher_text, respace_block_length)
