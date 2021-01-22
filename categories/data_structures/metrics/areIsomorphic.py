import pandas as pd

def areIsomorphic(array1, array2):
    a1, a2 = map(pd.DataFrame, [array1, array2])
    l1, l2 = [len(x) for x in array1], [len(x) for x in array2]
    return a1.shape == a2.shape and l1 == l2
