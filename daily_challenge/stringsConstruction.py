a, b = eval(dir()[0])
return min(b.count(c) // a.count(c) for c in set(a))

