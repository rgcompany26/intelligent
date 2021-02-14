import numpy as np

def sumxy(min, max):
    if min >= max:
        return null
    sum = np.random.randint(min, max)
    y = np.random.randint(1, sum)
    x = sum - y
    return [x, y, sum, abs(x - y)]

