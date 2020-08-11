def cardinality(start, speed):
    t = []
    for i in range(1, len(start)):
        try:
            if (start[i] - start[0]) / (speed[0] - speed[i]) > 0:
                t.append((start[i] - start[0]) / (speed[0] - speed[i]))
        except:
            continue
    return max(t.count(x) for x in set(t)) + 1 if t != [] else -1


def runnersMeetings(startPosition, speed):
    return max(cardinality(startPosition[i:], speed[i:]) for i in range(len(speed)))
