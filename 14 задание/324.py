for n in range(2,50):
    c = 86
    s = ''
    while c!=0:
        last = c%n
        c = c // n
        s = str(last) + s
    if s[-2:] == '22':
        print(n)