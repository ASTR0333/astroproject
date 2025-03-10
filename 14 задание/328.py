for n in range(2,50):
    c = 67
    s = ''
    while c!=0:
        last = c%n
        c = c // n
        s = str(last) + s
    if len(s)==4 and s[-1] == '1':
        print(n)