import math
from abc import ABC, abstractmethod


class GeometryShape(ABC):

    def __init__(self, units):
        self.units = units

    @abstractmethod
    def area(self):
        # pass
        raise NotImplemented()


class Square(GeometryShape):

    def __init__(self, units, length):
        super().__init__(units)
        self.length = length

    def area(self):
        return self.length ^ 2


class Circle(GeometryShape):

    def __init__(self, units, radius):
        super().__init__(units)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ^ 2

class Triangle(GeometryShape):

    def __init__(self, units, sidea, sideb, sidec):
        super().__init__(units)
        # self.radius = radius

    def area(self):
        pass


class GeometryShapeFactory:
    @staticmethod
    def get_shape(shape_type: str, units: str, **kwargs):
        try:
            match shape_type:
                case 'circle':
                    return Circle(units, kwargs['radius'])
                case 'triangle':
                    return Triangle(units, kwargs['sidea'], kwargs['sideb'], kwargs['sidec'])
        except KeyError:
            raise ValueError('Unsuitable param for type', shape_type)


if __name__ == '__main__':
    # s = GeometryShape()
    # s.area()
    # s = Square('m',4)
    # c = Circle('cm', 5)
    my_shape = GeometryShapeFactory.get_shape("circle", 'm', 6)