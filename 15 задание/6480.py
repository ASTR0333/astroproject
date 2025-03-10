for x in [0.25*k for k in range(10**6)]:
    a = 0
    p = 10 <= x <= 21
    q = 13 <= x <= 38
    r = 18 <= x <= 25
    f = (not(q<=(p or r))) <= ((not a) <= (not q))
    if f == 0:
        print(x)

