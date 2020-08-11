from collections import Counter

def extraNumber(a, b, c):
    return Counter([a, b, c]).most_common()[-1][0]

