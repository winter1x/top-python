class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        print('getting x')
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('must be (int, float)')
        print(f'setting x {value}')
        self._x = value

    @property
    def y(self):
        print('getting y')
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('must be (int, float)')
        print(f'setting y {value}')
        self._y = value

    def point_print(self):
        print(f'Point x={self._x}, y={self._y}')

    def __str__(self):
        return f'Point x={self._x}, y={self._y}'

    def __add__(self, other):
        if not isinstance(other, Point):
            return False
        return Point(self._x + other._x, self._y + other._y)

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self._x == other._x and self._y == other._y

p1 = Point(1, 2)
print(p1.x)
print(p1.y)
p1.x = 5
p1.y = 8
p1.point_print()
print(p1)
p2 = Point(1, 2)
p1 += p2
print(p1)
print(p1 == Point(6, 10))