from functools import lru_cache


@lru_cache

def f(n):
    if n == 1:
        return 6
    return 3*n + 2 + f(n-1)

for i in range(1,2025):
    f(i)

print(f(2024)-f(2020))