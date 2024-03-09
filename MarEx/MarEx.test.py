
class MainPoint:

    def __init__(self, first, second, third, four):
        self.first = first
        self.second = second
        self.third = third
        self.four = four

    def sum_p(self):
        return self.first + self.second

    def all_sum(self):
        return self.sum_p() / self.third

    def twice_sum(self):
        return f'Первый пример: {self.sum_p()}\nВторой пример: {self.all_sum(
        )}'

    def del_space(self):
        floats = self.four.split()
        n_f1 = float(floats[0])
        n_f2 = float(floats[1])
        n_f3 = float(floats[2])
        n_f4 = float(floats[3])
        n_f5 = float(floats[4])
        return (f'За 2019 год: {n_f1:.0%}\nЗа 2020 год: {n_f2:.0%}\nЗа 2021 '
                f'год:'
                f' {n_f3:.0%}\nЗа 2022 год: {n_f4:.0%}\n'f'За 2023 год: '
                                                         f'{n_f5:.0%}')
        # return (f'Первый год: {self.four[0]:.0%}, второй год: '
        #         f'{self.four[1]:.0%}, '
        #         f'третий год: {self.four[2]}')



        # four_s = []
        # for i in self.four:
        #     if i != ' ':
        #         four_s += i
        # return four_s


mp = MainPoint(2, 3, 2, input('-> '))
# print(mp.first, mp.second)
# print(mp.__dict__)
# print(f'EPS: {mp.sum_p()}')
# print(f'PS: {mp.all_sum()}')
# print(f'Оценка компании СБ: \n{mp.twice_sum()}')

# def work_show_num(sh_n):
#     if sh_n == 2:
#         return f'Оценка компании СБ: \n{mp.twice_sum()}'
#     elif sh_n == 3:
#         return f'PS: {mp.all_sum()}'
#     elif sh_n == 4:
#         return f'EPS: {mp.sum_p()}'


# show_num = int(input('Показать оценку компании (2) | Показать рентабельность('
#             '3)\nПоказать '
#       'див.политику(4) | Оценить компанию по показателям(5): '))
# print(work_show_num(show_num))
print(mp.__dict__)
print(mp.del_space())

# numbers = input("Введите числа через пробел: ")
# floats = numbers.split()
# n_f1 = float(floats[0])
# n_f2 = float(floats[1])
# n_f3 = float(floats[2])
# print(f'{n_f1}\n{n_f2:.0%}\n{n_f3:.0%}')