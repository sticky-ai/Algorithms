def variableName(name):
    return len(re.findall('^[0-9]|\W+', name)) == 0
