n = 0
for p1 in 'КОСУФ':
    for p2 in 'КОСУФ':
        for p3 in 'КОСУФ':
            for p4 in 'КОСУФ':
                for p5 in 'КОСУФ':
                    s = p1 + p2 + p3 + p4 + p5
                    n +=1
                    if s.count('Ф') == 0 and s.count('У') == 2:
                        print(n, s)