def check(a):
    for x in range(1000):
        for y in range(1000):
            f = ((2*x+y!=70) or (x < y) or (a<x))
            if f == 0:
                return 0
    return 1
for a in range(1,1000):
    if check(a):
        print(a)
