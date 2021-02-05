#!/bin/python3

import math
import os
import random
import re
import sys

def dfs(graph, x, y, size):
    cnt = 0
    if x < 0 or x >= size[0] or y < 0 or y >= size[1]:
        return cnt
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        cnt += 1
        
        cnt += dfs(graph, x-1, y+1, size)
        cnt += dfs(graph, x+1, y-1, size)
        cnt += dfs(graph, x+1, y+1, size)
        cnt += dfs(graph, x-1, y-1, size)
        cnt += dfs(graph, x-1, y, size)
        cnt += dfs(graph, x+1, y, size)
        cnt += dfs(graph, x, y-1, size)
        cnt += dfs(graph, x, y+1, size)

    return cnt

# Complete the maxRegion function below.
def maxRegion(grid):
    cnt = []
    r, c = len(grid), len(grid[0])
    for i in range(r):
        for j in range(c):
            cnt.append(dfs(grid, i, j, [r, c]))
    return max(cnt)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()

