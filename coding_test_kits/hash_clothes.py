from collections import defaultdict
from functools import reduce

def solution(clothes):
    dic = defaultdict(list)
    for k, v in clothes:
        dic[v].append(k)
    
    return reduce(lambda x, y: x*(y+1), map(len, dic.values()), 1) - 1
