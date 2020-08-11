def makeArrayConsecutive2(statues):
    a = 0
    count = 0
    statues.sort()
    for i in range(0, len(statues) - 1):
        if statues[i] + 1 != statues[i+1]:
            a = statues[i+1] - statues[i] -1
            count += a
    return count

