ans = 0
for p1 in 'АСПЕКТ':
    for p2 in 'АСПЕКТ':
        for p3 in 'АСПЕКТ':
            for p4 in 'АСПЕКТ':
                for p5 in 'АСПЕКТ':
                    for p6 in 'АСПЕКТ':
                        s = p1 + p2 + p3 + p4 + p5 + p6
                        if s.count('А') == 1 and s.count('С') == 1 and s.count('П') == 1 and s.count('Е') == 1 and s.count('К') == 1 and s.count('Т') == 1:
                            if 'АЕ' not in s and 'ЕА' not in s:
                                ans+=1
print(ans)
