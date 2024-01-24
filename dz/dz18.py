main_str = input('Введите строку: ')
# main_str = 'I am learning Python. hello, WORLD!'
# print(main_str)
st1 = main_str.find('h')
st2 = main_str.rfind('h')
change_str = main_str[st1 + 1:st2 + 1]

print(main_str[:st1] + change_str[::-1] + main_str[st2:])
