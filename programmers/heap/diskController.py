import heapq as h
from collections import deque

def solution(jobs):
    t, st, ft, tt = 0, 0, 0, 0
    disk, priority, waiting = [], [], []
    
    for job in jobs:
        h.heappush(priority, job)
    
    while True:
        for i in range(len(priority)):
            if t >= priority[0][0]:
                waiting.append(h.heappop(priority))

        waiting.sort(key=lambda x: x[-1])

        if not disk:
            if waiting:
                disk = waiting.pop(0)
                st = t
                ft = t + disk[1]

        elif disk:
            if t == ft:
                tt += ft - disk[0]
                disk = []
                continue

        t += 1
        
        if not priority and not disk:
            break

    return int(tt / len(jobs))
