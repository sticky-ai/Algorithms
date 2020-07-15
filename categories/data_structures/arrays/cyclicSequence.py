def cyclicSequence(sequence):
    minIdx = sequence.index(min(sequence))
    arr = sequence[minIdx:] + sequence[:minIdx]
    return arr == sorted(sequence) if len(set(sequence)) == len(sequence) else False
