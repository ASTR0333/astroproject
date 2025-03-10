def f(x, end, flag):
    if x == 6:
        flag = 1
    if x > end:
        return 0
    if x == end and flag == 1:
        return 1
    if x == 8:
        return 0
    return f(x + 1, end,flag) + f(x + 4, end,flag) + f(4 * x, end,flag)


print(f(2,24,0))
