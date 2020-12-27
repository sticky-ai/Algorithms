import numpy as np

def priceSuggestion(contractData):
    c = sorted(contractData)
    l = len(c) // 2
    return c and [np.median(c[:l]) // 1, -(-np.median(c[l:]) // 1)]
