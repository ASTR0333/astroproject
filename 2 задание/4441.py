print('a b c d')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                f = ((not a) <= b) and (b == (not c)) and (not d)
                if f == 1:
                    print(a,b,c,d)
#bacd