from itertools import combinations

def stringsCrossover(inputArray, result):    
    count = 0
    for comb in combinations(inputArray, 2):
        if all([t in c for c, t in zip(zip(*comb), result)]):
            count += 1
    return count
