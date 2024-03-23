class Point3DL:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'{self.x}, {self.y}, {self.z}'

    def __add__(self, other):
        return f'({self.x + other.x}, {self.y + other.y}, {self.z + other.z})'

    def __sub__(self, other):
        return f'({self.x - other.x}, {self.y - other.y}, {self.z - other.z})'

    def __mul__(self, other):
        return f'({self.x * other.x}, {self.y * other.y}, {self.z * other.z})'

    def __truediv__(self, other):
        return f'({self.x / other.x}, {self.y / other.y}, {self.z / other.z})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __getitem__(self, key):
        if key == 'x':
            return self.x
        if key == 'y':
            return self.y
        if key == 'z':
            return self.z

    def __setitem__(self, key, value):
        if key == 'x':
            self.x = value
        if key == 'y':
            self.y = value
        if key == 'z':
            self.z = value


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
c1['x'] = 20
print('Запись значения в координату x:', c1['x'])
