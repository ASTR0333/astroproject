for x in range(10000):
    a = 1
    p = x in [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    q = x in [ 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    f = (a <= p) and (q <= (not a))
    if f == 1:
        print(x)