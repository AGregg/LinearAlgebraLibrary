from vector import *

def vectorAdd(x, y):
    value = []
    for i in range(len(x.coordinates)):
        value.append(x.coordinates[i] + y.coordinates[i])
    return Vector(value)

def vectorSubtract(x, y):
    value = []
    for i in range(len(x.coordinates)):
        value.append(x.coordinates[i] - y.coordinates[i])
    return Vector(value)

def scalarMultiply(x, y):
    value = []
    for i in range(len(x.coordinates)):
        value.append(x.coordinates[i] * y)
    return Vector(value)

def vectorNegate(x):
    value = []
    for i in range(len(x.coordinates)):
        value.append(-x.coordinates[i])
    return Vector(value)
