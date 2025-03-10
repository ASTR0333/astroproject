from functools import lru_cache


@lru_cache(None)
def f(x,end,k):
    if x > end:
        return 0
    if k > 6:
        return 0
    if x == end and k == 6:
        return 1

    return f(x+1,end,k+1) + f(x+5,end,k+1) + f(x*3,end,k+1)

print(f(1,111,0))