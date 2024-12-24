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

p1 = Point(1, 2)
print(p1.x)
print(p1.y)
p1.x = 5
p1.y = 8