from collections import deque

def solution(priorities, location):
    cnt = 0
    queue = deque([(v, i) for i, v in enumerate(priorities)])
    while queue:
        cur = queue.popleft()
        if queue and max(queue)[0] > cur[0]:
            queue.append(cur)
        else:
            cnt += 1
            if cur[1] == location:
                return cnt
