def regexMatching(pattern, test):
    return any(re.findall(pattern, test))
