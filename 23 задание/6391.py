def pr(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

def f(x,end,flag):
    if x == 16:
        flag = 1
    if pr(x):
        return 0
    if x > end:
        return 0
    if x == end and flag:
        return 1
    return f(x+1,end,flag) + f(x+2,end,flag) + f(x*3,end,flag)

print(f(8,32,0))