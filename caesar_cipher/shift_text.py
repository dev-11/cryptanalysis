import string

cipher_text = input()

def shift_text(text, shift):
    shift %= 26
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    return string.translate(text, string.maketrans(alphabet, shifted_alphabet), string.whitespace)

for shift in range(26):
    print(str(shift).zfill(2) + ': ' + shift_text(cipher_text, shift))
