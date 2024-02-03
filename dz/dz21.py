def nums(num):
    if not num:
        return 0
    else:
        count = nums(num[1:])
        if num[0] < 0:
            count += 1
        return count


o_n = [-2, 3, 8, -11, -4, 6]
print(nums(o_n))
