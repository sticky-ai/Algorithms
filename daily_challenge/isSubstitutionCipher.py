# 68 chars
a, b = eval(dir()[0])
l = lambda x:len(set(x))
return l(zip(a, b)) <= l(a) == l(b)

# 75 chars
# a, b = eval(dir()[0])
# l = lambda x:len(set(x))
# return l(a) == l(b) and l(zip(a, b)) <= l(a)

# 82 chars
# a, b = eval(dir()[0])
# c = len(set(a))
# return c == len(set(b)) and len(set(z for z in zip(a, b))) <= c

# 85 chars
# a = eval(dir()[0])
# c = len(set(a[0]))
# return c == len(set(a[1])) and len(set(z for z in zip(*a))) <= c

# 136 chars
# def isSubstitutionCipher(s1, s2):
#     s = set()
#     for z in zip(s1, s2):
#         s.add(z)
#     return len(set(s1)) == len(set(s2)) and len(s) <= max(len(set(s1)), len(set(s2)))
