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

# import time
# import locale
#
# locale.setlocale(locale.LC_ALL, "ru")

# seconds = time.time()
# print('Кол-во секунд:', seconds
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

# from random import randint


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
# print("Внесены изменения")
# print("Клонированный репозиторий")


# Множества (set {})

# s = {'banana', 'apple', 'orange', 'banana', 'apple'}
# print(s)
# print(type(s))
# print(len(s))

# c = ('red', 'blue', 'green', 'red')
#
# a = set(c)
# print(a, type(a))

# mas = [1, 2, 3, 4, 5, 6, 3, 3, 4, 9]
# s = {x for x in mas if x % 2 == 0}
# print(s)

# def to_set(element):
#     st = set(element)
#     return st, len(st)
#
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))

# t = {'red', 'blue', 'green'}
# # print('green' in t)
# for i in t:
#     print(i)

# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# a = [i for i in r if 'a' not in i]
# a = ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r]
# a = ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c']
# print(a)


# a = {"Tom", "Mark", "Wolf", "Carl"}
# print(a)
# a.add('Anna')
# print(a)
# a.remove("Tom")  # при обращении к несуществующему элементу - ошибка KeyError
# print(a)
# user = "Wolf"
# if user in a:
#     a.remove(user)
# print(a)
# a.discard("Mark")
# print(a)
# n = a.pop()
# print(n)
# print(a)
# a.clear()
# print(a)


# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a.union(b)
# c = a | b
# a |= b
# print(a)
# c = a & b
# a &= b
# print(c)
# print(a)
# c = a - b
# a -= b
# print(c)
# print(a)
# c = a ^ b
# a ^= b
# print(c)
# print(a)


# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# # s = s1.union(s2, s3, s4, s5, s6, s6, s7)
# s = s1 | s2 | s3 | s4 | s5 | s6 | s6 | s7
# print(s)
# count = len(s)
# print('Count', count)
# print('Min', min(s))
# print('Max', max(s))
# print('Sum', sum(s))

# s1 = set(input("Введите слово: "))
# s2 = "How are you"
# a = s1 & set(s2)
# print(a)
# for i in a:
#     print(i, end=" ")


# drawing = {'Марина', 'Женя', 'Света'}
# music = {'Костя', 'Женя', 'Илья'}
# one_hobby = drawing ^ music
# print("Один кружок: ", one_hobby)
# both_hobbies = drawing & music
# print("Два кружка: ", both_hobbies)
# drawing -= both_hobbies
# print("Кружок рисования: ", drawing)

# a = {0, 1, 2, 3, 4, 5}
# b = {3, 2, 1}
# print(a >= b)


# Тип frozenset
# s = frozenset([1, 2, 3, 4, 5])
# print(s)
# print(type(s))
# a = frozenset({'hello', 'world'})

# print(a)

# a = {0, 1, 2, 3, 4}
# print(a)
# b = list(a)
# print(b)


# Словарь

# lst = [1, 2, 3]
# d = {'one': 1, 'two': 2, 'three': 3, 4: 'four'}
#
# print(lst[0])
# print(d['one'])
# d['one'] = 10
# print(d['one'])
# print(d[4])

# d = {'one': 1, 'two': 2, 4: 'four'}
# print(d)
# print(type(d))
#
#
# d1 = dict(one=1, two=2, four='four')
# print(d1)
# print(type(d1))

# d = {0: 1, 'two': 2, (1, 2.3): 'кортеж', True: [2, 3, 4, 6]}
# print(d)
# print(d[True][1])
# print(d[(1, 2.3)])
# print(d['two'])
# print(d[0])

# lst = [('one', 1), ['two', 2], ['three', 3]]
# d = dict(lst)
# print(d)

# d = {a: a ** 2 for a in range(7)}
# print(d)

# d = {'one': 1, 'two': 2, 'four': 4}
#
# key = 'four'
# if key in d:
#     del d[key]

# try:
#     del d[key]
# except KeyError:
#     print(key + "Нет в словаре")
#
# for i in d:
#     print(i, '->', d[i])

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# m = 1
# for i in d:
#     m *= d[i]
# print(m)

# d = dict()
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")

# d = {i: input("-> ") for i in range(1, 5)}
# print(d)
# dislike = int(input("какой элемент исключить: "))
# del d[dislike]
# print(d[2])

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# print(sum(d))

# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core-i3-4670K', 3, 8500],
#     '3': ['AMD FX-63DD', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core-i5-3450', 5, 6400]
# }
# for i in goods:
#     print(i, ')', goods[i][0], ' - ', goods[i][1], ' шт. по ', goods[i][2], ' руб.', sep='')
#
# while True:
#     n = input('Введите номер товара: ')
#     if n != '0':
#         qty = int(input('Количество: '))  # 8
#         try:
#             goods[n][1] += qty  # goods['2'][1] = 8
#         except KeyError:
#             print("Неверный номер товара. (Допустимые: 1 - 5)")
#     else:
#         break

#     n = input('Введите номер товара: ')
#     if n != '0':
#         if n in goods:
#             qty = int(input('Количество: '))  # 8
#             goods[n][1] += qty  # goods['2'][1] = 8
#         else:
#             print("Неверный номер товара. (Допустимые: 1 - 5)")
#     else:
#         break
#
# for i in goods:
#     print(i, ')', goods[i][0], ' - ', goods[i][1], ' шт. по ', goods[i][2], ' руб.', sep='')


# d = {'a': 1, 'b': 2, 'c': 3}
#
# print(d.keys())  # список ключей
# print(d.values())  # список значений
# print(d.items())  # список ключей и значений

# for i, j in d.items():
#     print(i, j)

# print(list(d.values()))

# d = {'a': 1, 'b': 2, 'c': 3}

# d2 = d.copy()
# print('d:', d, id(d))
# print('d2:', d2, id(d2))
#
# d2['a'] = 5
# d['e'] = 6
#
# print('d:', d, id(d))
# print('d2:', d2, id(d2))
#
# d.clear()
# print('d:', d, id(d))
# print('d2:', d2, id(d2))

# print(d['b'])
# value = d.get('e', 'Такого ключа не существует')
# print(value)

# item = d.pop('e', "Такого ключа не существует")
# item = d.popitem()  # удаляет последний ключ и значение элемента
# print(item)
# print(d)
#
# a = [1, 2, 3]
# n = a.pop(0)
# print(n)


# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# d1 = d[]
# for i in d:
#     if i not in d1:
#         del d[i]
# print(d)
# print(d1)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# d1 = {'name': d['name'], 'salary': d['salary']}
#
# del d['name'], d['salary']
#
#
# print(d)
# print(d1)

# d = {'a': 1, 'c': 3, 'b': 2}
#
# d1 = {'r': 7, 'q': 40}
# d.update(d1)
# d2 = [('a', 20), ('b', 9)]  # {'a': 20, 'b': 9}
# d.update(d2)
# print(d)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# # x.update(y)
# # z = x.copy()
# new_dict = x | y
# print(new_dict)

# a = {
#     'first': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'second': {
#         4: 'four',
#         5: 'five'
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t', y, ': ', a[x][y], sep="")
#


# sales = {'John': {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
#          'Tom': {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3632},
#          'Anne': {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
#          'Fiona': {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451}}
#
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print('\t', y, ': ', sales[x][y], sep="")
#
# person = input('Имя: ')
# region = input('Регион: ')
# print(sales[person][region])
# new_data = int(input("Новое значение: "))
# sales[person][region] = new_data
# print(sales[person])

# d = {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694}
# new_d = {value: key for key, value in d.items()}
# print(new_d)

# d = {'N': 1, 'S': 2, 'E': 3, 'W': 4}  # 'N': 1, 'S': 2
# new_d = {k: v for k, v in d.items() if v <= 2}
# print(new_d)

# d = {'N': 1, 'S': 2, 'E': 3, 'W': 4}
# for i in range(2):
#     print('key:', list(d.items())[i][0], 'value:', list(d.items())[i][1])

# d = {'N': 1, 'S': 2, 'E': 3, 'W': 4}
# c = list(d)
# for key in c[:2]:
#     print(f'{key}: {d[key]}')
#
# for key, value in list(d.items())[2:4]:
#     print(f'{key}: {value}')

# d = {'N': 1, 'S': 2, 'E': 3, 'W': 4}
# value = list(d.items())
# print(value)

# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
#
# d = {}
# current_key = ''
# for item in a:
#     if type(item) == str:
#         d[item] = []  # {"one": []}
#         current_key = item  # current_key = 'one'
#     else:
#         d[current_key].append(item)  # d['one']
# print(d)


# d = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# print(d)
#
#
#
# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# f = {k: v for k, v in zip(b, a)}
# print(f)

# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# d = [4.5, 7.4, 9.6]
# # c = tuple(zip(a, b))
# # c = list(zip(a, b))
# # c = set(zip(a, b))
# c = list(zip(a, b, d))
# print(c)

# d_one = {'name': 'Igor', 'last_name': 'Petrov', 'job': 'Consultant'}
# d_two = {'name': 'Irina', 'last_name': 'Bolganova', 'job': 'Manager'}
#
# for (k1, v1), (k2, v2) in zip(d_one.items(), d_two.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)


# d = [(1, 'one'), (2, 'two'), (3, 'three')]
# a, b = zip(*d)
# print(a)
# print(b)


# a = ['one', 'three', 'two']
# b = [2, 3, 1]
#
# d = list(zip(a, b))
# print(d)
# d.sort()
# print(d)
# print(dict(d))
# d = dict(zip(a, b))
# v = sorted(d.items())
# print(v)
# print(dict(v))

# one = {'apple': 0.45, 'orange': 0.35}
# two = {'paper': 0.2, 'onion': 0.55}
# print({**one, **two})  # распаковали словарь
# print({**one})  # распаковали словарь
#
# for k, v in {**two, **one}.items():
#     print(k, '->', v)

# data = ['red', 'blue', 'yellow', 'green']
# num = 1
# for val in data:
#     print(num, ') ', val, sep='')
#     num += 1
# print()
# for num, val in enumerate(data, 1):
#     print(num, ') ', val, sep='')

# month = ['January', 'February', 'March']
# # total = [52000.00, 51000.00, 48000.00]
# # pc = [46800.00, 45900.00, 43200.00]
# #
# # for m, n1, n2 in zip(month, total, pc):
# #     print('Чистая прибыль в', m, n1 - n2)

# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)

# def func(*args):
#     # print(args)
#     # print()
#     return args
#
#
# print(func(2))
# print(func(2, 3, 4, 'abc'))

# def summa(*params):
#     res = 0
#     for i in params:
#         res += i
#     return res
#
#
# print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(summa(3, 4, 5))

# def to_dict(*args):
#     return {el: el for el in args}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict('grey', (2, 17), 3.11, -4))

# def func(*args):
#     r = sum(args) / len(args)
#     print(r)
#     # res = []
#     # for el in args:
#     #     if el < r:
#     #         res.append(el)
#     # return res
#     return [res for res in args if res < r]
#
#
# print(func(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(func(3, 6, 1, 9, 5))


# def func(a, *args):
#     return a, args
#
#
# print(func(1))
# print(func(1, 2, 3, 4, 5, 6, 7))

# def print_score(student, *scores):
#     print("Student Name: ", student)
#     for score in scores:
#         print(score)
#
#
# print_score('Dima', 5, 4, 3, 3, 5, 4)
# print_score('Sasha', 4, 2, 5, 5, 3, 4)
# print_score('Artur')

# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3, d='Dima'))
# print(func())
# print(func(d=9))


