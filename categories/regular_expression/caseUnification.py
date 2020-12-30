def caseUnification(inputString):
    return inputString.upper() if len(re.findall('[A-Z]', inputString)) > len(inputString) / 2 else inputString.lower()
