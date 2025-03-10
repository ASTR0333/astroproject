from functools import lru_cache


@lru_cache

def f(n):
    if n >= 2022:
        return n
    return f(n+5) + 7

for i in range(2022,1,-1):
    f(i)

print(f(45)-f(49))