# def intro(**data):
#     for k, v in data.items():
#         print(k, '->', v)
#     print()
#
#
# intro(name='Dima', surname='Bolganov', age=22)
# intro(name='Yana', surname='Ivanova', email='yana@mail.ru',  age=19, phone='+7-909-324-47-47')


# def db(**kwargs):
#     my_dict.update(kwargs)
#
#
# my_dict = {'one': 'first'}
# db(k1=22, k2=32, k3=11, k4=91)
# db(name='Bob', age=31, weight=61, eyes_color='green')
# print(my_dict)


# def func(a, b, c, *args, d, e, **kwargs):
#     return a, b, c, args, e, kwargs, d
#
#
# print(func(5, 6, 7, 8, 9, 5, 5, 34, 4, e=100, k1=22, k2=32, k3=11, k4=91, d=55))


# name = 'Tom'
# print('глобальная область видимости: ', id(name))
#
#
# def hi():
#     # global name
#     name = 'Sam'
#     print('локальная область видимости: ', id(name))
#     surname = 'Johnson'
#     print('Hello', name, surname)
#
#
# def bye():
#     print('Good bye', name)
#
#
# hi()
# bye()
# print(name)
# print('глобальная область видимости: ', id(name))

# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()  # 5

# x = 4
#
#
# def add_five(a):
#     # x = 2
#
#     def add_some():
#         # x = 1
#         print('x =', x)
#         return a + x
#
#     return add_some()
#
#
# print(add_five(5))


# sum = 5

# lst = [9, 5, 3, 8]
# print(sum(lst))

# import builtins
# name = dir(builtins)
#
# for t in name:
#     print(t)

# def outer(who):
#     def inner():
#         print('Hello,', who)
#     inner()
#
#
# outer('World!')

# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print(a + b)  # 8
#
#     print('a:', a)  # 6
#     fun2(4)
#
#
# fun1()


# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a
#         a = 35
#         print('a:', a)
#
#     inner()
#     t = a
#
#
# fn()
# c = x + t  # 25 + 30 = 55
# print(c)


# def fn1():
#     x = 25
#
#     def fn2():
#         x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print('fn2.x =', x)
#
#     fn2()
#     print('fn1.x =', x)
#
#
# fn1()


# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# res = outer(2, 3, -1, 4)
# print(res)


# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# item1 = outer(5)
# print(item1(10))
#
# item2 = outer(8)
# print(item2(5))

# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = 'soft' + b
#         return a, b, c
#
#     return func2
#
# func = func1()
# print(func())

# def func(city):
#     count = 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         print(city, count)
#
#     return inner
#
#
# res1 = func('Москва')
# res1()
# res1()
# res2 = func('Сочи')
# res2()
# res2()
# res2()
# res1()
# res1()


# lambda (анонимная функция)

# print((lambda x, y: x + y)(1, 2))
#
# func = lambda x, y: x + y
# print(func(1, 2))

# print((lambda x, y: x**2 + y**2)(2, 5))

# print((lambda *args: args)(1, 2, 3, 4, 5, 6))

# y = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )
#
# for i in y:
#     print(i('abc  '))


# def outer(n):
#     def inner(x):
#         return x + n
#
#     return inner
#
#
# f = outer(5)
# print(f(10))
#
#
# def outer1(n):
#     return lambda x: x + n
#
#
# f1 = outer1(5)
# print(f1(10))
#
#
# outer2 = lambda n: lambda x: x + n
#
# f2 = outer2(5)
# print(f2(10))
#
#
# print((lambda n: lambda x: x + n)(5)(10))


# print((lambda x, y, z: x + y + z)(2, 4, 6))
# print((lambda n: lambda x: lambda y: n + x + y)(2)(4)(6))

# def func(item):
#     return item[1]
#
#
# d = {'b': 3, 'c': 1, 'a': 2}  # {'c': 2, 'a': 2, 'b': 3}
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])
# # lst.sort(key=func)
# print(lst)
# d1 = dict(lst)
# print(d1)


# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6},
# ]
#
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
#
# res1 = sorted(players, key=lambda item: item['rating'])
# print(res1)
#
# res2 = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res2)

# a = [
#     lambda x, y: x + y,
#     lambda x, y: x - y,
#     lambda x, y: x * y,
#     lambda x, y: x / y,
# ]
#
# print(a[0](5, 2))
# print(a[1](5, 2))
# print(a[2](5, 2))
# print(a[3](5, 2))

# d = {
#     1: lambda: print('Понедельник'),
#     2: lambda: print('Вторник'),
#     3: lambda: print('Среда'),
#     4: lambda: print('Четверг'),
#     5: lambda: print('Пятница'),
#     6: lambda: print('Суббота'),
#     7: lambda: print('Воскресенье')
# }
#
# d[5]()

# d = {
#     'circle': lambda r: r ** 2 * 3.14,
#     'rectangle': lambda w, h: w * h,
#     'trapezoid': lambda a, b, h: 0.5 * (a + b) * h
# }
#
# for i in
# main = int(input("Площадь какой фигуры вы хотите найти (1: окружность; 2: прямоугольник; 3: трапеция): "))
# if main != 0 and main < 3 and main == 1:
#     r_in = int(input('Введите радиус окружности: '))
#     print('Площадь окружности радиуса ', r_in, ': ', d['circle'](r_in), sep="")
# if main != 0 and main < 3 and main == 2:
#     h_in = int(input('Введите длину прямоугольника: '))
#     w_in = int(input('Введите ширину прямоугольника: '))
#     print('Площадь прямоугольника размером ', h_in, " * ", w_in, ': ', d['rectangle'](h_in, w_in), sep="")
# if main != 0 and main < 4 and main == 3:
#     a_in = int(input('Введите первое основание трапеции: '))
#     b_in = int(input('Введите второе основание трапеции: '))
#     he_n = int(input('Введите высоту трапеции: '))
#     print('Площадь трапеции для a=', a_in, ', b=', b_in, ', h=', he_n, ': ', d['trapezoid'](a_in, b_in, he_n), sep="")
# else:
#     print('Введен неверный номер фигуры. Попробуйте снова.')
# print('Площадь прямоугольника размером 10*13: ', d['rectangle'](10, 13))
# print('Площадь трапеции для a=7, b=5, h=3: ', d['trapezoid'](7, 5, 3))


# print((lambda a, b: a if a > b else b)(15, 13))
# print((lambda a, b, c: a if (a < b and a < c) else (b if b < c else c))(9, 13, 7))


# def fib2(n):  # return Fibonacci series up to n
#     """Return a list containing the Fibonacci series up to n."""
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)    # see below
#         a, b = a+b, b
#     return result
#
#
# fib = fib2(100)    # call it
# print(fib)

# t = (2.88, -1.75, 100.55)
# t2 = tuple(map(int, t))
# # t2 = tuple(map(lambda x: int(x), t))
# print(t2)


# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
# res = list(map(lambda x, y: (x , y), st, num))
# print(res)

# num = ['1', '2', '3']
# print(list(map(int, num)))

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l_s = list(map(lambda x, y: (x + y), l1, l2))
# print(l_s)

# t1 = ('abcd', 'efthssfh', 'vs', 'gif')
# t2 = tuple(filter(lambda s: len(s), t1))
# print(t2)

# b = [66, 98, 72, 68, 59, 60, 81, 74, 65]
# # res = list(filter(lambda s: s > 75, b))  # только проверяет условие (цикл с условием)
# res = list(map(lambda s: s + 5, b))  # только выполняет действие с каждым элементом (цикл без условия)
# print(res)


# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10))))
# print(m)
# n = [x ** 2 for x in range(10) if x % 2]
# print(n)

# import random
#
# my_list = [random.randint(1, 30) for i in range(20)]
# print(my_list)
#
# print(list(filter(lambda num: 10 <= num <= 20, my_list)))


# def hello():
#     return 'Hello, I am func "hello"'


# def super_func(func):
#     print('Hello, I am func "super_func"')
#     print(func())

#
# super_func(hello)


# def hello():
#     return 'Hello, I am func "hello"'
#
#
# test = hello
# print(test())


# Декораторы:

# def my_decor(func):
#     def wrap():
#         print('Код до функции')
#         func()
#         print('Код после функции')
#     return wrap
#
#
# def func_test():
#     print('Hello, I am func "func_test"')
#
#
# test = my_decor(func_test)
# test()

# def my_decor(func):  # декорирующая функция
#     def wrap():
#         print("*" * 30)
#         func()
#         print('=' * 30)
#     return wrap
#
#
# @my_decor  # декоратор
# def func_test():  # декорируемая функция
#     print('Hello, I am func "func_test"')
#
#
# @my_decor
# def hello():
#     print('Hello, I am func "hello"')
#
#
# func_test()
# hello()

# def bold(fn):
#     def wrap():
#         return '<b>' + fn() + '</b>'
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return '<i>' + fn() + '</i>'
#
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return 'text'
#
#
# print(hello())


# def cnt(fn):
#     count = 0
#
#     def wrap(arg1, arg2):
#         nonlocal count
#         count += 1
#         fn(arg1, arg2)
#         print('Вызов функции: ', count, '\n', '*' * 30, sep='')
#
#     return wrap
#
#
# @cnt
# def hello(a, b):
#     print('Hello', a, '\nHello', b)
#
#
# hello('Python', 'JavaScript')
# hello('one', 'two')
# # hello()

# def args_decor(fn):
#     def wrap(*args, **kwargs):
#         print('args', args)
#         print('kwargs', kwargs)
#         fn(*args, **kwargs)
#     return wrap
#
#
# @args_decor
# def print_data(a, b, c, study='Python'):
#     print(a, b, c, 'изучают', study, '\n')
#
#
# print_data('Борис,', 'Лиза,', 'Светлана', study='JavaScript')
# print_data('Дима', 'Сергей', 'Виктор')

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, '=', end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor('Сумма:', '+')
# def summa(a, b):
#     (print(a + b))
#
#
# @decor('Разность:', '-')
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)


# def decor(args1):
#     def args_dec(fn):
#         def wrap(x):
#             return fn(x) * args1
#         return wrap
#
#     return args_dec
#
#
# @decor(3)
# def p(a):
#     return a
#
#
# print(p(5))

# def dec(args1, args2):
#     def arg_dec(fn):
#         def wrap(v, x, y, z):
#             len_nums = len(fn(v, x, y, z))
#             # summa_sah = (v + x + y + z) / len_nums
#             print(args1, v, ', ', x, ', ', y, ', ', z, args2, (v + x + y + z) / len_nums, sep='')
#         return wrap
#     return arg_dec
#
#
# def summa(a, b, c, d):
#     s = a + b + c + d
#     print('Сумма чисел ', a, ', ', b, ', ', c, ', ', d, ' = ', s, sep='')
#
#
# @dec('Среднее арифметическое чисел ', ' = ')
# def sub(a, b, c, d):
#     return a, b, c, d
#
#
# summa(2, 3, 3, 4)
# sub(2, 3, 3, 4)


# print(int('18'))
# print(int(18.5))
# print(int(float('18.5')))

# print(int('100', 2))  # 4
# print(int('100', 8))  # 64
# print(int('100', 10))  # 100
# print(int('100', 16))  # 256

# print(bin(18))  # 0b10010 - двоичная сч
# print(oct(18))  # 0o22 - восьмеричная сч
# print(hex(18))  # 0x12 - шестнадцатеричная сч
#
# print(0b10010)
# print(0o22)
# print(0x12)
# print(0b10010 + 0o22 + 0x12 + 18)

# q = 'Pyt'
# w = "hon"
# e = q + w
# print(e)
# # print(e * -3)
# # print('y' in e)
# # print('y1' in e)
#
# # print(e[-6])
# # print(e[1:4])
# # print(e[2:])
# # print(e[::-1])
#
# e = e[:3] + 't' + e[4:]
# print(e)


