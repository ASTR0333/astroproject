for x in [0.25*k for k in range(10**6)]:
    a = 0
    p = 1381 <= x <= 2165
    q = 369 <= x <= 3894
    r = 2643 <= x <= 3155
    f = (not(q<=(p or r))) <= ((not a) <= (not q))
    if f == 0:
        print(x)
print(3894-369)

