def f(x,end,flag):
    if x == 39:
        flag = 1
    if x < end:
        return 0
    if x == 32:
        return 0
    if x == end and flag:
        return 1
    return f(x-1,end,flag) + f(x-5,end,flag) + f(x//4,end,flag)

print(f(43,17,0))