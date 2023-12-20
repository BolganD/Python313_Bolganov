# name = "Dima"  # инициализация переменной
# print("Hello,", name)
# age = 20.3
# print(age)
# text = "Hello"
# print(age)
# print(text + " " + str(age))
# print(type(age))  # int - 20, float - 20.3
# print(type(text))  # str - "Hello"
# a = True
# print(type(a))  # bool - "True" "False"

# a = 4
# b = 5
# print(a, id(a))
# print(b, id(b))
#
# a = b
# print(a, id(a))
# print(b, id(b))

# a = b = c = 1
# print(a)
# print(b)
# print(c)

# a, b, c = 5, 'Hello', 9.2
# print(a)
# print(b)
# print(c)
# print(PI)
# PI = 2
# pr

# a = 15
# b = 200
# c = 17
# d = 32
# print("a:", a)
# print("b:", b)
# print("c:", c)
# print("d:", d)
#
# # c = a  # 1
# # a = b  # 2
# # b = c  # 1
#
# a, c, b, d = d, b, c, a
#
# print("a:", a)
# print("b:", b)
# print("c:", c)
# print("d:", d)

# print("строка \
#       символов")
# print('строка \nсимволов \rfile.txt')  # \r - возврат каретки
# print('строка \nсимволов D:\\folder\\file.txt')

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + ", " + s2 + "!\t\t"
# # print(s1 + ",", s2 + "!")
# print(s3 * 5)

# print(4505968490304747282123)
# print(4.505968490304747282123)

# print(6 + 2)
# print(6 - 2)
# print(6 // 2)  # 3.0 / 3
# print(6 * 2)
# print(6 // 4)  # 1
# print(6 / 3)  # 2.0
# print(6 ** 2)  # 36
# print(6 % 2)

# number = (6 + 4) * (5 ** 2 + 7)
# print(number)

# num = 10
# num += 5  # num=num+5
# print(num)
#
# num -= 3
# print(num)

# num = 4321
# print("Исходное число:", num)
# a = num % 10
# b = num % 100 // 10
# c = num % 1000 // 100
# d = num % 10000 // 1000
# a = num % 10
# num //= 10
# b = num % 10
# num //= 10
# c = num % 10
# num //= 10
# d = num % 10
# print(a)
# print(b)
# print(c)
# print(d)
# print(a * 1000 + b * 100 + c * 10 +d)

# res = num % 10 * 1000
# num //= 10
# res += num % 10 * 100
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print(res)

# num1 = "2.3"
# num2 = 3
# # res = num1 + str(num2)
# res = float(num1) + num2
# print(res)

# print(int(3.8))
# print(round(3.895, 2))
# print(type(round(3.895, 2)))

# name = "Виктор"
# age = 28
# print("Меня зовут", name + ". Мне", age, "лет.")
# print("Меня зовут", name, ". Мне", age, "лет.", sep=" ---", end=" ")
# print("Я учу Python.")

# name = input("Введите имя: ")
# print(name)

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# # num = int(num)
# res = num ** power
# print("Число", num, "в степени", power, "равно", res)
# print(type(num))

# b1 = True
# b2 = False
# print(b1 + 5)  # 1 + 5
# print(b2 + 5)  # 0 + 5

# False => "", 0, False, None

# print(bool("python"))
# print(bool(""))
# print(bool(-0.2))
# print(bool(0))
# print(bool(False))
# print(bool(None))
# test = None
# print(test)

# print(7 == "7")
# print(2 + 5 == 7)
# print(7 != 10 - 7)
# print(8 > 5)
# print(8 < 5)
# print(9 <= 9)
# print(9 >= 9)
# print("привет" > "ПРИВЕТ")

# print(2 > 4 - 3)
# print(2 * 5 > 7 >= 4 + 3)
# print(3 * 3 <= 7 >= 2)

# a = 10
# b = 5
# c = a == b
# print(a, b, c)  # 10 5 False

# print(5-3 == 2 and 1 + 3 == 4)  # True (True:True)
# print(5-3 == 2 and 1 + 3 < 4)  # False (True:False)
# print(5-3 > 2 and 1 + 3 == 4)  # False (False:True)
# print(5-3 < 2 and 1 + 3 < 4)  # False (False:False)

