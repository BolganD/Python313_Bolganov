class Automobile:
    def __init__(self, name, year, brand, engine, color, price):
        self.name = name
        self.year = year
        self.brand = brand
        self.engine = engine
        self.color = color
        self.price = price

    def input_info(self):
        print(' Данные автомобиля '.center(40, '*'))
        print(f'Название модели: {self.name}\nГод выпуска: '
              f'{self.year}\nПроизводитель: {self.brand}\nМощность двигателя: '
              f'{self.engine}\nЦвет машины: {self.color}\nЦена: {self.price}')
        print('=' * 40)


auto_1 = Automobile('X7 M50i', '2021', 'BMW', '530 л.с.', 'white', '10790000')
auto_1.input_info()