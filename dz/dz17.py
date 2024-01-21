def ascii_nums(a, b):
    if a < b:
        all_num_v_a = [chr(z) for z in range(a, b + 1)]
        return all_num_v_a
    elif a > b:
        all_num_v_b = [chr(z) for z in range(b, a + 1)]
        return all_num_v_b


x = int(input('Введите первое число -> '))
y = int(input('Введите второе число -> '))

print(ascii_nums(x, y))
