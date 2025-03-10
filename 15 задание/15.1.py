def check(a1,a2):
    for x in range(1,500):
        d = 17<=x<=58
        c = 29<=x<=80
        a = a1<=x<=a2
        f = d <= (((not c) and (not a)) <= (not d))
        if f == 0:
            return 0

    return 1



for a1 in range(1,100):
    for a2 in range(a1, 100):
        if check(a1,a2) == 1:
            print(a1,a2)
            break


