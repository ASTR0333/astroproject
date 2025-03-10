for x in range(1,1000):
    a = 0
    p = x in range(1,7,1)
    q = x in [3,5,15]
    f = (not a) <= (((not p) and q) or (not q))
    if f == 0:
        print(x)