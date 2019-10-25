def respace_text(text, block_length):
    return [text[i:i+block_length] for i in range(0, len(text), block_length)]


def remove_punctuation(text):
    return ''.join([i for i in text if i.isalnum()])


merge_cipher_blocks = remove_punctuation