# print(5-3 == 2 or 1 + 3 == 4)  # True (True:True)
# print(5-3 == 2 or 1 + 3 < 4)  # True (True:False)
# print(5-3 > 2 or 1 + 3 == 4)  # True (False:True)
# print(5-3 < 2 or 1 + 3 < 4)  # False (False:False)

# print(9 - 7)  # 2
# print(not 9 - 7)  # False
# print(not 7 - 7)  # True

# cnt = 8
# if cnt < 10:
#     cnt += 2
#     print("Код верен: " + str(cnt))
# else:
#     print(cnt + 5)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")

# a = 15
# b = 15
# if a > b:
#     print("a > b")
# elif a == b:
#     print("a = b")
# else:
#     print("a < b")

# a = input("Введите первую сторону: ")
# b = input("Введите вторую сторону: ")
# c = input("Введите третью сторону: ")
# if a == b == c:
#     print("Треугольник равносторонний")
# if a == b or a == c or a == b:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")

# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:     # (day >= 1) and (day <= 5):
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели не существует")

# month = int(input("Введите номер месяца: "))
# if month == 1 or month == 2 or month == 12:
#     print("Зима")
# elif 3 <= month <= 5:
#     print("Весна")
# elif 6 <= month <= 8:
#     print("Лето")
# elif 9 <= month <= 11:
#     print("Осень")
# else:
#     print("Ошибка ввода данных")


# ЗАНЯТИЕ №3

# v = int(input("Введите количество ворон: "))
# if 0 <= v <= 9:
#     print("На ветке", v, end=" ")
#     if v == 1:
#         print("ворона")
#     elif 2 <= v <= 4:
#         print("вороны")
#     else:
#         print("ворон")
# else:
#     print("Ошибка ввода данных")

# password = "use"
# match password:
#     case 'admin':
#         print("Администратор")
#     case "user":
#         print("Пользователь")
#     case _:
#         print("Логин не найден")

# day = 'вторник'
# time = 14
# match day:
#     case "понедельник" | "вторник" | "среда" | "четверг" | "пятница" if 9 <= time <= 13 or 15 <= time <= 16:
#         print("Рабочий день")
#     case "суббота" | "воскресенье":
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или не рабочее время")


# a, b = 30, 20
#
# print(a if a > b else b)

# a, b = 30, 20
#
# print("a == b" if a == b else ("a > b" if a > b else "b > a"))

# a = 5
# b = 0
# print("на ноль делить нельзя" if b == 0 else a / b)
# print(a / b)

# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")
#
# print("Следующая строка")

# a = int(input("Введите числитель: "))
# b = int(input("Введите знаменатель: "))
# print('Результат:', a / b if b else 'На ноль делить нельзя')

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")


# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки или нельзя делить на ноль")
# else:  # работает когда в блоке try не возникло исключения
#     print("Всё нормально. Вы ввели числа", n, 'и', m)
# finally:
#     print("Конец программы")


# a = input("Введите первое число: ")
# b = input("Введите второе число: ")
# try:
#     a = int(a)  # a = 5
#     b = int(b)  # b = "два"
# except ValueError:
#     a = str(a)  # a = "5"
# finally:
#     print(a + b)


# Циклы while, for
# while

# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1  # i = i + 1

# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 1  # i = i - 1

# i = 2
# while i <= 20:
#     print("i =", i)
#     i += 2

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i)
#     i += 1


# ДЗ
# n = int(input("Введите кол-во символов: "))
# i = 0  # вертикально ("*\n" * n), горизонтально ("*" * n)
# while i <= n:
#     print("*")
#     i += 1


# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# res = 0
# while a <= b:  # 5 6 7 8 9 10
#     if a % 2:  # a % 2 != 0
#         res += a  # res(0) = 0 + a(1)
#     a += 1  # 0 + 1... 1 + 1... 2 + 1...
# print(res)

# a = int(input('Введите начало диапазона: '))  # 5
# b = int(input('Введите конец диапазона: '))  # 10
# if a % 2 == 0:  # 5
#     a += 1
# res = 0
# while a <= b:  # 5 <= 10
#     print("a =", a)
#     res += a  # res = 0 + 5
#     a += 2  # a = a + 2
# print(res)

