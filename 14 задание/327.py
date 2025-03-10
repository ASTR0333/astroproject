for n in range(2,50):
    c = 381
    s = ''
    while c!=0:
        last = c%n
        c = c // n
        s = str(last) + s
    if len(s)==3 and s[-1] == '3':
        print(n)