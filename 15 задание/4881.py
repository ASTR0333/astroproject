for x in range(10000):
    a = 0
    p = x in [1,12]
    q = x in [12,13,14,15,16]
    f = (not a) <= ((not p) and (not q))
    if f == 0:
        print(x)