# s = int(input("Введите кол-во символов: "))
# t = input("Введите тип символа: ")
# ol = int(input("Введите ориентацию символов (1 - вертикальная, 0 - горизонтальная): "))
# i = 0
# while i <= s:
#     if ol == 0:
#         print(t, end="")
#     else:
#         print(t)
#     i += 1

# n = input("Введите целое число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Повторите попытку ввода: ")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")


# n = input("Введите число: ")
#
# while type(n) != int and type(n) != float:
#     try:
#         n = int(n)
#     except ValueError:
#         try:
#             n = float(n)
#         except ValueError:
#             print("Число не целое и не вещественное!")
#             n = input("Повторите попытку ввода: ")
# n = int(n)
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# i = 0
# while i < 10:
#
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break


# res = 1
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     res *= n
# print(res)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i, end=" ")
#     i += 1
# else:
#     print("\nЦикл окончен, i =", i)

# j = 1
# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#
#     while j < 4:
#         print("\tВнутренний цикл: j=", j)
#         j += 1
#     i += 1


# t = 1
# while t < 10:
#     o = 1
#     while o < 10:
#         res = t * o
#         print(t, "*", o, "=", res, end="\t\t")
#         o += 1
#     print()
#     t += 1


# t = 0
# while t < 5:
#     o = 0
#     while o < 16:
#         if t % 2 == 0:
#             print("+", end="")
#         if t % 2 == 1:
#             print("-", end="")
#         o += 1
#     print()
#     t += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1


# i = 0
# while i < 5:
#     print(" " * i, "*")
#     i += 1


# for element in collection:
#   print(element)

# for i in "Hello!", "World", "!":
#     print(i)

# for i in range(n):
#   print(i)

# print(list(range(5)))

# range(start, stop,step)


# for i in range(9):
#     print(i, end=" ")
#
# print()
#
# i = 9
# while i > 0:
#     print(i, end=" ")
#     i -= 2

# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# m = 11
# n = 100
# for i in range(m, n + 1, 11):
#     print(i, end=" ")

# for i in range(1, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")


# raz = 1
# m = 100
# print('Добро пожаловать в игру "Угадай число"\nДля выхода из игры введите "0"')
# a = int(input("Введите число от 1 до 100: "))
# while a < m:
#     zg = 54
#     if a < zg:
#         print("Загаданное число больше", a)
#         a = int(input("Введите число от 1 до 100: "))
#         raz += 1
#     if a > zg:
#         print("Загаданное число меньше", a)
#         a = int(input("Введите число от 1 до 100: "))
#         raz += 1
#     if a == zg:
#         print("Поздравляем! Вы угадали число с", raz, "раза")
#         break
#     if a == 0:
#         print("Вы успешно вышли из игры")
#         break


# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print('done')

# for i in range(3): # 0 1 2
#     print("+++ i =", i)
#     for j in range(2): # 0 1
#         print("------ j =", j)

# a = int(input("Введите длину прямоугольника: "))
# b = int(input("Введите высоту прямоугольника: "))
# for i in range(b):
#     for j in range(a):
#         if i == 0 or i == b - 1 or j == 0 or j == a - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# nums = [letter * 2 for letter in "Banana"]
# nums = [i for i in range(30) if i % 2 == 0]
# print(nums)


# Список (list)
# nums = [8, 3, 2, 6, 9]
# print(nums)
# # print(type(nums))
# # print(nums[0])
# # print(nums[3])
# # # print(nums[6])  # IndexError
# # print(nums[-1])
# # print(nums[-2])
# #
# # nums[1] = 256
# # print(nums)
# # nums[3] += 100
# # print(nums)
# # print(len(nums))
# for i in range(len(nums)):
#     print(nums[i] ** 2)

# s = []
# print(s)
#
# b = list("Hello") # 'Hello' => []
# print(b)
# print(b[0])

# print(range(6))
# n = list(range(6))
# print(n)
#
# print(list(range(2, 11, 2)))

# [выражение for переменная in последовательность]

