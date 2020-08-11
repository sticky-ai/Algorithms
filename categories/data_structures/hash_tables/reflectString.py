def reflectString(inputString):
    s = string.ascii_lowercase
    d = {k:v for k, v in zip(s, s[::-1])}
    return ''.join([d[i] for i in inputString])
