def f(x,end,f8,f10):
    if x == 8:
        f8 = 1
    if x == 10:
        f10 = 1
    if x > end:
        return 0
    if x == end and f8 and f10:
        return 1
    return f(x+2,end,f8,f10) + f(x*2,end,f8,f10) + f(x-1,end,f8,f10)
print(f(32,17,0,0))