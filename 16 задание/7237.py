from functools import lru_cache


@lru_cache

def f(n):
    if n >= 1900:
        return n
    elif n%3!=0:
        return n*f(n+1)
    else:
        return n * f(n+2) // 3

for i in range(1900,1,-1):
    f(i)

print(f(1875)//f(1880))