# def changeCharToStr(s, c_old, c_new):
#     s2 = ''
#     i = 0
#
#     while i < len(s):
#         if s[i] == c_old:
#             s2 += c_new
#         else:
#             s2 += s[i]
#         i += 1
#     return s2
#
#
# str1 = 'Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования.'
#
# str2 = changeCharToStr(str1, 'N', 'P')
# print('str1 =', str1)
# print('str1 =', str2)


# print('Привет')
# print(u'Привет')

# print('C.\\folder\\file.txt\\')
# print(r'C.\folder\file.txt\\'[:-1])
# print(r'C.\folder\file.txt' + '\\')

# name = 'Дмитрий'
# age = 25
# print(f'Меня зовут {name}. Мне {age} лет.')
# m = 2.5643523
# print(f'Число: {round(m, 2)}')
# print(f'Число: {m:.3f}')

# x = 10
# y = 5
# print(f'{x = }, {y = }')
# print('x = ', x, ', y = ', y, sep='')

# print(f'{x} x {y} / 2 = {x * y / 2}')
# num = 74
# print(f'{{{{{num}}}}}')

# dir_name = 'my_doc'
# file_name = 'data.txt'
# print(fr'home\{dir_name}\{file_name}')
#
# s = """
# Многос
# тро
# чный\n текст
# """
# print(s)
# s1 = '''
# Многострочн'ый' "новый" тек\nст
# '''
# print(s1)

# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
# print(sum.__doc__)
# print(len.__doc__)


# from math import pi
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     print('Hello')
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)

# print(ord('a'))  # 97
# print(ord('й'))  # 97

# while True:
#     n = input('-> ')
#     if n != '-1':
#         print(ord(n))
#     else:
#         break


# s = 'Test string for me'
# arr = [ord(x) for x in s]
# print('ASCII коды:', arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print('Среднее арифметическое: ', arr)
# arr += [ord(x) for x in input('-> ')[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

# print(chr(97))
# print(chr(1048))
# print(chr(8364))

# print('apple' == 'Apple')  # 97 == 65
# print('apple' > 'Apple')  # 97 > 65
#
# print(ord('a'))
# print(ord('A'))

# a = 122
# b = 97
# all_num = [chr(z) for z in range(b, a + 1)]
# nums = str(all_num)
# print(nums)


# def ascii_nums(a, b):
#     if a < b:
#         all_num_v_a = [chr(z) for z in range(a, b + 1)]
#         return all_num_v_a
#     elif a > b:
#         all_num_v_b = [chr(z) for z in range(b, a + 1)]
#         return all_num_v_b
#
#
# x = int(input('a ->'))
# y = int(input('b -> '))
#
# print(ascii_nums(x, y))

# from random import randint
#
# SHORTEST = 7
# LONGEST = 10
# MIN_ASCII = 33
# MAX_ASCII = 126
#
#
# def random_password():
#     random_length = randint(SHORTEST, LONGEST)
#     result = ''
#     for i in range(random_length):
#         result += chr(randint(MIN_ASCII, MAX_ASCII))
#     return result
#
#
# print('Ваш случайный пароль:', random_password())

# s = 'hello, WORLD! I am learning Python.'

# print(s.capitalize())  # Hello, world! i am learning python.
# print(s.lower())  # hello, world! i am learning python.
# print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON.
# print(s.swapcase())  # HELLO, world! i AM LEARNING pYTHON.
# print(s.title())  # Hello, World! I Am Learning Python.
# print(s)
# # print(s.count('h'))  # возвращает кол-во точных вхождений подстроки в строку
# # print(s.count('h', 1, -4))
# print(s.find('Python', 10, -20))  # ищет в строке подстроку и возвращает его
# # индекс,
# # если совпадение не найден, то возвращает '-1'
# print(s.find('l'))
# print(s.rfind('l'))
#
# print(s.index('l'))
# print(s.rindex('l'))

# two_words = input('Введите два слова через пробел: ')
# s_one = two_words[:two_words.find(' ')]
# s_two = two_words[two_words.find(' ') + 1:]
# s_one, s_two = s_two, s_one
# print(s_one, s_two)

# print(s.startswith('hello'))  # возвращает True если строка начинает с
# # указанной подстроки
# print(s.find('I'))
# print(s.startswith('I am', 14))
# print(s.endswith('lo', 3, 5))
# print('abc123'.isalpha())
# print('abcABC'.isalpha())  # определяет, состоит ли строка только из букв
# print(''.isalpha())
# print('123'.isdigit())  # определяет, состоит ли строка из цифр
# print('123.234'.isdigit())
#
# print('abc123'.isalnum())  # определяет, состоит ли строка из букв и цифр
# print('abcA123'.isalnum())
#
# print('abc'.islower())  # определяет, является ли строки строчными буквами
# print('!#@ABC'.isupper())  # определяет, является ли строки заглавными буквами

# print('py'.center(10, '-'))
# print('py'.center(11, '-'))

# print('    py   '.lstrip())
# print('   py    '.rstrip())
# print('   py    '.strip())
#
# print('https://www.pythons.org'.lstrip("/:pths").rstrip('.org'))
# print('https://www.pythons.org'.strip('/:pths.org'))

# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(str1.replace('Nython', 'Python', 2))


# def sert(st1, st2, alst):
#     a = alst.replace(st1, st2, 1)
#     return a
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(sert('Nython','Python',str1))

# s1 = '-'
# seq = ('a', 'b', 'c')
# print(s1.join(seq))
# print('..'.join(['1', '2']))  # объединение итерируемой последовательности (
# # состоит из строковых значений) в строку
# print(':'.join('Hello'))

# s = 'hello, WORLD! I am learning Python.'
#
# print(s.split())
# print('www.python.org.ru'.rsplit('.', 1))
# print('www.python.org.ru'.split('.', 1))  # делит строку на список, состоящий
# # из подстрок


# a = input('-> ').split()
# a = int(a)
# print(a)

# a = input('-> ').split()
# print(a)
# print(a[0], a[1][0] + '.', a[2][0] + '.')


# a = list(map(int, input('Введите коды символов: ').split()))
# print(a)
#
# b = list(map(int, a))
# print(b)

import re

# s = 'Я ищу совпадения в 2024 году. И я их найду в 2 счёта. 200010 0002001'
# reg = r'\w+\s\w+$'
# print(re.findall(reg, s))  # возвращает список, содержащий все совпадения с
# # шаблоном
# print(re.search(reg, s))  # возвращает месторасположение первого совпадения с
# # шаблоном
# print(re.search(reg, s).span())
#
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
#
# print(re.search(reg, s).group())

# print(re.match(reg, s))  # возвращает месторасположение первого совпадения с
# шаблоном, но только вначале строки

# s = 'Я ищу совпадения в 2024 году. И я их найду в 2 счёта.'
# reg = r"\."
# print(re.split(reg, s))  # возвращает список, в котором строка разбита по
# # шаблону
#
# print(re.sub(reg, '!', s, 1))  # поиск и замена


# s = 'Я ищу совпадения в 2024 году. И я их найду в 2 счёта. 987654'
# # reg = r"[204]"
# # reg = r"[0-4]"
# # reg = r"[12][0-9][0-9][0-9]"
# reg = r"[^0-9]"
# print(re.findall(reg, s))

# print(ord('Ё'))
# print(ord('ё'))
#
# print(ord('А'))
# print(ord('а'))
#
# print(ord('Я'))
# print(ord('я'))

# main_str = input('Введите строку: ')
# # main_str = 'I am learning Python. hello, WORLD!'
# # print(main_str)
# st1 = main_str.find('h')
# st2 = main_str.rfind('h')
# change_str = main_str[st1 + 1:st2 + 1]
#
# print(main_str[:st1] + change_str[::-1] + main_str[st2:])


# st = ('Час в 24-часовом формате от 00 до 23. 2021-06-15Е22:55. Минуты, '
#       'в диапазоне от 00 до 59. 2021-06-15Т01:09.')
# req = r'[0-2][0-3]:[0-5][0-9]'
# print(re.findall(req, st))

# d = 'Цифры: 7, +17, --42, 0013, 0.3'
# print(re.findall(r'[+-]?\d+[.\d]*', d))

# st = "05-03-1987 # Дата рождения"
#
# print('Дата рождения:', re.sub('-', '.', re.sub(r"\s#.*", "", st)))
# print('Дата рождения:', re.sub('-', '.', re.sub(r"#.*", "", st)))

# st = 'author=Пушкин А.С; title = Евгений Онегин; price =200; year= 1831'
# req = r"\w+\s*=\s*[^;]+"
# print(re.findall(req, st))

# st = '12 сентября 2021 года 235'
# req = r"\d{,4}"
# print(re.findall(req, st))

# st = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578'
# req = r"[+]?7\d{10}"
# print(re.findall(req, st))

# def valid_login(name):
#     return re.findall(r'^[A-Za-z0-9_-]{6,16}$', name)  # 6 - 16,
#     # англ. буквы, _,
#     # -,
#     # [0-9]
#
#
# print(valid_login('Python_master'))
# print(valid_login('Python-Python'))


# s = ('Я ищу совпадения в 2024 году. И я их найду в 2 счёта. 987654 Hel_lo ['
#      '-World]')

# print(re.findall(r"\w+", "12 + й", flags=re.ASCII))
# print(re.findall(r"\w+", "12 + й", flags=re.A))
# print(re.findall(r"\w+", "12 + й", re.A))

# text = 'Hello world'
# print(re.findall(r'\w.+', text, re.DEBUG))

# s = 'Я ищу совпадения в 2024 году. И я их найду в 2 счёта.'
# reg = r'я'
# print(re.findall(reg, s, re.IGNORECASE))

# text = """
# one
# two
# """
# print(re.findall(r'one.\w+', text))
# print(re.findall(r'one.\w+', text, re.DOTALL))
# print(re.findall(r'one$', text))
# print(re.findall(r'one$', text, re.MULTILINE))

# print(re.findall(r'''[a-z.-]+
# @
# [a-z.-]+
# ''', 'test@mail.ru', re.VERBOSE))

# text = """Python,
# python,
# PYTHON"""
# reg = '(?mi)^python'
# print(re.findall(reg, text))

# test = ('123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, '
#         'login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru')
# req = r'[a-zа-я0-9._-]+@[a-zа-я._-]+'
# print(re.findall(req, test))

# text = "<body>пример жадного соответствия регулярных выражений</body>"
# print(re.findall("<.*?>", text))

# *?, +?, ??
# {m,n}?, {,n}?, {n,}?

# st = '12 сентября 2021 года 235'
# req = r"\d{3,4}?"
# print(re.findall(req, st))

# s = "<p>Изображение <img alt='Картинка' src='bg.jpg'> - фон страницы</p>"
# # reg = r'<img.*?>'
# reg = r"<img\s+[^>]*\s*=\s*[^>]+>"
# print(re.findall(reg, s))

# text = "Python (в русском языке встречаются названия пито́н[16] или па́йтон[17]) — высокоуровневый язык " \
#        "программирования общего назначения с динамической строгой типизацией " \
#        "и автоматическим управлением памятью[18][19]."
# req = r'\[\d+]'
# print(re.findall(req, text))

# s = 'Петр, Ольга и Виталий отлично учатся!'
# reg = 'Петр|Виктор|Ольга'
# print(re.findall(reg, s))

