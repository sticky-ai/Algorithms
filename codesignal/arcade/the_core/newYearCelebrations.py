def newYearCelebrations(takeOffTime, minutes):
    midnight = 24*60
    takeoff_mins = 60*int(takeOffTime[:2]) + int(takeOffTime[-2:])
    if takeoff_mins == 0:
        takeoff_mins = midnight
    return sum(midnight <= takeoff_mins + x - 60*i <= midnight + 60 for i, x in enumerate(minutes)) + 1
