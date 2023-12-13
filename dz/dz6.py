a = [5, 4, 2, 3, 4, 6, 7, 5, 2, 1]
m = []
n = []
for el in a:
    if el not in m:
        m.append(el)
        n.append(el)
    else:
        if el in n:
            i = n.index(el)
            n.pop(i)
print(n)
