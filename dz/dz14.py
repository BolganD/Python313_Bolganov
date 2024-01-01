s = []
for i in range(int(input('Количество студентов: '))):
    name = input(str(i + 1) + '-й студент: ')
    score = int(input("Балл: "))
    s.append([name, score])
middle_score = sum([x[1] for x in s]) / len(s)
print('Средний балл: ', round(middle_score), '. Студенты с баллом выше среднего:', sep='')
for name, score in s:
    if score > middle_score:
        print(name)

