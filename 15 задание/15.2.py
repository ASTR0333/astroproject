for x in range(1,1000):
    a = 0
    p = x in range(2,21,2)
    q = x in range(3,31,3)
    f = (p <= a) or ((not a) <= (not q))
    if f == 0:
        print(x)