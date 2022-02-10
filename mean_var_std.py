import numpy as np


def calcMVS(func):
    axis1 = func(0).tolist()
    axis2 = func(1).tolist()
    flattened = func().flatten().tolist()[0]

    return [axis1, axis2, flattened]


def calcMetric(matrix, func):
    axis1 = func(matrix, axis=0).tolist()
    axis2 = func(matrix, axis=1).tolist()
    flattened = func(matrix)

    return [axis1, axis2, flattened]


def calculate(list):
    dict = {}
    arr = np.array(list)
    matrix = np.reshape(arr, (3, 3))
    dict['mean'] = calcMVS(matrix.mean)
    dict['variance'] = calcMVS(matrix.var)
    dict['standard-deviation'] = calcMVS(matrix.std)
    dict['max'] = calcMetric(matrix, np.amax)
    dict['min'] = calcMetric(matrix, np.amin)
    dict['sum'] = calcMetric(matrix, np.sum)

    print(dict)
    return dict
