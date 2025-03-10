for n in range(2,50):
    c = 71
    s = ''
    while c!=0:
        last = c%n
        c = c // n
        s = str(last) + s
    if s[-2:] == '13':
        print(n)