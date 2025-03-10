ans = []
def st(num):
    i = 0
    while 2**i<num:
        i+=1
    if 2**i == num:
        return 1
    else:
        return 0
for n1 in range(1,100):
    for n2 in range(1, 100):
        s = '0' + '2' * n2 + '1' * n1
        if len(s)>=75:
            s1  = s
            while '01' in s or '02' in s:
                s = s.replace('02','1110',1)
                s = s.replace('01', '220',1)
            summ1 = s.count('1') + s.count('2') * 2
            summ2 = s1.count('1') + s1.count('2') * 2
            if st(summ1) == 1:
                ans.append(summ2)

print(min(ans))


