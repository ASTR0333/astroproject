ans = []
for n1 in range(1,100):
    for n2 in range(1, 100):
        s = '0' + '1' * n1 + '2' * n2
        if len(s) >= 95:
            s1 = s
            while '01' in s or '02' in s:
                s = s.replace('02','1110',1)
                s = s.replace('01', '2210', 1)
            summ1 = s.count('1') + s.count('2') * 2
            summ2 = s1.count('1') + s1.count('2') * 2
            if str(summ1) == str(summ1)[::-1]:
                ans.append(summ2)
print(min(ans))





