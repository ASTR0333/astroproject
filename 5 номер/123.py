for n in range(1,10000):
    n2 = bin(n)[2:]
    if n%2 != 0:
        n2 = '10' + n2 + '11'
    else:
        n2 = '1' + n2 + '00'
    r = int(n2,2)
    if r > 1023:
        print(r)



