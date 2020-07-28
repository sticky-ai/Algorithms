def isGeometricProgression(sequence):
    diff = [sequence[i+1] / sequence[i] for i in range(len(sequence) - 1)]
    return len(set(diff)) == 1
