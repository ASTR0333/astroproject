def to5(s):
    q = ''
    while s>0:
        last = s%5
        q = str(last)+q
        s = s // 5
    return q
for x in range(0,10000):
    s = to5(125**7 - 25**4 + x)
    if s.count('4')==15 and s.count('3')==1 and s.count('1')==2:
        print(x)