# a = [0 for _ in range(5)]
# print(a)
# n = 5
# b = [i ** 2 for i in range(1, n + 1)]
# print(b)

# a, b = [1, 2, 3], [4, 5]
# c = a + b
# print(c)
# d = b * 3
# print(d)

# a = [0] * int(input("Введите кол-во элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# s = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         s += a[i]
# print("Сумма: ", s)

# j = 0
# for i in a:
#     if i < 0:
#         j += i
# print(j)


# a = list(range(10, 100 + 1, 10))
# print(a)
# for i in range(len(a)):
#     print(a[i] + 2, end=" ")
# print()
#
# for i in a:
#     print(i + 2, end=" ")


# n = int(input('Введите количество элементов списка: '))
# a = [int(input('-> ')) for _ in range(n)]
#
# sum_negative = sum([num for num in a if num < 0])
# print('Сумма отрицательных элементов:', sum_negative)

# a = [int(input('-> ')) for _ in range(int(input("n = ")))]
# print('Сумма отрицательных элементов:', sum([num for num in a if num < 0]))

# n = list(range(21, 40 + 1))
# s = k = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]

# for i in n:
#     if i % 2 == 0:
#         k += 1
#     else:
#         s += i
#
# print("sum нечетных элементов: ", s)
# print("count четных элементов: ", k)


# n = list(range(21, 41))
# a = 2
# print(n[a])
# print(n[a-1])
# print(n[a+1])


# n = [int(input('-> ')) for _ in range(int(input('n = ')))]
# for i in range(1, len(n)):
#
#     # print(n[i], "-> ", end=" ")
#     # print(n[i - 1])
#     if n[i] > n[i - 1]:
#         print(n[i], end=" ")


# n = [int(input('-> ')) for _ in range(int(input('n = ')))]
# s = k = 0
# for i in range(len(n)):
#     if n[i] != 0:
#         k += 1
#     s += n[i]
# print(s / k)


# n = [int(input('-> ')) for _ in range(int(input('n = ')))]
# for i in range(len(n)):
#     if i % 2 == 0:
#         print(n[i], end=" ")

# a = [7, 8, 2, 1, 17, 9]
# print(a)
# # a[0], a[1] = a[1], a[0]
# print(a[1:4])
# print(a[1:])
# print(a[:1])
# print(a[4:1:-1])
# print(a[10:20])

# m = list(range(1, 8))
# print(m[0:7:1])
# print(m[::-1])
# print(m[::2])
# print(m[1::2])
# print(m[:1])
# print(m[-1:])
# print(m[3:4])
# print(m[4::])
# print(m[4:1:-1])
# print(m[2:5])

# s = [5, 7, 3, 8, 1, 9]
# print(s)
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# s[2:5] = []
# del s[1]
#
# print(s)

# Методы списков

# s = [5, 7, 3, 8, 1, 9]
# print(s)
# s.append(99)  # Добавляет элемент в КОНЕЦ списка
# print(s)
# s.extend([1, 2, 3])  # Добавляет список элементов в КОНЕЦ списка
# print(s)
# # s.extend('add')
# print(s)
# s.insert(0, 100)  # Добавляет элемент (второй параметр) в любой индекс (первый параметр) кроме последнего
# print(s)
# s.insert(30, 200)
# print(s)


# n = [int(input('-> ')) for _ in range(int(input('n = ')))]
# s = []
# n = int(input('Кол-во элементов в списке: '))
# for num in range(n):
#     x = int(input("Введите число: "))
#     s.insert(0, x)
# print(s)

# s = []
# n = int(input('Кол-во элементов в списке: '))
# for num in range(n):
#     x = int(input("Введите число кратное 3: "))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print("Число", x, "не делится на 3 без остатка.")
#
# print(s)

# a = [5, 3, 7, 6, 1, 2, 7, 5]
# b = [4, 1, 8, 5, 9, 7, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:  # если i находится в c
#             continue
#         if i == j:
#             c.append(i)
#             break
#
# print(c)  # [5, 7, 1]


# n = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# m = []
# for i in n:
#     if i in n:
#         continue
#     else:
#         m.append(i)
# print(m)

