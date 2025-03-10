for n in range(1,10000):
    n2 = bin(n)[2:]
    if n%2!=0:
        n2 = n2.replace('1','*')
        n2 = n2.replace('0','1')
        n2 = n2.replace('*','0')
        if n2.count('1') > 0:
            n2 = n2[n2.index('1'):]
        else:
            n2 = '0'
    n2 = (n2.count('1')*'1')*2 + (n2.count('0')*'0')*2
    r = int(n2,2)
    if r > 60:
        print(n)

