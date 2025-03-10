def check(a):
    for x in range(1,500):
        for y in range(1, 500):
            f = (x+y<=30) or (y<=x+2) or (y>=a)
            if f == 0:
                return 0
    return 1

for a in range(0,500):
    if check(a)==1:
        print(a)

