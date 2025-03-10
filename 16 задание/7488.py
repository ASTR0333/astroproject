from functools import lru_cache

@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    return 3*n*f(n-1)

for i in range(1,10**4):
    f(i)
print((f(2024)//6+f(2023))/f(2022))
