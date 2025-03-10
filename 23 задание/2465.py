def f(x,end,f9,f12):
    if x == 9:
        f9 = 1
    if x == 12:
        f12 = 1
    if x > end:
        return 0
    if x == end and f9+f12==2:
        return 1
    return f(x+1,end,f9,f12) + f(x+3,end,f9,f12) + f(2*x,end,f9,f12)

print(f(3,20,0,0))


