ans = 0
for p1 in 'PIR':
    for p2 in 'PIR':
        for p3 in 'PIR':
            for p4 in 'PIR':
                for p5 in 'PIR':
                    s = p1+p2+p3+p4+p5
                    if s.count('P') == 1:
                        ans+=1
                        print(s)
print(ans)
