def find_area(s, n, m):
    if s == 1:
        return n * m
    elif s == 2:
        return n * m / 2
    elif s == 3:
        return 3.14 * (n * n / 4)
    else:
        return "Введен неверный номер фигуры"


g = int(input("Введите номер фигуры (1-прямоугольник, 2-треугольник, 3-круг): "))
e = int(input("Введите основание: "))
f = int(input("Введите высоту: "))
print(find_area(g, e, f))
