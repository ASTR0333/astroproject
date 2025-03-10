def f(x,end,f25,f45):
    if x == 25:
        f25 = 1
    if x == 45:
        f45 = 1
    if x > end:
        return 0
    if x == 17 or x == 32 or x == 50:
        return 0
    if x == end and f25 and f45:
        return 1
    return f(x+1,end,f25,f45) + f(x+5,end,f25,f45) + f(x**2,end,f25,f45)

print(f(5,60,0,0))
        