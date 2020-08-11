from itertools import combinations

def stringsCrossover(inputArray, result):
    ans = []
    combs = combinations(inputArray, 2)
    for x, y in combs:
        ans.append(all([c in x[idx] + y[idx] for idx, c in enumerate(result)])) 
    return sum(ans)
        
#     temp = ''
#     combs = list(combinations(inputArray, 2))
#     for c1, c2 in combs:    
#         for idx, (i, j) in enumerate(zip(c1, c2)):
#             if i == result[idx - 1]:
#                 temp += i
#             elif j == result[idx - 1]:
#                 temp += j
#             else:
#                 temp += min(i, j)
#     ans = [temp[i : i + len(result)] for i in range(0, len(temp), len(result))]
#     return ans.count(result)
