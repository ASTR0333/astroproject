def to7(x):
    q = ''
    while x>0:
        last = x%7
        x = x//7
        q = str(last) + q
    return q
for x in range(0,2031):
    s = 7**170 + 7**100 - x
    if to7(s).count('0')==71:
        print(x,s)
