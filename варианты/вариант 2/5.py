for n in range(1,10000):
    n2 = bin(n)[2:]
    n2 = n2[:-1]
    if n%2!=0:
        n2 = n2 + '10'
    else:
        n2 = n2 + '01'
    r = int(n2,2)
    if r == 2018:
        print(n)