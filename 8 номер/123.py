k = 0
for p1 in 'ВЕНТИЛЬ':
    for p2 in 'ВЕНТИЛЬ':
        for p3 in 'ВЕНТИЛЬ':
            for p4 in 'ВЕНТИЛЬ':
                for p5 in 'ВЕНТИЛЬ':
                    for p6 in 'ВЕНТИЛЬ':
                        for p7 in 'ВЕНТИЛЬ':
                            s = p1+p2+p3+p4+p5+p6+p7
                            if s.count('В') == 1 and s.count('Е') == 1 and s.count('Н') == 1 and s.count('Т') == 1 and s.count('И') == 1 and s.count('Л') == 1 and s.count('Ь') == 1 and s[-1] != 'Ь' and 'ЕЬИ' not in s and 'ИЬЕ' not in s:
                                print(s)
print(k)
