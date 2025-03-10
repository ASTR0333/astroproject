def f(x,end):
    if x > 21:
        return 0
    if x == 21:
        return 1
    if x == 10:
        return 0
    return f(x+1,end)+f(2*x,end)
print(f(1,21))