# s = 'int = 40, float = 4.0f, double = 8.0, float, int'
# # reg = r'\w+\s*=\s*\d[.\w]*'
# # reg = r'int\s*=\s*\d[.\w]*|float\s*=\s*\d[.\w]*'
# reg = r'(int|float)\s*=\s*\d[.\w]*'
# # print(re.findall(reg, s))
# print(re.search(reg, s).group())

# (?:...) - это группирующая скобка является не сохраняющей

# s = '127.0.0.1'
# # s = '127.168.255.255'
# # req = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
# req = r'(?:\d{1,3}.){3}\d{1,3}'
# print(re.findall(req, s))
# print(re.search(req, s).group())

# s = '5 + 7*2 - 4'
# reg = r'\s*([+*-])\s*'
# print(re.split(reg, s))

# a = '01-11-2021'
# pattern = '(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])'
# print(re.findall(pattern, a))
# print(re.search(pattern, a).group())

# s = 'Я ищу совпадения в 2024 году. И я их найду в 2 счёта.'
# reg = r'([0-9]+)\s(\D+)'  # ['2024 году. И я их найду в', '2024', 'году. И я их найду в']
# print(re.findall(reg, s))
# print(re.search(reg, s).group(1))
# m = re.search(reg, s)
# print(m[0], m[1], m[2])
# print(m[1])
# print(m[2])

# text = """
# Самара
# Москва
# Тверь
# Уфа
# Казань
# """
# count = 0
#
# def repl_find(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"
#
#
# print(re.sub(r'\s*(\w+)\s*', repl_find, text))


# s = "<p>Изображение <img src=\"bg.jpg\"> - фон страницы </p>"
# reg = r"<(img)\s+[^>]*src\s*=(?P<q>['\"])(.+?)(?P=q)>"
# print(re.findall(reg, s))
#
# # (?P<name>...)  (?P=name)

# s = 'Самолёт прилетает 10/23/2024. Будем рады вас видеть после 10/24/2024.'
# # 23.10.2024
# reg = r'(\d{2})/(\d{2})/(\d{4})'
# print(re.sub(reg, r'\2.\1.\3', s))

# s = 'yandex.com and yandex.ru'
# reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r'http://\1', s, re.IGNORECASE))

# s = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 7 499 456-45-78'
# reg = r'[+]?7\s?[(]?\d{3}?[)]?\s?\d{3}?\s?[-]?\d{2}?\s?[-]?\d{2}?'
# print(re.findall(reg, s))


# Рекурсия


# def elevator(n):  # 0
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print('->', n)
#     elevator(n - 1)  # 5 4 3 2 1
#     print(n, end='')
#
#
# n1 = int(input('На каком вы этаже?: '))  # 5
# elevator(n1)

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9]))


# def sum_list(lst):  # [1, 3, 5, 7, 9]
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         return lst[0] + sum_list(lst[1:])  #
#
#
# print(sum_list([1, 3, 5, 7, 9]))


# def to_str(n, base):  # n = 15
#     convert = "0123456789ABCDEF"
#     if n < base:  # 254 < 16
#         return convert[n]  # convert[15] => 'F'
#     else:
#         return to_str(n // base, base) + convert[n % base]  # convert[14] => 'E'
#         # '5'
#
#
# print(to_str(254, 2))
# print(to_str(15, 2))
# print(to_str(15, 8))
# print(to_str(15, 16))


# names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea',
#                                                                     'Bill'],
#          'Ann']
# print(names)
# print(len(names))
# print(names[0])
# print(isinstance(names[0], list))
# print(names[1])
# print(isinstance(names[1][1], list))


# def count_item(lst):
#     count = 0
#     for item in lst:
#         if isinstance(item, list):
#             count += count_item(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_item(names))


# def remove(text):
#     if not text:
#         return ''
#     if text[0] == '\t' or text[0] == ' ':
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
#
# print(remove(" Hello\tWorld"))


# def nums(num):
#     c = 0
#     for i in num:
#         if i < 0:
#             c += 1
#         # else:
#         #     c += 1
#     return c
#
#
# o_n = [-2, 3, 8, -11, -4, 6]
# print(nums(o_n))


# Файлы

# Текстовые
# Бинарные


# f = open('test.txt', 'r')
# print(*f)
# print(f)
#
# f.close()
# print(f.closed)
# print(f.mode)
# print(f.name)
# print(f.encoding)

# f = open('test1.txt', 'r')
#
# print(f.readline())  # считали одну строку из файла
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# f.close()

# f = open('test1.txt', 'r')
# print(f.readlines(16))  # считали все данные из файла и вернули список строк
# print(f.readlines())
# f.close()

# f = open('test1.txt', 'r')
# for l in f:
#     print(l)
# f.close()

# f = open('test1.txt', 'r')
# c = 0
# for i in f:
#     c += 1
# print(c)
# f.close()

# f = open('xyz.txt', 'a')
# f.write('New text\n')
# f.close()

# f = open('xyz.txt', 'w')
# line = ['This is line 1\n', 'This is line 2\n']
# f.writelines(line)
# f.close()

# f = open('xyz.txt', 'w')
# lst = [str(i) for i in range(1, 20)]
# print(lst)
# for index in lst:
#     f.write(index + '\t')
# f.close()

# f = open('text2.txt', 'w')
# f.write('Замена строки в текстовом файле;\nизменить строку в '
#         'списке;\nзаписать список в файл;\n')
# f.close()
#
# f = open('text2.txt', 'r')
# rl = f.readlines()
# print(rl)
# rl[1] = 'Hello World\n'
# print(rl)
# f.close()
#
# f = open('text2.txt', 'w')
# f.writelines(rl)
# f.close()

# f = open('text2.txt', 'w')
# f.write('Замена строки в текстовом файле;\nизменить строку в '
#         'списке;\nзаписать список в файл;\n')
# f.close()
#
# f = open('text2.txt', 'r')
# rl = f.readlines()
# f.close()
#
# pos = int(input('pos = '))
# if 0 <= pos < len(rl):
#         del rl[1]
# else:
#         print('Введен неверно.')
#
# print(rl)
#
# f = open('text2.txt', 'w')
# f.writelines(rl)
# f.close()

# def input_index():
#     file = open('text2.txt', 'r')
#     read_text = file.readlines()
#     file.close()
#     index = int(input('Введите номер строки: '))
#     if index not in range(1, len(read_text) + 1) or index < 1:
#         print('Убедитесь что введен корректный номер строки и повторите попытку.')
#         return input_index()
#     else:
#         return read_text, index - 1
#
#
# t, i = input_index()
#
# f = open('text2.txt', 'w')
# del t[i]
# f.writelines(t)
# f.close()

# f = open('test.txt', 'r')
# print(f.read(3))
# print(f.tell())  # возвращает текущую позицию условного курсора в файле
# print(f.seek(1))
# print(f.read())
# print(f.tell())
# f.close()

# f = open('test.txt', 'r+')
# print(f.write('I am learning Python'))
# print(f.tell())
# print(f.seek(3))
# print(f.write('-new string-'))
# print(f.tell())
# f.close()

# with open('test.txt', 'w+') as f:
#     print(f.write('01234\n56789'))
#
# with open('test.txt', 'r+') as f:
#     for line in f:
#         print(line[:3])

# file_name = 'res_1.txt'
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     print(lt)
#     return ' '.join(lt)
#
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))
#
#
# with open(file_name, 'r') as f:
#     nums = f.read()
#
# print(nums)
#
# nums_list = list(map(float, nums.split()))
# print(sum(nums_list))
# print(len(nums_list))
#
# print('Done!')

# def longest_worlds(file):
#     with open(file, 'r', encoding='utf-8') as text:
#         w = text.read().split()
#         max_length = len(max(w, key=len))  # длина самого длинного слова
#         print(max_length)
#         res = [word for word in w if len(word) == max_length]
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# print(longest_worlds('world.txt'))

# one = 'one.txt'
# two = 'two.txt'

# text = ('Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока '
#         '№6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n')
# with open(one, 'r') as fr, open(two, 'w') as fw:
#     for line in fr:
#         line = line.replace('Строка', 'Линия -')
#         fw.write(line)


# Модуль OS и OS.PATH

import os

# print(os.getcwd())  # путь к текущей директории
#
# print(os.listdir())  # список директории и файлов
# print(os.listdir('..\..'))

# os.mkdir("folder1")  # создание папки

# os.makedirs("nested1/nested2/nested3")

# os.rmdir('folder1')

# os.remove('xyz.txt')  # удаление файла

# os.rmdir('nested1')

# os.rename('nested1', 'tested')  # переименовать папку

# os.rename('world.txt', 'tested/worlds.txt')  # переименовать файл и
# перенести его в заданную директорию

# os.renames('two.txt', 'folder1/file.txt')  # переименовали файл и переместили
# в заданную директорию, при этом может создать промежуточные директории

# print(os.listdir())

# for root, dirs, files in os.walk('tested', topdown=False):
#     print('Root:', root)
#     print('Subdirs:', dirs)
#     print('Files:', files)


# def remove_empty_dirs(root_tree):
#     print(f'Удаление пустых директорий в ветви {root_tree}')
#     print('-' * 50)
#
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f'Директория {root} удалена')
#
#     print('-' * 50)
#
#
# remove_empty_dirs('tested')

# import os.path

# print(os.path.split(r'D:\Python\PyCharmProject\tested\nested2\test1.txt')[0])
# print(os.path.dirname(r'D:\Python\PyCharmProject\tested\nested2\test1.txt'))
# print(os.path.basename(r'D:\Python\PyCharmProject\tested\nested2\test1.txt'))
#
# print(os.path.join(r'D:\Python', 'PyCharmProject', 'tested', 'test1.txt'))

# dirs = [r'Work\F1', r'Work\F2\F21']
# for d in dirs:
#     os.makedirs(d)
# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\F21': ['f211.txt', 'f212.txt']
# }
#
# for d, f in files.items():
#     for file in f:
#         file_path = os.path.join(d, file)
#         print(file_path)
#         open(file_path, 'w').close()


# file_with_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F2\F21\f211.txt', r'Work\F2\F21\f212.txt']
# for file in file_with_text:
#     with open(file, 'w') as f:
#         f.write(f'Какой-то текст для файла расположенного по пути: {file}')


# def print_tree(root, topdown):
#     print(f'Обход {root} {"сверху вниз" if topdown else "снизу вверх"}')
#     for root, dirs, files in os.walk(root, topdown):
#         print(root)
#         print(dirs)
#         print(files)
#     print('-' * 50)
#
#
# print_tree('Work', False)
# print_tree('Work', True)

# print(os.path.exists(r'D:\Python\PyCharmProject\tested\nested2\test1.txt'))
#
# print(os.path.isfile(r'D:\Python\PyCharmProject\tested\nested2\test1.txt'))
# print(os.path.isdir(r'D:\Python\PyCharmProject\tested\nested2\test1.txt'))

import time

#
# path = 'main.py'
# # print(f"{os.path.getsize('main.py')} bytes")
# # print(os.path.getsize('main.py') // 1024)
# #
# print(time.strftime('%d.%m.%Y, %H:%M:%S', time.localtime(os.path.getatime(
#     path))))  #
# # возвращает время
# # последнего доступа к
# # файлу
# print(time.strftime('%d.%m.%Y, %H:%M:%S', time.localtime(os.path.getctime(
#     path))))  #
# print(time.strftime('%d.%m.%Y, %H:%M:%S', time.localtime(os.path.getmtime(
#     path))))  #  # возвращает время последнего изменения файла

# file_path = r'tested\nested2\nested3\text2.txt'
# if os.path.exists(file_path):
#     dirs, name = os.path.split(file_path)
#     print(f'{name}, ({dirs}) - последний доступ к файлу: '
#           f'{os.path.getatime(file_path)}')
# else:
#     print(f'Файл {file_path} не существует')

