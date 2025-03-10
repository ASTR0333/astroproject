for x in range(1,1000):
    a = 1
    p = x in range(2,21,2)
    q = x in range(5,51,5)
    f = (a <= p) and (q <= (not a))
    if f == 1:
        print(x)