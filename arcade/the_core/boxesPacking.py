def boxesPacking(length, width, height):
    boxes = sorted([sorted(box) for box in zip(*[length, width, height])])
    return all(boxes[i][j] < boxes[i+1][j] for j in range(len(boxes[0])) for i in range(len(boxes) - 1))
