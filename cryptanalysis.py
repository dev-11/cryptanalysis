# -*- coding: utf-8 -*-

from Cryptanalysis import encrypt
from Cryptanalysis import decrypt
from Formatters import sanitiser
import string
from termcolor import colored


def main():
    plain_text = '...we shall defend our Island, whatever the cost may be, we shall fight on the beaches, we shall fight on the landing grounds, we shall fight in the fields and in the streets, we shall fight in the hills; we shall never surrender, and even if, which I do not for a moment believe, this Island or a large part of it were subjugated and starving, then our Empire beyond the seas, armed and guarded by the British Fleet, would carry on the struggle, until, in God’s good time, the New World, with all its power and might, steps forth to the rescue and the liberation of the old.'
    alphabet = string.ascii_uppercase
    cipher = encrypt(plain_text=plain_text, alphabet=alphabet, key=13, respace_block_length=5)
    candidates = decrypt.exhaust(cipher, alphabet)

    print("========== PLAIN TEXT ==========")
    print(plain_text)
    print("========== CIPHER ==========")
    print(*cipher)
    print("========== CANDIDATES ==========")
    for idx, c in enumerate(candidates):
        current_color = 'green' if sanitiser.remove_punctuation(plain_text.upper()) == c else 'cyan'
        print(colored(str(idx).zfill(2) + ': ' + c, current_color))
        print()


if __name__ == '__main__':
    main()
