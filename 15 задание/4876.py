for x in [0.25*k for k in range(10**6)]:
    a = 1
    p = 43 <= x <= 49
    q = 44 <= x <= 53
    f = (a <= p) or q
    if f == 1:
        print(x)