from math import ceil, floor
s, e = eval(dir()[0])
a, c, f = abs, ceil, floor
r = 0
for x, y in zip(s, e):
    if c(x) == c(y):
        r += min(
            a(c(x) - x) + a(c(y) - y), 
            a(f(x) - x) + a(f(y) - y))
    else:
        r += a(x - y)

return r

# from math import ceil, floor
# def perfectCity(departure, destination):
#     s = 0
#     c, f = ceil, floor
#     for x, y in zip(departure, destination):
        
#         if c(x) == c(y):
#             s += min(
#                 abs(c(x) - x) + abs(c(y) - y),
#                 abs(f(x) - x) + abs(f(y) - y))
            
#         else:
#             s += abs(x - y)
    
#     return s
            
            
