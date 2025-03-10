def f(x,end,flag):
    if x == 16:
        flag = 1
    if x < end:
        return 0
    if x == end and flag == 1:
        return 1
    return f(x-2,end,flag) + f(x//2,end,flag)

print(f(38,2,0))