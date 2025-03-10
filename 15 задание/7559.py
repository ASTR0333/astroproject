def check(a):
    for x in range(1, 1000):
        f = (x%33 == 0) <= ((not x%a==0) <= (not x%242==0))
        if f == 0:
            return 0
    return 1


for a in range(1,10000):
    if check(a) == 1:
        print(a)
