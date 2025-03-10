from functools import lru_cache

@lru_cache(None)
def f(x,end):
    if x > end:
        return 10**20
    if x == end:
        return 0
    return min(f(x+1,end),f(x+5,end),f(x*3,end))+1

print(f(1,227))