# def directory(main_dir):
#     for root, dirs, files in os.walk(main_dir):
#         for rand_dir in dirs:
#             print(f'Имя: {str(rand_dir)}; Тип: dir')
#         # print(f'Root: {root}')
#         # print(f'Dirs: {dirs}')
#         # print(f'Files: {files}')
#
#         for file in files:
#             file_p = os.path.join(root, file)
#             weight = os.path.getsize(file_p)
#             print(f'Имя: {str(file)}; Тип: file; Размер: {weight} bytes')
#
#
#
#
# directory('Work')

# dir_name = 'tested'
# objs = os.listdir(dir_name)
# print(objs)
#
# for obj in objs:
#     p = os.path.join(dir_name, obj)
#     # print(p)
#     if os.path.isfile(p):
#         print(f'{obj} - file - {os.path.getsize(p)} bytes')
#     elif os.path.isdir(p):
#         print(f'{obj} - dir')


# ООП

# В классах могут быть: свойства(поля, переменные) и методы(функции)
# class Point:
#     x = 1
#     y = 1
#
#
# p1 = Point()
# p1.x = 5
# p1.y = 24
# print(p1.x)
# print(p1.y)
# print(p1.__dict__)
# print(id(p1))
#
# p2 = Point()
# p2.x = 10
# print(p2.x + p1.x)
# print(p2.__dict__)
# print(id(p2))
#
# print(id(Point))


# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self, x, y):  # def set_coord(p1):
#         self.x = x  # p1.x = 5
#         self.y = y  # p1.y = 24
#         print(self.__dict__)
#
#
# p1 = Point()
# # p1.x = 5
# # p1.y = 24
# p1.set_coord(5, 24)
# # Point.set_coord(p1)
#
#
# p2 = Point()
# # p2.x = 10
# # p2.y = 30
# p2.set_coord(10, 30)


# class Human:
#     name = 'name'
#     birthday = '00.00.0000'
#     phone = '00-00-00'
#     country = 'country'
#     city = 'city'
#     address = 'street, house'
#
#     def print_info(self):
#         print(' Персональные данные '.center(40, '*'))
#         print(f'Имя: {self.name}\nДата рождения: {self.birthday}\nНомер '
#               f'телефона: {self.phone}\nСтрана: {self.country}\nГород: '
#               f'{self.city}\nДомашний адрес: {self.address}')
#         print('=' * 40)
#
#     def input_info(self, n, b, p, co, ci, ad):
#         self.name = n
#         self.birthday = b
#         self.phone = p
#         self.country = co
#         self.city = ci
#         self.address = ad
#
#     def set_address(self, address):
#         self.address = address
#
#     def get_address(self):
#         return self.address
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info('Юля', '23.05.1986', '45-46-98', 'Россия', 'Москва',
#               'Чистопрудный бульвар, 1А')
# h1.print_info()
# h1.set_address('ул. Ленина, 56')
# h1.print_info()
# print(h1.get_address())
# print()
# h1.set_name('Дима')
# h1.print_info()
# print(h1.get_name())


# class Person:
#     skill = 10  # статическое свойство
#     count = 0
#
#     def __init__(self, name, surname):
#         self.name = name  # динамическое свойство
#         self.surname = surname
#         # print(f'Инициализатор класса {self}')
#         Person.count += 1
#
#     # def __del__(self):
#     #     print('Удаление экземпляра', self)
#     #
#     # def print_info(self):
#     #
#     #     print(f"Данные сотрудника: {self.name} {self.surname}")
#     #
#     # def add_skill(self, k):
#     #     self.skill += k
#     #     print(f'Квалификация сотрудника: {self.skill}', end='\n\n')
#
#
# p1 = Person('Дмитрий', 'Болганов')
# # p1.print_info()
# # p1.add_skill(3)
# # p1 = 5
# print(p1.count)
#
# p2 = Person('Анна', 'Долгова')
# # p2.print_info()
# # p2.add_skill(2)
# print(p2.count)
#
# print(Person.count)


# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print(f'Инициализация робота: {self.name}')
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, 'выключается!')
#         Robot.k -= 1
#
#         if Robot.k == 0:
#             print(self.name, 'был последним')
#         else:
#             print('Работающих роботов осталось:', Robot.k)
#     def print_welcome(self):
#         print(f"Приветствую! Меня зовут: {self.name}")
#
#
# droid1 = Robot('R2-D2')
# droid1.print_welcome()
# print(f'Численность роботов: {Robot.k}')
# print()
# droid2 = Robot('C-3PO')
# droid2.print_welcome()
# droid3 = Robot('HP-7')
# droid3.print_welcome()
# print(f'Численность роботов: {Robot.k}')
# print('\nЗдесь роботы могут проделать какую-то работу\n')
# print('Роботы закончили свою работу. Давайте их выключим')
# del droid1
# del droid2
# del droid3
# print(f'Численность роботов: {Robot.k}')


# class Automobile:
#     def __init__(self, name, year, brand, engine, color, price):
#         self.name = name
#         self.year = year
#         self.brand = brand
#         self.engine = engine
#         self.color = color
#         self.price = price
#
#     def input_info(self):
#         print(' Данные автомобиля '.center(40, '*'))
#         print(f'Название модели: {self.name}\nГод выпуска: '
#               f'{self.year}\nПроизводитель: {self.brand}\nМощность двигателя: '
#               f'{self.engine}\nЦвет машины: {self.color}\nЦена: {self.price}')
#         print('=' * 40)
#
#
# auto_1 = Automobile('X7 M50i', '2021', 'BMW', '530 л.с.', 'white', '10790000')
# auto_1.input_info()

# class Rectangle:
#
#     def __init__(self, length, wig):
#         self.len = length
#         self.wig = wig
#
#     def show_len_wig(self):
#         print(f'Длина прямоугольника: {self.len}\nШирина прямоугольника: '
#               f'{self.wig}')
#
#     def find_square(self):
#         print(f'Площадь прямоугольника: {self.len * self.wig}')
#
#     def find_per(self):
#         print(f'Периметр прямоугольника: {(self.len + self.wig) * 2}')
#
#     def find_gip(self):
#         print(f'Гипотенуза прямоугольника: '
#               f'{round((self.len**2 + self.wig**2)**0.5, 2)}')
#
#     def create_pic(self):
#         for i in range(self.len):
#             print('*' * self.wig)
#
#
# show_rec = Rectangle(3, 9)
# show_rec.show_len_wig()
# show_rec.find_square()
# show_rec.find_per()
# show_rec.find_gip()
# show_rec.create_pic()


# class Point:
#     __slots__ = ['__x', '__y', 'z']
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def get_coord(self):
#         return self.__x, self.__y
#
#     def __check_value(c):
#         if isinstance(c, int) or isinstance(c, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print('Координаты должны быть числами')
#
#     def get_x(self):
#         return self.__x
#
#     def get_y(self):
#         return self.__y
#
#     def set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print('Координата', x, 'должна быть числом')
#
#     def set_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print('Координата', y, 'должна быть числом')
#
#
# p1 = Point(5, 10)
# p1.z = 1
# print(p1.z)
#
# p1.set_x(20.6)
# p1.set_y(30)
# p1.set_y('aaa')
# print(p1.__check_value())
# print(p1.get_coord())
# p1.set_coord(100, 'abc')
#
# print(p1.get_coord())
# p1.__x = 100
# p1.y = 'abc'
# print(p1.x, p1.y)
# print(p1.get_x())
# print(p1.get_y())
# print(p1.__dict__)
# print(Point.__dict__)
# print(p1._Point__x)
# p1._Point__x = 'asf'
# print(p1.__dict__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __get_x(self):
#         return self.__x
#
#     def __get_y(self):
#         return self.__y
#
#     def __set_x(self, x):
#         self.__x = x
#
#     def __set_y(self, y):
#         self.__y = y
#
#     x = property(__get_x, __set_x)
#
#
# p1 = Point(5, 10)
# # print(p1.get_x())
# print(p1.x)
# p1.x = 100
# print(p1.x)
# # print(Point.__dict__)
# print(p1.__dict__)

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         if not isinstance(x, (int, float)):
#             raise TypeError("Устанавливаемое значение должно быть числом") #
#             # Исключение выбрасывает
#             # print()
#         self.__x = x
#
#     def __get_y(self):
#         return self.__y
#
#     def __set_y(self, y):
#         self.__y = y
#
#     @x.deleter
#     def x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     # x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# # print(p1.get_x())
#
# p1.x = 100
# print(p1.x)
# print(p1.__dict__)


# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print('Килограммы задаются только числами')
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#     def print_data(self):
#         print(self.__kg, 'кг => ', end='')
#         print(self.to_pounds(), 'фунтов')
#
#
# weight = KgToPounds(12)
# weight.print_data()
# weight.kg = 41
# weight.print_data()
# weight.kg = 'ABSD'
# weight.print_data()
# print(weight.__dict__)


# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#     # get_count = staticmethod(get_count)
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# print(p1.get_count())
# print(Point.get_count())


# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(round(Change.inc(10) / Change.dec(10), 2))


# class Args:
#     @staticmethod
#     def maxi(*my_list):
#         return max(my_list)
#
#     @staticmethod
#     def mini(*my_list):
#         return min(my_list)
#
#     @staticmethod
#     def s_arif(*my_list):
#         return sum(my_list) / len(my_list)
#
#     # @staticmethod
#     # def factorial(num):
#     #     if num == 1:
#     #         return 1
#     #     else:
#     #         return Args.factorial(num - 1) * num
#     @staticmethod
#     def factorial(num):
#         fact = 1
#         for i in range(1, num + 1):
#             fact *= i
#         return fact
#
#
# print(f'Максимальное число: {Args.maxi(3, 5, 7, 9)}')
# print(f'Минимальное число: {Args.mini(3, 5, 7, 9)}')
# print(f'Среднее арифметическое число: {Args.s_arif(3, 5, 7, 9)}')
# print(f'Факториал числа {5}: {Args.factorial(5)}')

# from math import sqrt
#
#
# class Square:
#     count = 0
#
#     @staticmethod
#     def square_triangle1(a, b, c):
#         Square.count += 1
#         p = (a + b + c) / 2
#         return sqrt(p * (p - 2) * (p - b) * (p - c))
#
#     @staticmethod
#     def square_triangle2(a, b):
#         Square.count += 1
#         return 0.5 * a * b
#
#     @staticmethod
#     def square_area(a):
#         Square.count += 1
#         return a * a
#
#     @staticmethod
#     def square_rectangle(a, b):
#         Square.count += 1
#         return a * b
#
#     @staticmethod
#     def get_count():
#         return Square.count
#
#     def print_info(self):
#         print(self, 'Hello')
#
#
# area = Square()
# area.print_info()
# Square.print_info(area)
# print(f'Площадь треугольника по формуле Гер'
#       f'она: {Square.square_triangle1(3, 4, 5)}')
# print(f'Площадь треугольника через основание и высоту:'
#       f' {Square.square_triangle2(6, 7)}')
# print(f'Площадь квадрата: {Square.square_area(7)}')
# print(f'Площадь прямоугольника: {Square.square_rectangle(2, 6)}')
# print(f'Количество подсчетов площади: {Square.get_count()}')


# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split('.'))
#         date1 = cls(day, month, year)  # date1 = Date(23, 10, 2024
#         return date1
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count('.') == 2:
#             day, month, year = map(int, date_as_string.split('.'))
#             return day <= 31 and month <= 12 and year <= 3999
#
#     def string_to_db(self):
#         return f'{self.year}-{self.month}-{self.day}'
#
#
# dates = [
#     '30.12.2023',
#     '20-12-2020',
#     '01.01.2024',
#     '12.31.2020'
# ]
#
# for string_date in dates:
#     if Date.is_date_valid(string_date):
#         date = Date.from_string(string_date)
#         print(date.string_to_db())
#     else:
#         print('Неправильная дата или формат строки с датой')

# date2 = Date.from_string('23.10.2024')
# print(date2.string_to_db())
# date3 = Date.from_string('13.12.2022')
# print(date3.string_to_db())
# string_date = '23.10.2024'
# day, month, year = map(int, string_date.split('.'))
# print(day, month, year)
# time_date = Date(day, month, year)
# print(time_date.string_to_db())

# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     su_r = 'RUB'
#     su_u = 'USD'
#     su_e = "EUR"
#
#     def __init__(self, surname, num, percent, value=0):
#         self.surname = surname
#         self.num = num
#         self.percent = percent
#         self.value = value
#         print(f'Счет #{self.num} принадлежащий клиенту {self.surname} был '
#               f'открыт.')
#         print('*' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счет №{self.num} принадлежащий клиенту {self.surname} был '
#               f'закрыт.')
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f'Состояние счета в долларах: {usd_val} {Account.su_u}')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f'Состояние счета в евро: {eur_val} {Account.su_e}')
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percent(self):
#         self.value += self.value * self.percent
#         print('Проценты были успешно начислены')
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению у вас нет {val} {Account.su_r}")
#         else:
#             self.value -= val
#             print(f'{val} {Account.su_r} были успешно сняты')
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f'{val} {Account.su_r} были успешно добавлены')
#         self.print_balance()
#
#     def print_balance(self):
#         print(f'Текущий баланс: {self.value} {Account.su_r}')
#
#     def print_info(self):
#         print('Информация о счете:')
#         print('-' * 20)
#         print(f'#{self.num}')
#         print(f'Владелец: {self.surname}')
#         self.print_balance()
#         print(f'Проценты: {self.percent:.0%}')
#         print('-' * 20)
#
#
# acc = Account('Долгих', '12345', 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(1)
# acc.convert_to_eur()
# acc.edit_owner('Дюма')
# acc.print_info()
# acc.add_percent()
# print()
# acc.withdraw_money(100)
# print()
# print()
# acc.add_money(4470)
# print()
# acc.withdraw_money(3000)

# import re
#
#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         # self.verify_fio(fio)
#         # self.verify_old(old)
#         # self.verify_weight(weight)
#         # self.verify_ps(ps)
#
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError('ФИО должно быть строкой')
#         f = fio.split()  # ['Волков', 'Игорь', 'Николаевич']
#         if len(f) != 3:
#             raise TypeError('Неверный формат ФИО')
#         # letters = ''.join(re.findall("[a-za-Яё-]", fio, re.IGNORECASE))
#         # for s in f:
#         if re.findall(r"[^a-za-яё\s-]", fio, re.IGNORECASE):
#             raise TypeError('В ФИО можно использовать только буквы и дефис')
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or old < 14 or old > 120:
#             raise TypeError('Возраст должен быть целым числом в диапазоне от '
#                             '14 до 120 лет')
#
#     @staticmethod
#     def verify_weight(weight):
#         if not isinstance(weight, float) or weight < 20 or weight > 120:
#             raise TypeError('Вес должен быть вещественным числом от 20 кг до '
#                             '120кг')
#
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError('Паспорт должен быть строкой')
#         s = ps.split()  # ['1234', '345678']
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError('Неверный формат паспорта')
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError('Серия и номер паспорта должны быть числами')
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @property
#     def password(self):
#         return self.__password
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @old.setter
#     def old(self, old):
#         self.verify_old(old)
#         self.__old = old
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#     @weight.setter
#     def weight(self, weight):
#         self.verify_weight(weight)
#         self.__weight = weight
#
#
# p1 = UserData('Волков Игорь Николаевич', 22, '1234 345678', 75.7)
# p1.fio = 'Волков Игорь Анатольевич'
# p1.old = 54
# p1.password = '3411 544567'
# p1.weight = 43.1
# print(p1.fio)
# print(p1.old)
# print(p1.password)
# print(p1.weight)

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x}, {self.__y})'
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1) -> None:
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width
#         print('Инициализатор базового класса Prop')
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         super().__init__(*args)
#         print('Переопределенный инициализатор Line')
#         # Prop.__init__(self, *args)
#
#     def draw_line(self) -> None:
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.get_width()}')


# class Rect(Prop):
#     def draw_rect(self):
#         print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, '
#               f'{self._width}')


# line = Line(Point(1, 2), Point(10, 20), 'yellow', 5)
# line.draw_line()
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.draw_rect()


# DRY (Don't Repeat Yourself) - не повторяйся

# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         self.width = width
#         self.height = height
#         super().__init__(color)
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError('Некорректное значение ширины')
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError('Некорректное значение высоты')
#
#     def area(self):
#         print(f'Площадь {self.color} прямоугольника = ', end='')
#         return self.__width * self.__height
#
#
# rect = Rectangle(10, 20, 'green')
# print(rect.area())


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x}, {self.__y})'
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1) -> None:
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print('Координаты должны быть числами')
#
#
# class Line(Prop):
#     def set_coord(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print('Координаты должны быть целочисленными значениями')
#
#     def draw_line(self) -> None:
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# class Rect(Prop):
#     def draw_rect(self):
#         print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, '
#               f'{self._width}')
#
#
# line = Line(Point(1, 2), Point(10, 20), 'yellow', 5)
# line.set_coord(Point(15.6, 45), Point(100, 20))
# line.draw_line()
#
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.set_coord(Point(55.5, 45.5), Point(100, 200))
# rect.draw_rect()


# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rec(self):
#         print(f'Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}')
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         self.fon = background
#         super().__init__(width, height)
#
#     def show_rec(self):
#         super().show_rec()
#         print('Фон:', self.fon)
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, border, line, color):
#         super().__init__(width, height)
#         self.border = border
#         self.line = line
#         self.color = color
#
#     def show_rect(self):
#         super().show_rec()
#         print(f'{self.show_border()} \n{self.show_line()} \n{self.show_color()}')
#
#
#     def show_border(self):
#         return f'Ширина границы: {self.border}'
#
#     def show_line(self):
#         return f'Тип границы: {self.line}'
#
#     def show_color(self):
#         return f'Цвет границы: {self.color}'
#
#
# shape1 = RectFon(400, 200, 'yellow')
# shape1.show_rec()
# shape2 = RectBorder(600, 300, '1px', 'solid', 'red')
# shape2.show_rect()


# class Vector(list):
#     def __init__(self, lst):
#         self.lst = lst
#
#     def __str__(self):
#         return ' '.join(map(str, self.lst))
#
#
# v = Vector([1, 2, 3])
# print(sum(v))
# print(v)
# print(type(v))


# Перегрузка методов


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1) -> None:
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coord(self, sp=None, ep=None):
#         if ep is None:
#             if sp.is_int():
#                 self._sp = sp
#             else:
#                 print('Координата sp должна быть целочисленным значением')
#         elif sp is None:
#             if ep.is_int():
#                 self._ep = ep
#             else:
#                 print('Координата ep должна быть целочисленным значением')
#         else:
#             if sp.is_int() and ep.is_int():
#                 self._sp = sp
#                 self._ep = ep
#             else:
#                 print("Координаты должны быть целочисленными значениями")
#
#
# line = Line(Point(1, 2), Point(10, 20), "yellow", 5)
# line.draw_line()
# line.set_coord(Point(15, 45), Point(100, 200))
# line.draw_line()
# line.set_coord(Point(55, 55))
# line.draw_line()
# line.set_coord(ep=Point(90, 20))
# line.draw_line()


# Абстрактные методы


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1) -> None:
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def draw(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод draw()")
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#     def draw(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Ellipse(Prop):
#     def draw(self):
#         print(f"Рисование эллипса: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10, 10), Point(20, 10)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
# figs.append(Ellipse(Point(-10, -10), Point(10, 10)))
#
# for f in figs:
#     f.draw()

# from math import pi
#
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         self._width = width
#         self._length = length
#         self._radius = radius
#
#
# class Rectangle(Table):
#     def __init__(self, width, length):
#         super().__init__(width=width, length=length)
#
#     def show_res(self):
#         return self._width * self._length
#
#
# class Circle(Table):
#     def __init__(self, radius):
#         super().__init__(radius=radius)
#
#     def show_res(self):
#         return round(pi * self._radius ** 2)
#
#
# tables = [Rectangle(20, 10), Rectangle(20, 20), Circle(radius=20)]
#
# for t in tables:
#     print(f'{}\nПлощадь стола: {t.show_res()}')


# Абстрактные классы

#
# from abc import ABC, abstractmethod
#
#
# class Chess(ABC):  # абстрактный класс
#     def draw(self):
#         print("Нарисовал шахматную фигуру")
#
#     @abstractmethod
#     def move(self):
#         print('Метод move() в базовом классе')
#
#
# class Queen(Chess):
#     # def move(self):
#     #     super().move()
#     #     print('Ферзь перемещен на e2e4')
#     pass
#
#
# # q = Chess()
# q = Queen()
# q.draw()
# # q.move()

# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     @abstractmethod
#     def print_value(self):
#         print(self.value, end=' ')
#
#     def show(self):
#         print(f' =  {self.convert_to_rub():.2f} RUB')
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = 'USD'
#
#     def convert_to_rub(self):
#         return self.value * Dollar.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=' ')
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = 'EUR'
#
#     def convert_to_rub(self):
#         return self.value * Euro.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=' ')
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
#
# d += e
# for elem in d:
#     elem.print_value()
#     elem.show()

# for elem in e:
#     elem.print_value()
#     elem.show()


# Интерфейсы

# from abc import ABC, abstractmethod
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print('Child')
#
#
# class GrandChild(Child):
#     def display2(self):
#         print('GrandChild')
#
#
# gc = GrandChild()
# gc.display2()
# gc.display1()


# Вложенные классы

# def outer():
#     a = 5
#
#     def inner():
#         print(a)
#
#     inner()
#
# outer()


# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def static_method():
#         print('Статический метод')
#
#     def outer_method(self):
#         print('метод в наружном классе')
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print('Вложенный класс', MyOuter.age, self.obj.name)
#             MyOuter.static_method()
#             self.obj.outer_method()
#
#
#
# out = MyOuter('Дима')
# inner = out.MyInner('внутренний', out)
# print(inner.inner_name)
# inner.inner_method()

# class Color:
#     def __init__(self):
#         self.name = 'Green'
#         self.lg = self.LightGreen()
#
#     def show(self):
#         print('Name:', self.name)
#
#     class LightGreen:
#         def __init__(self):
#             self.name = 'Light Green'
#
#         def display(self):
#             print('Name:', self.name)
#
#
# outer = Color()
# outer.show()
# outer.lg.display()


# class Intern:
#     def __init__(self):
#         self.name = 'Smith'
#
#     def display(self):
#         print('Name:', self.name)
#
#
# class Employee:
#     def __init__(self):
#         self.name = 'Employee'
#         self.intern = Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print('Name:', self.name)
#
#     class Head:
#         def __init__(self):
#             self.name = 'Alba'
#
#         def display(self):
#             print('Name:', self.name)
#
#
# outer = Employee()
# outer.show()
# d1 = outer.intern
# d1.display()
# d2 = outer.head
# d2.display()


# class Outer:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print('Outer')
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass()
#
#         def show(self):
#             print('Inner')
#
#         class InnerClass:
#
#             def show(self):
#                 print('InnerClass')
#
#
# outer = Outer()
# outer.show()
# # inner1 = outer.inner
# # inner1.show()
# inner2 = outer.inner.inner_inner
# inner2.show()


# class Computer:
#     def __init__(self):
#         self.name = 'PC001'
#         self.os = self.Os()
#         self.cpu = self.CPU()
#
#     class Os:
#         def system(self):
#             return 'Windows 10'
#
#     class CPU:
#         def make(self):
#             return 'Intel'
#
#         def model(self):
#             return 'Core-i7'
#
#
# comp = Computer()
# # my_os = comp.os
# # my_cpu = comp.cpu
# my_os = Computer.Os()
# my_cpu = Computer.CPU()
# print(f'{comp.name}:\nOs: {my_os.system()}\nCpu: {my_cpu.make()} {my_cpu.model()}')


# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.i = self.Infor()
#
#     def show_infor(self):
#         print(f'{self.name} => {self.i.m}, {self.i.p}, {self.i.me}')
#
#     class Infor:
#         def __init__(self):
#             self.m = 'HP'
#             self.p = 'i7'
#             self.me = '16'
#
#
# show_students = Student('Roman')
# show_students.show_infor()


# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f'{self.__class__}: {self.name}'
#
#     def __str__(self):
#         return f'{self.name}'
#
#
# cat = Cat('Пушок')
# print(cat)


# class Point:
#     def __init__(self, *args):
#         self.__coord = args
#
#     def __len__(self):
#         return len(self.__coord)
#
#
# p = Point(1, 2, 3, 4, 5, 6)
# print(len(p))

import math

# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)

#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# p = Point(1, 2)
# print(p.length)
# p.length = 20
# print(p.length)


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt1 = Point(1, 2)
# pt2 = Point2D(1, 2)
#
# print('pt1 =', pt1.__sizeof__())
# print('pt2 =', pt2.__sizeof__() + pt2.__dict__.__sizeof__())
#
# # print(pt1.__dict__)
# # print(pt2.__dict__)


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = 'z',
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#
# pt1 = Point(1, 2)
#
# pt3 = Point3D(10, 20, 30)
# # pt3.z = 30
# print(pt3.x, pt3.y, pt3.z)


# Множественное наследование

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name, 'is sleeping')
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + ' is playing')
#
#
# class Dog(Animal, Pet):
#     def __init__(self):
#         print('Инициализатор Dog')
#     def bark(self):
#         print(self.name + ' is barking')
#
#
# dog = Dog('Buddy')
# dog.bark()
# dog.play()
# dog.sleep()


