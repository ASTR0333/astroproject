def f(x,end,flag):
    if x == 14:
        flag = 1
    if x > end:
        return 0
    if x == end and flag == 1:
        return 1
    if x == 25:
        return 0

    return f(x+1,end,flag) + f(2*x,end,flag)


print(f(2,29,0))