for x in [0.25*k for k in range(10**6)]:
    a = 0
    p = 135 <= x <= 211
    q = 234 <= x <= 356
    r = 288 <= x <= 384
    f = (not(q <= (p or r))) <= ((not a) <= (not q))
    if f == 0:
        print(x)
print(288-234)