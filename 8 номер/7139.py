ans = 0
for p1 in '123456789AB':
    for p2 in '0123456789AB':
        for p3 in '0123456789AB':
            s = p1 + p2 + p3
            if s.count('2')==1 and s[-1]!='2':
                q = s[s.find('2')+1:]
                if '0' not in q and '2' not in q and '4' not in q and '6' not in q  and '8' not in q and 'A' not in q:
                    ans+=1
print(ans)



