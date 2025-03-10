for n in range(2,50):
    c = 30
    s = ''
    while c!=0:
        last = c%n
        c = c // n
        s = str(last) + s
    if len(s)==3:
        print(n)