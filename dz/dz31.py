class ValidOrd:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError(f'Значение {self.__name} должно быть целым положительным числом')
        instance.__dict__[self.__name] = value


class Order:
    price = ValidOrd()
    c = ValidOrd()

    def __init__(self, name, price, c):
        self.name = name
        self.price = price
        self.c = c

    def all_c(self):
        return self.price * self.c


o = Order('apple', 5, 10)
# print(o.__dict__)
print(f'{o.all_c()}')