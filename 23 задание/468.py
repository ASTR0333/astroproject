def f(x,end):
    if x > end:
        return 0
    if x == end:
        return 1
    return f(x+1,end)+f(2*x,end)

print(f(3,9)+f(3,18))