for x in [0.25*k for k in range(10**6)]:
    a = 0
    p = 1023 <= x <= 2148
    q = 1362 <= x <= 3898
    r = 1813 <= x <= 2566
    f = (not(q<=(p or r))) <= ((not a) <= (not q))
    if f == 0:
        print(x)

