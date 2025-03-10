for x in range(10000):
    a = 0
    p = x in [1,2,3,4]
    q = x in [1,2,3,4,5,6]
    f = (not a) <= ((not p) or (not q))
    if f == 0:
        print(x)
