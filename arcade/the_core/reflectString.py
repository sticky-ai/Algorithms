from string import ascii_lowercase

def reflectString(inputString):
    alpha = ascii_lowercase
    key = {k : v for k, v in enumerate(alpha[::-1])}
    hs = [alpha.index(i) for i in inputString]
    return ''.join([key[i] for i in hs])

    """Using string.makestrans library
    trans = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[::-1])
    return inputString.translate(trans)
    """
