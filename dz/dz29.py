class Clock:
    DAY = 86400

    def __init__(self, sec):
        if not isinstance(sec, int):
            raise ValueError('Секунды должны быть целым числом')
        self.sec = sec % self.DAY

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f'{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}'

    @staticmethod
    def get_form(x):
        return str(x) if x > 9 else '0' + str(x)

    # def __add__(self, other):
    #     if not isinstance(other, Clock):
    #         raise ArithmeticError('Правый операнд должен быть типом Clock')
    #     return Clock(self.sec + other.sec)

    def __sub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый операнд должен быть типом Clock')
        return Clock(self.sec - other.sec)

    def __mul__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый операнд должен быть типом Clock')
        return Clock(self.sec * other.sec)

    def __floordiv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый операнд должен быть типом Clock')
        return Clock(self.sec // other.sec)

    def __mod__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый операнд должен быть типом Clock')
        return Clock(self.sec % other.sec)


c1 = Clock(1000)
c2 = Clock(700)
print(f'c1: {c1.get_format_time()}')
sub_c = c1 - c2
mul_c = c1 * c2
floordiv_c = c1 // c2
mod_c = c1 % c2
print(f'c1 - c2: {sub_c.get_format_time()}')
print(f'c1 * c2: {mul_c.get_format_time()}')
print(f'c1 // c2: {floordiv_c.get_format_time()}')
print(f'c1 % c2: {mod_c.get_format_time()}')
c1 -= c2
print(f'c1 -= c2: {c1.get_format_time()}')
c1 *= c2
print(f'c1 *= c2: {c1.get_format_time()}')
c1 //= c2
print(f'c1 //= c2: {c1.get_format_time()}')
c1 %= c2
print(f'c1 % c2: {c1.get_format_time()}')


