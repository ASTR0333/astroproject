k = 0
for p1 in 'СЛОН':
    for p2 in 'СЛОН':
        for p3 in 'СЛОН':
            for p4 in 'СЛОН':
                for p5 in 'СЛОН':
                    s = p1+p2+p3+p4+p5
                    if s.count('С') == 1:
                        k+=1
print(k)

