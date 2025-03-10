def alg(s):
    while '01' in s or '02' in s or '03' in s:
        s = s.replace('01','2302',1)
        s = s.replace('02', '10', 1)
        s = s.replace('03', '201', 1)
    return s


for n1 in range(1,60):
    for n2 in range(1, 60):
        for n3 in range(1, 60):
            s = '0' + n1*'1' + n2 * '2' + n3 * '3'
            s1 = alg(s)
            if s1.count('1') == 60 and s1.count('2') == 22 and s1.count('3') == 17:
                print(n1)


