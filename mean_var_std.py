import numpy as np


def calculate(list):
    dict = {}
    arr = np.array(list)
    matrix = np.reshape(arr, (3, 3))
    dict['mean'] = [matrix.mean(0).tolist(), matrix.mean(
        1).tolist(), matrix.mean().flatten().tolist()[0]]
    print(dict)
    return []