# class A:
#     def __init__(self):
#         print('Инициализатор класса А')
#
#     def hi(self):
#         print('A')
#
#
# class AA:
#     def __init__(self):
#         print('Инициализатор класса AA')
#
#     def hi(self):
#         print('A')
#
#
# class B(A):
#     def __init__(self):
#         print('Инициализатор класса B')
#
#
# class C(AA):
#     def __init__(self):
#         print('Инициализатор класса C')
#
#     # def hi(self):
#     #     print('C')
#
#
# class D(B, C):
#     def __init__(self):
#         C.__init__(self)
#         B.__init__(self)
#         print('Инициализатор класса D')
#
#
# d = D()
# d.hi()
# print(D.mro())
# # print(D.__mro__())


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'{self.__x}, {self.__y}'
#
#
# class Styles:
#     def __init__(self, color='red', width=1):
#         print('Инициализатор Styles')
#         self._color = color
#         self._width = width
#
#
# class A:
#     def __init__(self):
#         print('Инициализатор класса А')
#
#
# class Pos(A):
#     def __init__(self, sp: Point, ep: Point, color='red', width=1):
#         print('Инициализатор Pos')
#         self._sp = sp
#         self._ep = ep
#         # Styles.__init__(self, color, width)
#         # super().__init__(color, width)
#
#
# class Line(Pos, Styles):
#     def draw(self):
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# l1 = Line(Point(10, 10), Point(100, 100), 'green', 5)
# l1.draw()
# print(Line.mro())


# Миксины

# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:
#     def log(self, message, filename='logfile.txt'):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message, filename=''):
#         super().log(message, filename='sublog.txt')
#
#
# subclass = MySubClass()
# subclass.display('Строка будет отображаться и запишется в файл')


# class Goods:
#     def __init__(self, name, weight, price):
#         print('Инициализатор Goods')
#         self.name = name
#         self.weight = weight
#         self.price = price
#         super().__init__()
#
#     def print_info(self):
#         print(f'{self.name}, {self.weight}, {self.price}')
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print('Инициализатор MixinLog')
#         MixinLog.ID += 1
#         self.id = MixinLog.ID
#
#     def save_sell_log(self):
#         print(f'{self.id}: товар был продан в 00:00 часов')
#
#
# class NoteBook(Goods, MixinLog):
#     pass
#
#
# n = NoteBook('HP', 1.5, 35000)
# n.print_info()
# n.save_sell_log()
# print()
# n = NoteBook('HP', 1.8, 48500)
# n.save_sell_log()


# Перегрузка операторов
# 24 * 60 * 60 = 86400 - число секунд в одном дне


# class Clock:
#     DAY = 86400
#
#     def __init__(self, sec):
#         if not isinstance(sec, int):
#             raise ValueError('Секунды должны быть целым числом')
#         self.sec = sec % self.DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f'{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}'
#
#     @staticmethod
#     def get_form(x):
#         return str(x) if x > 9 else '0' + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError('Правый операнд должен быть типом Clock')
#         return Clock(self.sec + other.sec)
#
#     def __sub__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError('Правый операнд должен быть типом Clock')
#         return Clock(self.sec - other.sec)
#
#     def __mul__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError('Правый операнд должен быть типом Clock')
#         return Clock(self.sec * other.sec)
#
#     def __floordiv__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError('Правый операнд должен быть типом Clock')
#         return Clock(self.sec // other.sec)
#
#     def __mod__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError('Правый операнд должен быть типом Clock')
#         return Clock(self.sec % other.sec)
#
#     def __eq__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError('Правый операнд должен быть типом Clock')
#         return self.sec == other.sec
#
#     def __ne__(self, other):
#         return not self.__eq__(other)
#
#     def __lt__(self, other):
#         return self.sec < other.sec
#
#     def __le__(self, other):
#         return self.sec <= other.sec
#
#     def __gt__(self, other):
#         return self.sec > other.sec
#
#     def __ge__(self, other):
#         return not self.__lt__(other)
#
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError('Ключ должен быть строкой')
#         hour_, min_, sec_ = self.get_format_time().split(':')
#         time_key = {
#             'hour': hour_,
#             'min': min_,
#             'sec': sec_,
#         }
#         try:
#             return time_key[item]
#         except KeyError:
#             return 'Неверный ключ'
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError('Ключ должен быть строкой')
#
#         if not isinstance(value, int):
#             raise ValueError('Значение должно быть целым числом')
#
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#
#         if key == 'hour':
#             self.sec = s + 60 * m + value * 3600
#         if key == 'min':
#             self.sec = s + 60 * value + h * 3600
#         if key == 'sec':
#             self.sec = value + 60 * m + h * 3600
#
#
# c1 = Clock(10000)
# c2 = Clock(200)
# print(c1.get_format_time())
# print(c1['hour'], c1['min'], c1['sec'])
# c1['hour'] = 11
# c1['min'] = 39
# c1['sec'] = 6
# print(c1['hour'], c1['min'], c1['sec'])
# print(c1.get_format_time())
# sub_c = c1 - c2
# mul_c = c1 * c2
# floordiv_c = c1 // c2
# mod_c = c1 % c2
# print(f'c1: {c1.get_format_time()}')
# print(f'c2: {c2.get_format_time()}')
#
# if c1 > c2:
#     print(f'c1 > c2 {c1 > c2}')
# else:
#     print(f'c1 > c2 {c1 > c2}')
#
# if c1 >= c2:
#     print(f'c1 >= c2 {c1 >= c2}')
# else:
#     print(f'c1 >= c2 {c1 >= c2}')
#
# if c1 < c2:
#     print(f'c1 < c2 {c1 < c2}')
# else:
#     print(f'c1 < c2 {c1 < c2}')
#
# if c1 <= c2:
#     print(f'c1 <= c2 {c1 <= c2}')
# else:
#     print(f'c1 <= c2 {c1 <= c2}')
#
#
# c1 -= c2
# print(f'c1 -= c2: {c1.get_format_time()}')
# c1 *= c2
# print(f'c1 *= c2: {c1.get_format_time()}')
# c1 //= c2
# print(f'c1 //= c2: {c1.get_format_time()}')
# c1 %= c2
# print(f'c1 % c2: {c1.get_format_time()}')
#
# if c1 == c2:
#     print('Время равно')
# else:
#     print('Время разное')
#
# if c1 != c2:
#     print('Время разное')
# else:
#     print('Время равно')
#
# if c1 < c2:
#     print('c1 больше c2')
# else:
#     print('c1 не больше c2')


# class Student:
#     def __init__(self, name, *marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):  # проверяет индекс на отрицание s1[3]
#         if 0 <= item <= len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError('Неверный индекс')
#
#     def __setitem__(self, key, value):  # изменяет s1[2]
#         if not isinstance(key, int) or key < 0:
#             raise TypeError('Индекс должен быть целым положительным числом')
#
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)  # 10 + 1 - 5 = 6
#             self.marks.extend([None] * off)
#
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError('Индекс должен быть целым числом')
#         if key not in range(len(self.marks)):
#             return IndexError('Недопустимый индекс')
#         del self.marks[key]
#
#
# s1 = Student('Сергей', 5.8, 5.6, 3.2, 4.8, 5)
# print(s1.name)
# print(s1.marks)
# print(s1.marks[2])
# print(s1[3])
# s1[17] = 17
# s1[17] = 555
# del s1[20]
# print(s1.marks)

# from random import choice, randint
#
#
# class Cat:
#     def __init__(self, name, age, pol):
#         self.name = name
#         self.age = age
#         self.pol = pol
#
#     def __str__(self):
#         if self.pol == 'M':
#             return f'{self.name} is good boy!!!'
#         elif self.pol == 'F':
#             return f'{self.name} is good girl!!!'
#         else:
#             return f'{self.name} is good Kitty!!!'
#
#     def __repr__(self):
#         return f"Cat(name='{self.name}', age={self.age}, pol='{self.pol}')"
#
#     def __add__(self, other):
#         if self.pol != other.pol:
#             return [Cat('No name', 0, choice(['M', 'F'])) for _ in range(randint(1, 5))]
#         else:
#             raise TypeError('Type are not supports!')
#
#
# cat1 = Cat('Tom', 4, 'M')
# cat2 = Cat('Elsa', 5, 'F')
# cat3 = Cat('Murzik', 3, 'M')
# print(cat1)
# print(cat2)
# print(cat1 + cat2)


# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
#
# s1 = Square(10)
# s2 = Square(20)
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
#
# shape = [r1, r2, s1, s2, t1, t2]
#
# for g in shape:
#     print(g.get_perimetr())


# Функторы

# class Counter:
#     def __init__(self):
#         self.__count = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__count += 1
#         print(self.__count)
#
#
# c1 = Counter()
# c1()
# c1()
# c1()
# print()
# c2 = Counter()
# c2()
# c2()
# c2()
# print()
# c1()
# c1()

