k = 0
for p1 in 'ГАЛКТИ':
    for p2 in 'ГАЛКТИ':
        for p3 in 'ГАЛКТИ':
            for p4 in 'ГАЛКТИ':
                for p5 in 'ГАЛКТИ':
                    for p6 in 'ГАЛКТИ':
                        for p7 in 'ГАЛКТИ':
                            for p8 in 'ГАЛКТИ':
                                s = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8
                                if s[0] in "ГКЛТ" and s[7] in "АИ"  and s.count("КЛ")==0 :
                                    k+=1
print(k)