# a = [1, 2, 3]
# b = [11, 22, 33, 44, 55]
# c = []
#
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# print(c)

# a = [1, 2, 3, 44, 55]
# b = [11, 22, 33]
# c = []
#
# if len(a) > len(b):
#     a, b = b, a
#
# for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
# for i in range(len(a), len(b)):
#         c.append(b[i])

# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print(c)

# s = [2, 8, 5, 7, 8, 3, 1]
# print(s)
# s.remove(8)  # удаляет элемент по заданному значению
# print(s)
# s.pop()  # удаляет элемент по индексу; без параметров - удаляет послед.элемент из списка
# a = s.pop(-1)
# print(a)
# s.clear()  # очистка всех элементов списка
# print(s)

# n = [int(input('-> ')) for _ in range(int(input('n = ')))]
# k = int(input("Введите индекс: "))
# n.pop(k)
# print(n)

# s = [2, 8, 5, 7, 8, 3, 1]
# print(s)
# num = s.count(8)  # считает кол-во заданных значений в списке
# print(num)
#
# ind = s.index(8)  # возвращает индекс первого искомого элемента
# print(ind)
# ind = s.index(8, 2)
# print(ind)

# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# m = []
# n = []
# for el in a:
#     if el not in m:
#         m.append(el)
#         n.append(el)
#     else:
#         if el in n:
#             i = n.index(el)
#             n.pop(i)
# print(n)

# a = [1, 2, 3]
# b = a.copy()
# print("a =", a)
# print("b =", b)
# a.append(20)
# print("a =", a)
# print("b =", b)
# b.append(120)
# print("a =", a)
# print("b =", b)

# a = [5, 4, 3, 1, 2]
# print(a)
# a.reverse()  # Ставить список в обратном порядке
# print(a)
#
# a.sort() # Перестраивает по возрастанию, сортирует
# print(a)
# a.sort(reverse=True)
# print(a)
#
# # b = ["Виталий", "Сергей", "Александр", "Анна"]
# # b.sort(key=len)
# # print(b)
#
# a = [5, 4, 3, 1, 2]
# print(a)
#
# sort = sorted(a, reverse=True)  # Такой же sort()
# print(sort)
# print(a)

# a = [5, 4, 3, 1, 2]
# a.sort()
# print(a)

# Генерация случайных данных

# import random
#
# print(random.random())
# print(random.randint(3, 9))  # от 3 по 9 (включительно)
# print(random.randrange(3, 9, 2))  # от 3 до 9 (не включительно)
#
# print(random.uniform(10.5, 25.5))
# print(round(random.uniform(10.5, 25.5), 2))
#
# city_list = ['Москва', 'Новосибирск', 'Воронеж', 'Саранск', 'Томск']
# # print(random.choice(city_list))
# # print(random.choices(city_list, k=3))
# random.shuffle(city_list)
# print(city_list)
#
# s = [55, 32, 46, 57, 12, 40, 4, 6, 7, 2, 13, 422, 456, 30]
# # print(random.choices(s, k=5))


# lst = ['5', '4', '3', '2', '1']
# print(len(lst))
# print(sum(lst))
# print(min(lst))
# print(max(lst))

# a = 5
# print(a)
# s = [55, 32, 46, 57, 12, 40, 4, 6, 7, 2, 13, 422, 456, 30]
# print(sum(s))

# import random
# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# print(max(mas))
# max_ = max(mas)
# mas.remove(max_)
# mas.insert(0, max_)
#
# print(mas)

# import random
# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# min_ch = min(mas)
# print("min=", min_ch)
# ind_min = mas.index(min_ch)
# print("index min=", ind_min)
# # del mas[0: ind_min]
# print(mas[ind_min:])

# x = list('1a2b3c4d5f')
# print(x)
# print('a' in x)
# print('e' not in x)

# lst = []
# if not lst:
#     print("Список пустой")
# else:
#     print("В списке есть элементы")

# import random

