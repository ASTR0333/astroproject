from functools import lru_cache


@lru_cache

def f(n):
    if n >= 10000:
        return 1
    elif n%2==0:
        return f(n+3) + 7
    else:
        return f(n+1) - 3

for i in range(10000,1,-1):
    f(i)

print(f(50)-f(57))