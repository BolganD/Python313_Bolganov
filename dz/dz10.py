m = input("Введите по порядку, без пробелов, элементы кортежа: ")
tpl_m = tuple(m)
t = []
print(tpl_m)
tpl_m = list(tpl_m)
for i in tpl_m:
    ct = tpl_m.count(i)
    if i not in t:
        print("Количество", i, "=", ct)
        t.append(i)




