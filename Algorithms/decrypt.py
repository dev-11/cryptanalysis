from Algorithms import caesar_cypher
from Algorithms import formatters


def exhaust(cipher, alphabet):
    merged_cipher = formatters.merge_cipher_blocks(cipher)
    candidates = []
    for shift in range(len(alphabet)):
        candidates.append(caesar_cypher.decode(merged_cipher, shift, alphabet))
    return candidates
