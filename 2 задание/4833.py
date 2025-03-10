print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((z <= y) and ((not x) <= w)) <= ((z == w) or (y and (not x)))
                if f == 0:
                    print(x,y,z,w)
#yzwx