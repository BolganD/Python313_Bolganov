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
#


ch_1 = int(input('Введите номер первой строки(от 0 до 2) -> '))
ch_2 = int(input('Введите номер второй строки(от 0 до 2) -> '))

pos = open('one.txt', 'r', encoding='utf-8')
list_one = pos.readlines()
change_line = list_one[ch_1]
list_one[ch_1] = list_one[ch_2]
list_one[ch_2] = change_line
print(list_one)
pos.close()

pos = open('one.txt', 'w', encoding='utf-8')
pos.writelines(list_one)
pos.close()
