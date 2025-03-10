for x in [0.25*k for k in range(10**6)]:
    a = 0
    p = 106 <= x <= 218
    q = 132 <= x <= 388
    r = 183 <= x <= 256
    f = (not(q<=(p or r))) <= ((not a) <= (not q))
    if f == 0:
        print(x)

