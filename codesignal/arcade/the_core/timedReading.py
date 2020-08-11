import re

def timedReading(maxLength, text):
    p = re.compile('\w+')
    return len([i for i in p.findall(text) if len(i) <= maxLength])
