print('a b c d f')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                f = b <= (a and c or d and (not a))
                if f == 0:
                    print(a,b,c,d,f)