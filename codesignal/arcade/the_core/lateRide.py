def lateRide(n):
    return sum([int(i) for i in str(n//60) + str(n%60)])
