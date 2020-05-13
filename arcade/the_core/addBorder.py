def addBorder(picture):
    max_len = len(max(picture, key=len)) + 2
    pre, post = ['*' * max_len], ['*' * max_len]
    c = [i.center(max_len, '*') for i in picture]
    return pre + c + post

