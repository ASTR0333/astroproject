ans = 0
for p1 in 'ВУАЛЬ':
    for p2 in 'ВУАЛЬ':
        for p3 in 'ВУАЛЬ':
            for p4 in 'ВУАЛЬ':
                for p5 in 'ВУАЛЬ':
                    s = p1 + p2 + p3 + p4 + p5
                    if s.count('В') == 1 and s.count('У') == 1 and s.count('А') == 1 and s.count('Л') == 1 and s.count('Ь') == 1:
                        if s[0] != 'Ь':
                            if 'ЬУ' not in s and 'ЬА' not in s:
                                ans +=1
print(ans)