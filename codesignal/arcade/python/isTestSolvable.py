def isTestSolvable(ids, k):
    digitSum = lambda q: sum([int(i) for i in str(q)])

    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)
    return sm % k == 0

