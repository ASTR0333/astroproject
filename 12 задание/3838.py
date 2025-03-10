def alg(s):
    while '01' in s or '02' in s or '03' in s:
        s = s.replace('01', '2302',1)
        s = s.replace('02', '10', 1)
        s = s.replace('03', '201', 1)
    return s
for p1 in range(1,100):
    for p2 in range(1, 100):
        for p3 in range(1, 100):
            s  =  '0' + p1 * '1' + p2*'2' + p3*'3'
            s1 = alg(s)
            if s1.count('1') == 51 and s1.count('2') == 29 and s1.count('3') == 23:
                print(p3)

