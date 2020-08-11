def christmasTree(levelNum, levelHeight):
    # Init Crown
    crown = ['*', '*', '***']

    # Draw Body
    body = []
    for i in range(0, 2 * levelNum, 2):
        for j in range(1, levelHeight + 1):
            body.append('*' * (2 * j + 3 + i))

    # Draw Foot
    foot = ['*' * (levelHeight + 1)] * levelNum if levelHeight % 2 == 0 else ['*' * levelHeight] * levelNum

    # Merge & Get longest Length
    tree = crown + body + foot
    l = len(max(tree, key=len))

    return [t.rjust(len(t) + int((l - len(t)) / 2), ' ') for t in tree]
