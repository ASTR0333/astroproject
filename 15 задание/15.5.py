for x in [k*0.25 for k in range(0,10**6)]:
    a = 0
    d = 17 <= x<= 58
    c = 29 <= x <= 80
    f = d <= (((not c) and (not a)) <= (not d))
    if f == 0:
        print(x)
