class Rectangle:

    def __init__(self, length, wig):
        self.len = length
        self.wig = wig

    def show_len_wig(self):
        print(f'Длина прямоугольника: {self.len}\nШирина прямоугольника: '
              f'{self.wig}')

    def find_square(self):
        print(f'Площадь прямоугольника: {self.len * self.wig}')

    def find_per(self):
        print(f'Периметр прямоугольника: {(self.len + self.wig) * 2}')

    def find_gip(self):
        print(f'Гипотенуза прямоугольника: '
              f'{round((self.len**2 + self.wig**2)**0.5, 2)}')

    def create_pic(self):
        for i in range(self.len):
            print('*' * self.wig)


show_rec = Rectangle(3, 100)
show_rec.show_len_wig()
show_rec.find_square()
show_rec.find_per()
show_rec.find_gip()
show_rec.create_pic()
