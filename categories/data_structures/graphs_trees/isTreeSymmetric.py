def isTreeSymmetric(t):
    return f(t.left, t.right) if t else True

def f(i, j):
    if i and j:
        return i.value == j.value and f(i.left, j.right) and f(i.right, j.left)
    return not i and not j
