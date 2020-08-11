def lineUp(commands):
    status = False
    cnt = 0
    
    for c in commands:
        if c == 'L' or c == 'R':
            status = not status
        if not status:
            cnt += 1
        return cnt