# n1 = int(input("Введите размер 1 списка: "))
# n2 = int(input("Введите размер 2 списка: "))
# a = [random.randint(0, 10) for i in range(n1)]
# b = [random.randint(0, 10) for j in range(n2)]
# print("Первый список:", a)
# print("Второй список:", b)
# # c = a + b
# # print("Третий список:", c)
#
# c = []
# d = []
# for el in a:
#         if el not in b:
#             d.append(el)
#             c.append(el)
#         else:
#             if el in c:
#                 i = c.index(el)
#                 c.pop(i)
# print('Элементы обоих список без повторений:', c)
#
# e = []
# for el in a:
#     if el in b and el not in e:
#         e.append(el)
# print("Элементы общие для двух списков:", e)
#
# f = [min(a), min(b), max(a), max(b)]
# print(f)

# a = [random.randint(1, 5) for i in range(10)]
# b = []

# for i in a:
#     if

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# m = ['Hello', 'World']
# print(m)
# print(len(m))
# print(m[1][4])  # Первый [] - выбор внешнего индекса, второй - выбор внутреннего индекса

# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end='\t')
#     print()

# for row in m:
#     for x in row:
#         print(x, end='\t')
#     print()


# a = [random.randint(0, 9) for i in range(10)]
# c = []
# for i in a:
#     # ix = a.index(i)
#
#     if i not in c and i in a:
#         c.append(i)
# print(c)

# a = [random.randint(0, 9) for i in range(50)]
# c = []
#
# for el in a:
#     if el in c:
#         c.append(el)
#         ix = c.index(el)
#         c.pop(ix)
#
#     if len(c) < 10 and el not in c:
#         c.append(el)
#     if len(c) == 10:
#         break
# print("Уникальные случайные числа:", c)


# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# m = ['Hello', 'World']
# print(m)


# w, h = 4, 3
# matrix = [[0 for x in range(w)] for y in range(h)]
# matrix = []
# for y in range(h):
#     new_row = []
#     for x in range(w):
#         new_row.append(0)
#     matrix.append(new_row)
# print(matrix)

# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()

# w, h = 4, 3
# matrix = [[random.randint(-20, 10) for x in range(w)] for y in range(h)]
# m = 0
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#         if x < 0:
#             m += 1
#     print()
# print("Количество отрицательных элементов:", m)


# w, h = 4, 3
# matrix = [[input("-> ") for x in range(w)] for y in range(h)]
# m = 0
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()

# import math
#
# num1 = math.sqrt(4)  # нахождение корня
# num2 = math.ceil(3.1)  # Округление в верхнюю сторону
# num3 = math.floor(6.4)  # Округление в нижнюю сторону
#
# print(num1)
# print(num2)
# print(num3)
# print(math.pi)

# import math as m
# from math import sqrt, ceil
# # from math import *
# num1 = sqrt(4)
# num2 = ceil(4.6)
# print(num1)
# print(num2)

import time
import locale

locale.setlocale(locale.LC_ALL, "ru")


# seconds = time.time()
# print('Кол-во секунд:', seconds)
#
# locale_time = time.ctime(130188452)
# print("Местное время:", locale_time)
#
# res = time.localtime()
# print(res.tm_mday, ".", res.tm_mon, '.', res.tm_year, sep='')
#
# print(time.strftime("Today is %B %d, %Y"))
# # print(time.strftime("%d/%m/%Y, %A, %H:%M:%S", time.localtime()))
#
# start = time.monotonic()
# time.sleep(3)
# finish = time.monotonic()
# res = finish - start
# print(res)


# Function

# def hello(name):  # аргументы
#     print('Hello,', name)
#
#
# hello("Irina")  # параметры
# hello("Igor")


# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# get_sum("abc", "def")

# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#
#
# symbol(9, '+', '-')
# symbol(7, 'X', '0')


# def get_sum(a, b):
#     print("Сумма: ", end="")
#     return a + b
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
# print(res * 2)

# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(maximum(9, 16))
#
#
# def change(a, b):
#     if a > b:
#         return a / b
#     if a < b:
#         return a * b
#
#
# x = int(input("Введите число a: "))
# y = int(input("Введите число b: "))
# print(change(x, y))


# def cube(a):
#     return a ** 3
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))
#     time.sleep(1)


# def change(lst):
#     print(lst)
#     symbol1 = lst.pop(0)
#     symbol2 = lst.pop()
#     lst.append(symbol1)
#     lst.insert(0, symbol2)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))


