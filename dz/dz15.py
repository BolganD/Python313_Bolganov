# d = {
#     'circle': lambda r: r ** 2 * 3.14,
#     'rectangle': lambda w, h: w * h,
#     'trapezoid': lambda a, b, h: 0.5 * (a + b) * h
# }
# main = int(input("Площадь какой фигуры вы хотите найти (1: окружность; 2: прямоугольник; 3: трапеция): "))
# if 0 < main < 4 and main == 1:
#     r_in = int(input('Введите радиус окружности: '))
#     print('Площадь окружности радиуса ', r_in, ': ', d['circle'](r_in), sep="")
# if 0 < main < 4 and main == 2:
#     h_in = int(input('Введите длину прямоугольника: '))
#     w_in = int(input('Введите ширину прямоугольника: '))
#     print('Площадь прямоугольника размером ', h_in, " * ", w_in, ': ', d['rectangle'](h_in, w_in), sep="")
# if 0 < main < 4 and main == 3:
#     a_in = int(input('Введите первое основание трапеции: '))
#     b_in = int(input('Введите второе основание трапеции: '))
#     he_n = int(input('Введите высоту трапеции: '))
#     print('Площадь трапеции для a=', a_in, ', b=', b_in, ', h=', he_n, ': ', d['trapezoid'](a_in, b_in, he_n), sep="")
# elif 0 >= main >= 4:
#     print('Введен неверный номер фигуры. Повторите попытку')


d = {
    'circle': lambda r: r ** 2 * 3.14,
    'rectangle': lambda w, h: w * h,
    'trapezoid': lambda a, b, h: 0.5 * (a + b) * h
}


def find_p(main):
    if 0 < main < 4 and main == 1:
        r_in = int(input('Введите радиус окружности: '))
        print('Площадь окружности радиуса ', r_in, ': ', d['circle'](r_in), sep="")
    if 0 < main < 4 and main == 2:
        h_in = int(input('Введите длину прямоугольника: '))
        w_in = int(input('Введите ширину прямоугольника: '))
        print('Площадь прямоугольника размером ', h_in, " * ", w_in, ': ', d['rectangle'](h_in, w_in), sep="")
    if 0 < main < 4 and main == 3:
        a_in = int(input('Введите первое основание трапеции: '))
        b_in = int(input('Введите второе основание трапеции: '))
        he_n = int(input('Введите высоту трапеции: '))
        print('Площадь трапеции для a=', a_in, ', b=', b_in, ', h=', he_n, ': ', d['trapezoid'](a_in, b_in, he_n),
              sep="")
    elif 0 >= main >= 4:
        print('Введен неверный номер фигуры. Повторите попытку')


find_p(int(input("Площадь какой фигуры вы хотите найти (1: окружность; 2: прямоугольник; 3: трапеция): ")))
