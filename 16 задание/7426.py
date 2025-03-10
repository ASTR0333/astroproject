from functools import lru_cache


@lru_cache

def f(n):
    if n < 7:
        return 7
    elif n%3!=0:
        return 5 - f(n-1)
    else:
        return 3 + f(n-1)

for i in range(7,3016):
    f(i)

print(f(3015))