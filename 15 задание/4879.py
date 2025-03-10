for x in range(10000):
    a = 0
    p = x in [1,2,4,8]
    q = x in [1,2,3,4,5,6]
    f = (not a) <= (not(p or q))
    if f == 0:
        print(x)