# def change(lst):
#     print(lst)
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))


# def is_greater(x, y):
# #     if x > y:
# #         return True
# #     else:
# #         return False
# #
# #
# # a = 10
# # b = 15
# # print(is_greater(a, b))
# # print(is_greater(5, 10))
# #
# # if is_greater(a, b):
# #     print(a, "больше", b)
# # else:
# #     print(b, "больше", a)

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif 'a' <= ch <= 'z':
#             has_lower = True
#         elif '0' <= ch <= '9':
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надежный пароль")
# else:
#     print("Это ненадежный пароль")


# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d  # 1 + 5 + 0 + 5
#     # 1 + 5 + 2 + 1
#
#
# print(get_sum(1, 4, 2, 3))
# print(get_sum(1, 4, 2))
# print(get_sum(1, 4))
#
# print(get_sum(1, 5, d=2))


# def set_param(c=20, s="-"):
#     print(s * c)
#
#
# set_param()
# set_param(7)
# set_param(12, s="#")
# set_param(5, s="*")


# def digit_sum(n, even=True):
#     s = 0
#     while n > 0:
#         current = n % 10
#         if even and current % 2 == 0:
#             s += current
#         elif not even and current % 2:
#             s += current
#         n //= 10
#     return s
#
#
# print("Сумма четный цифр:")
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
# print("\nСумма нечетный цифр:")
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))


# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Dima", 22)
# display_info(23, "Dima")
# display_info(age=23, name="Dima")


# Изменяемые и неизменяемые объекты

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(id(lt1))
# print(id(lt2))
# print(lt1 == lt2)  # True
# print(lt1 is lt2)  # False
#
# a = "Hello"
# b = "Hello"
# print(id(a))
# print(id(b))
# print(a == b)  # True
# print(a is b)  # True


# Кортеж (tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())


# a = 5,
# print(type(a))
# # b = tuple()
# # print(type(b))
# print(a)

# n = 'Hello', 'Python'
# b = tuple(('Hello', 'Python'))
# print(type(b))
# print(b)

# a = (1, 2, 3, 4, 5, 6)
# print(a)
# print(a[3])  # 4
# print(a[1:3])  # (2, 3)
# a[1] = 3  # не работает - TypeError


# s = tuple(int(input("-> ")) for i in range(5))
# s = tuple(int(input("-> ")) for i in range(5))
# print(s)

from random import randint
#
# s = tuple(randint(1, 100) for i in range(5))
# print(s)

# s = tuple(2 ** i for i in range(1, 13))
# print(s)

# t1 = tuple("hello")
# t2 = tuple("world")
# print(t1)
# print(t2)
#
# t3 = t1 + t2
# print(t3)
# # t4 = list(t3)
# # t5 = t3.count('l')
# # print(t5)
# # if 'e' in t3:
# #     print(t3.index('e'))
#
# for i in t3:
#     print(i, end=' ')


# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             # a = tpl)  # 1
#             # b = tpl.index(el, a + 1)  # 4
#             return tpl[tpl.index(el):tpl.index(el, tpl.index(el) + 1) + 1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return tuple()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 2, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t, id(t))
# t[4][0] = 'new'
# t[4].append('hi')
# print(t, id(t))

# t = (1, 2, 3)
# x = t[0]
# y = t[1]
# z = t[2]
# x, y, z = t
# print(x, y, z)

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# # user = get_user()
# first_name, year, married = get_user()
# print(first_name, year, married)

# tpl = (1, 2, 3, 4, 5, 6)
# print(tpl)
# lst = list(tpl)
# print(lst)
# ptl1 = tuple(lst)
# print(ptl1)
# del ptl1

# countries = (
#     ("Германия", 80.2, (("Гамбург", 3.326), ("Берлин", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.43))),
# )
# print(countries, end="\n\n")
#
# for country in countries:
#     country_name, country_population, country_city = country
#
#     print("\nСтрана:", country_name, "| Население =", country_population)
#     for city in country_city:
#         city_name, city_population = city
#         print("\tГород:", city_name, "| Население =", city_population)
print("Внесены изменения")

