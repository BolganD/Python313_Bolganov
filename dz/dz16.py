def dec(args1, args2):
    def arg_dec(fn):
        def wrap(v, x, y, z):
            len_nums = len(fn(v, x, y, z))
            # summa_sah = (v + x + y + z) / len_nums
            print(args1, v, ', ', x, ', ', y, ', ', z, args2, (v + x + y + z) / len_nums, sep='')
        return wrap
    return arg_dec


def summa(a, b, c, d):
    s = a + b + c + d
    print('Сумма чисел ', a, ', ', b, ', ', c, ', ', d, ' = ', s, sep='')


@dec('Среднее арифметическое чисел ', ' = ')
def sub(a, b, c, d):
    return a, b, c, d


summa(2, 3, 3, 4)
sub(2, 3, 3, 4)
