def remove_punctuation(text):
    return ''.join([i for i in text if i.isalnum()])


merge_cipher_blocks = remove_punctuation
