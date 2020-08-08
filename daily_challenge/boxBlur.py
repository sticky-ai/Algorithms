import numpy as np
def boxBlur(image):
    image = np.array(image)
    res = []
    for i in range(len(image) - 2):
        for j in range(len(image[0]) - 2):
            res.append(sum(sum(m) for m in image[i:i+3, j:j+3]) // 9)
    return np.reshape(res, (len(image) - 2, len(image[0]) - 2))
