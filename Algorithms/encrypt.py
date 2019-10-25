from Algorithms import formatters
from Algorithms import caesar_cypher


def encrypt(plain_text, alphabet, key, respace_block_length):
    cleaned_text = formatters.remove_punctuation(plain_text).upper()
    cypher_text = caesar_cypher.encode(cleaned_text, key, alphabet)
    return formatters.respace_text(cypher_text, respace_block_length)

