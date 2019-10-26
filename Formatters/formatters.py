def respace_text(text, block_length):
    return text if block_length == 0 else [text[i:i+block_length] for i in range(0, len(text), block_length)]
