print('x y z w')
for z in range(2):
    for y in range(2):
        for x in range(2):
            for w in range(2):
                f = ((not x ) <= y) and ((not y) == z) and w
                if f == 1:
                    print(z,y,x,w)