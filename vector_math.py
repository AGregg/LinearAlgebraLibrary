from vector import *

def add(self, v):
    values = [x+y for x,y in zip(self.coordinates, v.coordinates)]
    return Vector(value)

def subtract(self, v):
    values = [x-y for x,y in zip(self.coordinates, v.coordinates)]
    return Vector(value)

def scalar_multiply(self, c):
    values = [c*x for x in self.coordinates]
    return Vector(value)

def negate(self):
    value = [-x for x in self.coordinates]
    return Vector(value)
