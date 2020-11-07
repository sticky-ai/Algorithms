def oddNumbersBeforeZero(sequence):
    return len([s for s in sequence[:sequence.index(0)] if s % 2 != 0])
