def fixedPointsPermutation(permutation):
    return len([1 for o, n in zip(permutation, range(1, max(permutation) + 1)) if o == n])
