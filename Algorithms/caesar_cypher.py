import string


def decode(text, shift):
    shift %= 26
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    return str.translate(text, str.maketrans(alphabet, shifted_alphabet))


def encode(text, shift):
    return decode(text, shift)
