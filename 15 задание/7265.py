def check(a):
    for x in range(0,1000):
        for y in range(0, 1000):
            f = (3*x + 2*y > 25) or (x > 2*y) or (x+4*y<a)
            if f == 0:
                return 1
    return 0

for a in range(0,1000):
    if check(a) == 1:
        print(a)