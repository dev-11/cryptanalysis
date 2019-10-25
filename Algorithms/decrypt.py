from Algorithms import caesar_cypher
from Formatters import formatters


def exhaust(cipher, alphabet):
    merged_cipher = formatters.merge_cipher_blocks(cipher)
    for shift in range(len(alphabet)):
        yield caesar_cypher.decode(merged_cipher, shift, alphabet)
