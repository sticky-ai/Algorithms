def avoidObstacles(inputArray):
    s = sorted(set(inputArray))
    m = max(s)

    for step_size in range(1, m+2):
        steps = set([x for x in range(0, m+step_size+1, step_size)])
        if len(steps.intersection(s)) == 0:
            return step_size

