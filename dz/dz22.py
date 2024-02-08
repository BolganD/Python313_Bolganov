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