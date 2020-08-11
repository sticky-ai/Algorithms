import datetime

def maliciousProgram(curDate, changes):
    time = datetime.datetime.strptime(curDate, '%d %b %Y %H:%M:%S')
    d, M, y, h, m, s = changes
    try:
        c_time = time.replace(day = time.day + d,
                              year = time.year + y,
                              month = time.month + M,
                              hour = time.hour + h,
                              minute = time.minute + m,
                              second = time.second + s)
    except ValueError:
        return curDate
    
    return c_time.strftime('%d %b %Y %H:%M:%S')

