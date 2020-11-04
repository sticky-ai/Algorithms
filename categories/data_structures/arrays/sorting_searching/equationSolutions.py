def equationSolutions(l, r):
    return len([i for i in range(l, r+1) if i ** 3 in range(l, r+1)])
