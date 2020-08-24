from datetime import datetime, timedelta

def nextSecond(currentTime):
    h, m, s = currentTime
    op = datetime(1, 1, 1, hour=h, minute=m, second=s) + timedelta(seconds=1)
    return [op.hour, op.minute, op.second]
