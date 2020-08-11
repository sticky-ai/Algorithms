import re

def longestWord(text):
    r = re.split('[^a-zA-Z]', text)
    return max(r, key=len)
