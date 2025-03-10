for x in [0.25*k for k in range(10**6)]:
    a = 0
    p = 131 <= x <= 215
    q = 36 <= x <= 384
    r = 243 <= x <= 355
    f = (not(q<=(p or r))) <= ((not a) <= (not q))
    if f == 0:
        print(x)
print(384-36)

