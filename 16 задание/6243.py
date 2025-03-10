from functools import lru_cache


@lru_cache

def f(n):
    if n <= 2:
        return n
    return n+f(n-2)

for i in range(1,2024):
    f(i)

print(f(2023)+f(2020))