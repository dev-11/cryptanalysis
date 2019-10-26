from Formatters import formatters, sanitiser
from Algorithms.caesar_cipher import CaesarCipher


def encrypt(plain_text, alphabet, key, respace_block_length):
    cleaned_text = sanitiser.remove_punctuation(plain_text).upper()
    cypher_text = CaesarCipher().encrypt(cleaned_text, alphabet, key)
    return formatters.respace_text(cypher_text, respace_block_length)
