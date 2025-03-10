for x in range(10000):
    a = 1
    p = x in [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    q = x in [ 3, 6, 9, 12, 15, 18, 21, 24, 27, 30 ]
    f = (a <= (not p)) and ((not q) <= (not a))
    if f == 1:
        print(x)