class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other: 'Point'):
        if not isinstance(other, Point):
            raise TypeError('unsupported point and int')
        return Point(self.x+other.x, self.y+other.y)

    def __iadd__(self, other):
        return self.__add__(other)
    def __str__(self):
        return f"({self.x}, {self.y})"


if __name__ == '__main__':
    # p1 = Point(1,2)
    # p2 = Point(2,3)
    # print(p1 + p2)
    # p = p1
    # p1 += p2
    # print(p)
    # print(p1)

    l1 = [1,2,3]
    l2 = [10,20,30]
    print(l1 + l2)

    print('abc'+'def')

    print(l1 * 5)

    print('a'*10)
