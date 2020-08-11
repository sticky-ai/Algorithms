def groupDating(male, female):
    return list(zip(*[x for x in list(zip(male,female)) if x[0]!=x[1]]))

