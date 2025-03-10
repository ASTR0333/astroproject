
for p1 in range(1,1000):
    k = 0
    s = p1*'3'
    while '3333' in s or '222' in s:
        if '3333' in s:
            s = s.replace('3333','2',1)
            s = s.replace('222', '3',1)
            k+=1
        else:
            s = s.replace('222','3',1)
            k+=1
    if s == '22':
        print(p1,k)