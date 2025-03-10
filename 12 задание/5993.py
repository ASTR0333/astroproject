ans=[]
for n in range(1,50):
    k = 0
    s = '>2' + '12' * n + '<'
    while '>2<' not in s:
        k+=1
        s = s.replace('>1','>2',1)
        s = s.replace('12<', '1<2', 1)
        s = s.replace('>21', '1>', 1)
        s = s.replace('1<', '<2', 1)
        if k>1000:
            break
    if s.count('1')+s.count('2')*2>103:
        ans.append(n)
print(min(ans))