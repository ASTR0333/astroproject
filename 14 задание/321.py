for n in range(2,50):
    c = 30
    s = ''
    while c!=0:
        last = c%n
        c = c//n
        s = str(last) + s
    if s[-1] == '0' and len(s) == 4:
        print(n)






