for x in [0.25*k for k in range(10**6)]:
    a = 1
    p = 5<= x <= 30
    q = 14 <= x <=23
    f = (p == q) <= (not a)
    if f == 1:
        print(x)



