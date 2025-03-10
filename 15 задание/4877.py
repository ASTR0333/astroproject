for x in [0.25*k for k in range(10**6)]:
    a = 1
    p = 44 <= x <= 49
    q = 28 <= x <= 53
    f = (a <= p) or q
    if f == 1:
        print(x)