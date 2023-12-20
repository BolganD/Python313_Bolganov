alpha = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'я', 'э', 'ю'}
words = input("Введите строку: ")
s = 0
for i in words:
    if i in alpha:
        s += 1

print(s)
