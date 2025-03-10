from functools import lru_cache


@lru_cache(None)
def f(x,end,k):
    if x > end:
        return 0
    if k > 5:
        return 0
    if x == end and k == 5:
        return 1

    return f(x+1,end,k+1) + f(x+2,end,k+1) + f(x*2,end,k+1)

print(f(1,28,0))