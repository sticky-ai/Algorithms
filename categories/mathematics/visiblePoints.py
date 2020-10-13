from math import atan2, pi

def visiblePoints(points):
    
    maxView = 0
    field_width = 2 * pi * (45.0001 / 360)

    angles = [atan2(y, x) % (2 * pi) for x, y in points]
    angles.sort()

    for x in angles:
        if x < field_width:
            angles.append(x + (2 * pi))
        else:
            break
    
    for i, start_angle in enumerate(angles):
        for j in range(i, len(angles)):
            if angles[j] - angles[i] >= field_width:
                break
                
        temp = range(i, j)
        if len(temp) > maxView:
            maxView = len(temp)

    return maxView
