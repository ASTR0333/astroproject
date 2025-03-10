for x in [0.25*k for k in range(10**6)]:
    a = 1
    p = 15 <= x <= 39
    q = 44 <= x <= 57
    f = (a <= p) or q
    if f == 1:
        print(x)