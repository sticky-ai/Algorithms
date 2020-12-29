from functools import reduce

P, B = eval(dir()[0])
f = lambda x, y: x * y
R = [b for b in B if all([f <= s for f, s in zip(sorted(P), sorted(b))])]
m = [reduce(f, r) for r in R]
z = [reduce(f, b) for b in B]
return -1 if not R else z.index(min(m))
