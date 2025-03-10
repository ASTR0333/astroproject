print('a b c')
for a in range(2):
    for b in range(2):
        for c in range(2):
            f = a == ((b or b) <= c)
            if f == 1:
                print(a,b,c)

#bca