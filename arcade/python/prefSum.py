def prefSum(a):
    # return [sum(a[:i+1]) for i in range(len(a))] #Raise Time Execution Error
    return itertools.accumulate(a)  

