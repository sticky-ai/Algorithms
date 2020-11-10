from datetime import datetime, timedelta

def nextSecond(currentTime):
    h, m, s = currentTime
    op = datetime(1, 1, 1, hour=h, minute=m, second=s) + timedelta(seconds=1)
    return [op.hour, op.minute, op.second]

# Hard Coding Version
def nextSecond(currentTime):

    if currentTime[2] == 59:
        currentTime[2] = 0
        if currentTime[1] == 59:
            currentTime[1] = 0
            if currentTime[0] == 23:
                currentTime[0] = 0
            else:
                currentTime[0] += 1
        else:
            currentTime[1] += 1
    else:
        currentTime[2] += 1

    return currentTime

