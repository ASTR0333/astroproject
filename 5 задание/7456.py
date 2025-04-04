for n in range(1,1000):
    n_2 = bin(n)[2:]
    if n_2.count('1') % 2 == 0:
        n_2 = n_2 + '0'
        n_2 = '10' + n_2[2:]
    else:
        n_2 = n_2 + '1'
        n_2 = '11' + n_2[2:]
    r = int(n_2, 2)
    if r>50:
        print(n,r)
