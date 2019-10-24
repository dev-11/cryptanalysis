def decode(text, shift, alphabet):
    shift %= len(alphabet)
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    return str.translate(text, str.maketrans(alphabet, shifted_alphabet))


def encode(text, shift, alphabet):
    return decode(text, shift, alphabet)
