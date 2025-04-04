
for n in range(64,100):
    n2 = bin(n)[2:]
    if n2.count('1')%2==0:
        x = n2[-4:]
        x = x.replace('0','*')
        x = x.replace('1', '0')
        x = x.replace('*', '1')
        n2 = n2[:-4] + x
    else:
        y = n2[-5:-1]
        y = y.replace('0', '*')
        y = y.replace('1', '0')
        y = y.replace('*', '1')
        n2 = n2[:-5] + y + n2[-1]
    r = int(n2,2)
    print(n,r)




