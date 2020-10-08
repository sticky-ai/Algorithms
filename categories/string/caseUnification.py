def caseUnification(s):
    return s.upper() if sum(1 for i in s if i.isupper()) > (len(s) / 2) else s.lower()
