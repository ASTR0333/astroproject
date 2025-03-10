from functools import lru_cache


@lru_cache(None)

def f(x,end):
    if x > end:
        return 0
    if x == end and x%2!=0:
        return 1
    return f(x+2,end) + f(x*2,end) + f(x*3,end)

print()
