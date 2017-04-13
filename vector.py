class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def add(self, v):
        value = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(value)

    def subtract(self, v):
        value = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(value)

    def scalar_multiply(self, c):
        value = [c*x for x in self.coordinates]
        return Vector(value)

    def negate(self):
        value = [-x for x in self.coordinates]
        return Vector(value)
