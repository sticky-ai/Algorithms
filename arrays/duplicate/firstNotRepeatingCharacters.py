from collections import Counter

def firstNotRepeatingCharacter(s):
    res = [k for k, v in Counter(s).most_common() if v == 1]
    if len(res) == 0:
        return '_'
    else:
        return res[0]
