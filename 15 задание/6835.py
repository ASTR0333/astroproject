for x in [0.25*k for k in range(10**6)]:
    a = 1
    p = 13 <= x <= 19
    q = 17 <= x <= 23
    f = not((not p) <= q) <= (a <= (not q) <= p)
    if f == 1:
        print(x)