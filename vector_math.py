from vector import *

def vectorAdd(x, y):
    value = []
    for i in range(len(x.coordinates)):
        print(i)
        value.append(x.coordinates[i] + y.coordinates[i])
    return Vector(value)
