def check(a):
    for x in range(-100,100):
        for y in range(-100,100):
            f = ((a<x) or (x**2-7*x + 10>0))  and ((a>=y) or (y**2 + 7*y + 12 >0))
            if f == 0:
                return 0
    return 1

for a in range(-100,100):
    if check(a) == 1:
        print(a)

