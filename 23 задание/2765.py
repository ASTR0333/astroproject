def f(x,end,k):
    if x > end:
        return 0
    if x == end and k == 7:
        return 1
    if k > 7:
        return 0
    return f(x+1,end,k+1) + f(x+3,end,k+1) + f(2*x,end,k+1)

print(f(2,25,0))

