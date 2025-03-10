for x in range(10000):
    a = 0
    p = x in [3,6,9,12]
    q = x in [1,2,3,4,5,6]
    f = not((not a) and p) or (not q)
    if f == 0:
        print(x)
