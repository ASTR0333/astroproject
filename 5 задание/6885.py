def to15(n):
    s = ''
    while n!=0:
        last = n%15
        n = n//15
        if last<10:
            s = str(last) + s
        elif last == 10:
            s = 'a' + s
        elif last == 11:
            s = 'b' + s
        elif last == 12:
            s = 'c' + s
        elif last == 13:
            s = 'd' + s
        elif last == 14:
            s = 'e' + s
    return s
print(to15(40))