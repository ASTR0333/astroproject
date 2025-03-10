def to4(s):
    q = ''
    while s>0:
        last = s%4
        q = str(last)+q
        s = s // 4
    return q
for x in range(0,10000):
    s = to4(64**11 - 4**10 + 96 - x)
    if s.count('1')+s.count('2')*2 + s.count('3')*3 == 71:
        print(x)