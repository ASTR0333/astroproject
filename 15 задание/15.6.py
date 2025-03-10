for x in [0.25*k for k in range(10**6)]:
    a = 1
    p = 9 <= x <= 19
    q = 24 <= x <= 54
    f = a <= (p or q)
    if f == 1:
        print(x)
