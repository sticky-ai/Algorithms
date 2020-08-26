def visiblePoints(points):
    cnt = 0
    minTheta = int(math.degrees(math.atan2(1, 5)))
    maxTheta = int(math.degrees(math.atan2(3, 2)))
    
    for x, y in points:
        theta = abs(int(math.degrees(math.atan2(x, y))))
        if minTheta <= theta <= maxTheta:
            cnt += 1
    return cnt
