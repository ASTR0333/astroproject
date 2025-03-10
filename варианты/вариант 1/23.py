def f(x,end,flag):
    if x > end:
        return 0
    if x == 10:
        flag = 1
    if x == 17:
        return 0
    if x == end and flag:
        return 1
    return f(x+1,end,flag) + f(x*2,end,flag)

print(f(1,21,0))