# class StripChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, string):
#         if not isinstance(string, str):
#             raise ValueError('Аргумент должен быть строкой')
#         return string.strip(self.__chars)
#
#
# s1 = StripChars('?:!.; ')
# print(s1('Hello World!  '))
#
#
# def strip_chars(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError('Аргумент должен быть строкой')
#         return string.strip(chars)
#
#     return wrap
#
#
# s2 = strip_chars('?:!.; ')
# print(s2('Hello World!  '))


# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self):
#         print('Перед вызовом функции')
#         self.func()
#         print('После вызова функции')
#
#
# @MyDecorator
# def function():
#     print('Текст функции')
#
#
# function()


# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, x, y):
#         # print('Перед вызовом функции')
#         # res = self.func(x, y)
#         # print('После вызова функции')
#         return f'Перед вызовом функции\n {self.func(x, y)}\nПосле вызова функции'
#
#
# @MyDecorator
# def function(a, b):
#     return a * b
#
#
# print(function(2, 5))


# class Power:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, x, y):
#         return f'Результат: {self.func(x, y) ** 2}'
#
#
# @Power
# def fc(a, b):
#     return a * b
#
#
# print(fc(2, 3))


# class MyDecorator:
#     def __init__(self, arg):
#         self.name = arg
#
#     def __call__(self, func):
#         def wrap(*args, **kwargs):
#             return (f'Перед вызовом функции ({self.name})\n {func(*args, **kwargs)}\nПосле вызова '
#                     f'функции')
#
#         return wrap
#
#
# @MyDecorator('два параметра')
# def function(a, b):
#     return a * b
#
#
# @MyDecorator('три параметра')
# def function1(a, b, c):
#     return a * b * c

#
# print(function(2, 5))
#
# print(function1(2, 5, 2))


# class Power:
#     def __init__(self, num):
#         if not isinstance(num, int):
#             raise ValueError('Степень должна быть целым числом')
#         self.num = num
#
#     def __call__(self, f):
#         def wrap(*args, **kwargs):
#             return f'Результат: {f(*args, **kwargs) ** self.num}'
#
#         return wrap
#
#
# @Power(3)
# def func(a, b):
#     return a * b
#
#
# print(func(2, 2))


# Декорирование методов

# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         fn(*args, **kwargs)
#         print("*" * 20)
#
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f'{self.name} {self.surname}')
#
#
# p1 = Person('Виталий', 'Громов')
# p1.info()

# def decorator(arg):
#     class Wrapper(arg):
#         def doubler(self, value):
#             return value * 2
#
#     return Wrapper
#
#
# @decorator
# class ActualClass:
#     def __init__(self, num):
#         print('Инициализатор ActualClass')
#
#     def quad(self, value):
#         return value * 4
#
#
# obj = ActualClass(5)
# print(obj.quad(4))
# print(obj.doubler(4))


# Дескрипторы (__get__, __set__, __delete__, __set_name__)

# class String:
#     def __init__(self, value=None):
#         print(f'Инициализатор String: {value}')
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         if not isinstance(value, str):
#             raise ValueError(f'{value} должно быть строкой')
#         self.__value = value
#
#     def get(self):
#         return self.__value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = String(name)
#         self.surname = String(surname)
#
#     # @property
#     # def name(self):
#     #     return self.__name
#     #
#     # @name.setter
#     # def name(self, value):
#     #     if not isinstance(value, str):
#     #         raise ValueError(f'{value} должно быть строкой')
#     #     else:
#     #         self.__name = value
#     #
#     # @property
#     # def surname(self):
#     #     return self.__surname
#     #
#     # @surname.setter
#     # def surname(self, value):
#     #     if not isinstance(value, str):
#     #         raise ValueError(f'{value} должно быть строкой')
#     #     else:
#     #         self.__surname = value
#
#
# p = Person('Ivan', 'Petrov')
# # p.name = 56
# # print(p.name, p.surname)
# p.surname.set(54)


# class ValidString:
#     def __set_name__(self, person, name):
#         # print(owner)
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         print(instance)
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f'{self.__name} должно быть строкой')
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# p = Person('Ivan', 'Petrov')
# # p.surname = '5'
# print(p.name, p.surname)
# print(p.__dict__)

# class ValidOrd:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, int) or value < 0:
#             raise ValueError(f'{self.__name} должно быть целым положительным числом')
#         instance.__dict__[self.__name] = value
#
#
# class Order:
#     price = ValidOrd()
#     c = ValidOrd()
#
#     def __init__(self, name, price, c):
#         self.name = name
#         self.price = price
#         self.c = c
#
#     def all_c(self):
#         return self.price * self.c
#
#
# o = Order('apple', 5, 10)
# # print(o.__dict__)
# print(f'{o.all_c()}')


# class Integer:
#
#     @staticmethod
#     def verify_coord(coord):
#         if not isinstance(coord, int):
#             raise TypeError(f'Координата {coord} должна быть целым числом')
#
#     def __set_name__(self, owner, name):
#         self.__name = '_' + name
#
#     def __get__(self, instance, owner):
#         # return instance.__dict__[self.__name]
#         return getattr(instance, self.__name)
#
#     def __set__(self, instance, value):
#         self.verify_coord(value)
#         # instance.__dict__[self.__name] = value
#         setattr(instance, self.__name, value)
#
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p1 = Point3D(1, 2, 3)
# p1.x = 20
# print(p1.x)
# print(p1.__dict__)


# Метаклассы


# a = 5
# print(type(a))
# print(type(int))


# class MyList(list):
#     def get_length(self):
#         return len(self)
#
#
# lst = MyList()
# lst.append(5)
# lst.append(8)
# print(lst, lst.get_length())
#
#
# MyList1 = type(
#     'MyList1',
#     (list,),
#     dict(get_length=lambda self: len(self))
# )
#
#
# lst1 = MyList1()
# lst1.append(5)
# lst1.append(8)
# print(lst1, lst1.get_length())
#
# print(MyList.__dict__)
# print(MyList1.__dict__)


# from geometry import rect, sq, trian
#
#
# # import geometry  # работать не будет
# # from geometry import *
#
#
# def run():
#     r1 = rect.Rectangle(1, 2)
#     r2 = rect.Rectangle(3, 4)
#
#     s1 = sq.Square(10)
#     s2 = sq.Square(20)
#
#     t1 = trian.Triangle(1, 2, 3)
#     t2 = trian.Triangle(4, 5, 6)
#
#     shape = [r1, r2, s1, s2, t1, t2]
#
#     for g in shape:
#         print(g.get_perimetr())
#
#
# if __name__ == '__main__':
#     run()


# from car.electrocar import ElectroCar
#
# e_car = ElectroCar('Tesla', 'T', 2018, 99000)
# e_car.show_car()
# e_car.description_battery()


# class PayrollSystem:
#     def calculate(self, employees):
#         print('Расчет заработной платы:')
#         print('=' * 50)
#         for employee in employees:
#             print(f'Заработная плата: {employee.id}, {employee.name}')
#             print(f'- Проверить сумму: {employee.calculate_payroll()}')
#             print()
#         print('=' * 50)
#
#
# class Employee:
#     def __init__(self, id_em, name):
#         self.id = id_em
#         self.name = name
#
#
# class SalaryEmployee(Employee):
#     """Административные работники с фиксированной зп"""
#     def __init__(self, id_em, name, weekly_salary):
#         super().__init__(id_em, name)
#         self.weekly_salary = weekly_salary
#
#     def calculate_payroll(self):
#         return self.weekly_salary
#
#
# class HourlyEmployee(Employee):
#     """Сотрудники с почасовой оплатой"""
#     def __init__(self, id_em, name, hours_worked, hour_rate):
#         super().__init__(id_em, name)
#         self.hours_worked = hours_worked
#         self.hour_rate = hour_rate
#
#     def calculate_payroll(self):
#         return self.hours_worked * self.hour_rate
#
#
# class FixEmployee(SalaryEmployee):
#     """Сотрудники с фиксированной оплатой + комиссия"""
#     def __init__(self, id_em, name, weekly_salary, comm):
#         super().__init__(id_em, name, weekly_salary)
#         self.comm = comm
#
#     def calculate_payroll(self):
#         return self.weekly_salary + self.comm
#
#
# salary_em1 = SalaryEmployee(1, 'Валерий Задорожный', 1500)
# hourly_employee1 = HourlyEmployee(2, 'Илья Кромин', 40, 15)
# fix_em3 = FixEmployee(3, 'Николай Хорольский', 1000, 250)
# payroll_system = PayrollSystem()
# payroll_system.calculate([
#     salary_em1,
#     hourly_employee1,
#     fix_em3
# ])


# Упаковка данных

# сериализация, десериализация
# pickle
# json

# dump() - сохраняет данные в открытый файл
# dumps() - сохраняет данные в строку
# load() - считывает данные из файла
# loads() - считывает данные из строки


# import pickle


# file_name = 'basket.txt'
# shop_list = {
#     'фрукты': ['яблоки', 'манго'],
#     'овощи': ['морковь'],
#     'бюджет': 1000
# }
#
# with open(file_name, 'wb') as fh:
#     pickle.dump(shop_list, fh)
#
# with open(file_name, 'rb') as fh:
#     shop_list_2 = pickle.load(fh)
#
# print(shop_list_2)


# class Test:
#     num = 35
#     str = 'привет'
#     lst = [1, 2, 3, 5]
#     tpl = (22, 23)
#
#     def __str__(self):
#         return f'Число: {Test.num}\nСтрока: {Test.str}\nСписок: {Test.lst}\nКортеж: {Test.tpl}'
#
#
# obj = Test()
# obj1 = pickle.dumps(obj)
# print(f"Сериализация в строку: {obj1}")
#
# obj2 = pickle.loads(obj1)
# print(f"Десериализация из строки:\n{obj2}")


# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = 'test'
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f'{self.a} {self.b} {self.c(5)}'
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# item2 = pickle.dumps(item1)
# item3 = pickle.loads(item2)
# print(item3.__dict__)
# print(item3)


# data = {
#     'name': 'Olga',
#     'age': 35,
#     '20': None,
#     'hobbies': ('running', 'singing'),
#     'children': [
#         {
#             'first_name': 'Alice',
#             'True': 1
#         }
#     ]
# }
#
# # file_name = "data_file.json"
# #
# # with open(file_name, "w") as fw:
# #     json.dump(data, fw, indent=4)
# #
# # with open(file_name, 'r') as fw:
# #     data1 = json.load(fw)
# #
# # print(data1)
#
# json_string = json.dumps(data, sort_keys=True)
# print(json_string)
# print(type(json_string))
# data1 = json.loads(json_string)
#
# print(data1['hobbies'])
# print(type(data1))


#
# x = {
#     'name': 'Виктор'
# }
# print(json.dumps(x))
# print(json.loads(json.dumps(x)))
# print(json.dumps(x, ensure_ascii=False))





# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         a = ', '.join(map(str, self.marks))
#         return f'Группа: {self.name}: {a}'
#
#
# st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
# print(st1)


import json
from random import choice


def gen_person():

    name = ''
    tel = ''

    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'e']
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letter)

    while len(tel) != 10:
        tel += choice(num)

    person = {
        'name': name,
        'tel': tel
    }
    return person


def write_json(person_dict):
    idd = ''
    d_num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    while len(idd) != 11:
        idd += choice(d_num)

    try:
        data = json.load(open('person.json'))
    except FileNotFoundError:
        data = {}

    d = person_dict
    data[idd] = d
    with open('person.json', 'w') as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(gen_person())

# main_dict = {}
#
# dict1 = {'key1': 'value1', 'key2': 'value2'}
# dict2 = {'key3': 'value3', 'key4': 'value4'}
#
# main_dict['dict1'] = dict1
# main_dict['dict2'] = dict2
#
# print(main_dict)