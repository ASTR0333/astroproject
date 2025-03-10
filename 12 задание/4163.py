ans=[]
for p1 in range(1,300):
    for p2 in range(1, 300):
        s = p1*'1' + p2*'3'
        s1 = s
        while '12' in s or '13' in s:
            s = s.replace('12','21',1)
            s = s.replace('31', '23', 1)
            s = s.replace('13', '23', 1)
        if s.count('1') == 0 and s.count('2')*2 + s.count('3')*3 == 404:
            ans.append(len(s1))

print(max(ans))




