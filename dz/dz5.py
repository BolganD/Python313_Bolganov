# Задача 1


# n = [int(input('-> ')) for _ in range(int(input('n = ')))]
# s = k = 0
# for i in range(len(n)):
#     if n[i] != 0:
#         k += 1
#     s += n[i]
# print(s / k)


# Задача 2


n = [int(input('-> ')) for _ in range(int(input('n = ')))]
for i in range(len(n)):
    if i % 2 == 0:
        print(n[i], end=" ")
