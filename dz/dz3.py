s = int(input("Введите кол-во символов: "))
t = input("Введите тип символа: ")
ol = int(input("Введите ориентацию символов (1 - вертикальная, 0 - горизонтальная): "))
i = 0
while i <= s:
    if ol == 0:
        print(t, end=" ")
    else:
        print(t)
    i += 1
