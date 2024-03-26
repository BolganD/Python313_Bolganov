class Point3DL:
    RIGHT = 'Правый операнд должен быть типом Point3DL'

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'{self.x}, {self.y}, {self.z}'

    def __add__(self, other):
        if not isinstance(other, Point3DL):
            raise ValueError(self.RIGHT)
        else:
            return f'({self.x + other.x}, {self.y + other.y}, {self.z + other.z})'

    def __sub__(self, other):
        if not isinstance(other, Point3DL):
            raise ValueError(self.RIGHT)
        else:
            return f'({self.x - other.x}, {self.y - other.y}, {self.z - other.z})'

    def __mul__(self, other):
        if not isinstance(other, Point3DL):
            raise ValueError(self.RIGHT)
        else:
            return f'({self.x * other.x}, {self.y * other.y}, {self.z * other.z})'

    def __truediv__(self, other):
        if not isinstance(other, Point3DL):
            raise ValueError(self.RIGHT)
        else:
            return f'({self.x / other.x}, {self.y / other.y}, {self.z / other.z})'

    def __eq__(self, other):
        if not isinstance(other, Point3DL):
            raise ValueError(self.RIGHT)
        else:
            return self.x == other.x and self.y == other.y and self.z == other.z

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError('Ключ должен быть строкой')
        if item == 'x':
            return self.x
        elif item == 'y':
            return self.y
        elif item == 'z':
            return self.z
        else:
            print('Неверный ключ')

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError('Ключ должен быть строкой')
        if key == 'x':
            self.x = value
        elif key == 'y':
            self.y = value
        elif key == 'z':
            self.z = value
        else:
            print('Неверный ключ')


c1 = Point3DL(12, 15, 18)
c2 = Point3DL(6, 3, 9)
print("Координаты 1-й точки:", c1)
print("Координаты 2-й точки:", c2)
print("Сложение координат:", c1 + c2)
print("Вычитание координат:", c1 - c2)
print("Умножение:", c1 * c2)
print("Деление:", c1 / c2)
print("Равенство координат:", c1 == c2)
print(f'x = {c1['x']} x1 = {c2['x']}\ny = {c1['y']} y1 = {c2['y']}\nz = {c1['z']} z1 = {c2['z']}')
c2['x'] = 20
c2['y'] = 20
c2['z'] = 20
print('Запись значения в координату x:', c1['x'])
