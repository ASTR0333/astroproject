for i in range(1,10000):
    n = i
    if n % 2 == 0:
        n = n / 2
    else:
        n = n-1

    if n % 6 == 0:
        n = n / 6
    else:
        n = n-1

    if n % 15 == 0:
        n = n / 15
    else:
        n = n-1

    r = n
    if 'c' in hex(i)[2:] and r == 523:
        print(i)

