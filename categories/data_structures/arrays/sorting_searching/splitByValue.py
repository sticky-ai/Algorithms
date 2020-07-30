def splitByValue(k, elements):
    lt = [elements[i] for i in range(len(elements)) if elements[i] < k]
    gt = [elements[i] for i in range(len(elements)) if elements[i] > k]
    return lt + [k] + gt if lt != elements and gt != elements else elements
