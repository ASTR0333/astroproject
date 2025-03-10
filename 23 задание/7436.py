def f(x,end):
    if x == 13:
        return 0
    if x > end:
        return 0
    if x == end:
        return 1
    return f(x+2,end) + f(x*3,end) + f(x**2,end)




print(f(3,49))