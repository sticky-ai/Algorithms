from calendar import weekday
def dayOfWeek(birthdayDate):
    m, d, y = map(int, birthdayDate.split("-"))
    w = weekday(y, m, d)
    i = 1
    while True:
        try:
            if weekday(y + i, m, d) == w:
                break
            else:
                i += 1
        except:
            i += 1
    return i
    

