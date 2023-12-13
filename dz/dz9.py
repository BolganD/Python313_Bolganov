from random import randint


def numbers():
    t1 = tuple(randint(0, 5) for i in range(10))
    t2 = tuple(randint(-5, 0) for i in range(10))
    t3 = t1 + t2
    t4 = t3.count(0)
    return t1, t2, t3, t4


ts_1, ts_2, all_t, nul = numbers()
print(ts_1)
print(ts_2)
print(all_t)
print('0 =', nul)





