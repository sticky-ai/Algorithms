def areSimilar(a, b):
    if sorted(a) == sorted(b) and sum([i != j for i, j in zip(a, b)]) <= 2:
        return True
    else:
        return False

