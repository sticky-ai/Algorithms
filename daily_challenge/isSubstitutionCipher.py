a, b = eval(dir()[0])
c = len(set(a))
return c == len(set(b)) and len(set(z for z in zip(a, b))) <= c

# def isSubstitutionCipher(s1, s2):
#     s = set()
#     for z in zip(s1, s2):
#         s.add(z)
    
#     return len(set(s1)) == len(set(s2)) and len(s) <= max(len(set(s1)), len(set(s2)))
