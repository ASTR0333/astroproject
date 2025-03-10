def n6(n):
    while n!=0:
        if n % 10 == 6:
            return 1
        n //= 10
    return 0
def f(x,end):
    if n6(x):
        return 0
    if x > end:
        return 0
    if x == end:
        return 1
    return f(x+1,end) + f(x+3,end)

print(f(1,45))