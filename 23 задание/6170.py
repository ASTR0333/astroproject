from functools import lru_cache


@lru_cache(None)
def summa(n):
    s= 0
    while n!=0:
        s = s + n%10
        n //= 10
    return s

def f(x,end,k):
    k = k - summa(x)
    if x > end:
        return 0
    if k<0:
        return 0
    if x == end:
        return 1
    return f(x+3,end,k) + f(x*4,end,k) + f(x*5,end,k)


print(f(1,5500,1000))