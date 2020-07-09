def howManySundays(n, startDay):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    diff = abs(days.index('Sunday') - days.index(startDay))
    return n // 7 + 1 if n % 7 + diff >= 7 else n // 7
