for n in range(2,50):
    c = 94
    s = ''
    while c!=0:
        last = c%n
        c = c // n
        s = str(last) + s
    if s[0:2] == '23':
        print(n)