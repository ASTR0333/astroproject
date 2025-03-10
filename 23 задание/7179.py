from functools import lru_cache


@lru_cache(None)
def f(x,end,f1,f2):
    if x % 3 == 0:
        f1 +=1
    if x % 5 == 0:
        f2 +=1
    if x > end:
        return 0
    if x == end and f1 == f2:
        return 1
    return f(x+1,end,f1,f2) + f(x+4,end,f1,f2) + f(x*3,end,f1,f2)

print(f(1,180,0,0))


