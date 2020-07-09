import numpy as np

def rotateImage(a):
    t = np.transpose(a)
    return [i[::-1] for i in t]


