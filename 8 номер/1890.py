ans = 0
for p1 in 'УЛЕЙ':
    for p2 in 'УЛЕЙ':
        for p3 in 'УЛЕЙ':
            for p4 in 'УЛЕЙ':
                s = p1 + p2 + p3 + p4
                if s.count('У') == 1 and s.count('Л') == 1 and s.count('Е') == 1 and s.count('Й') == 1:
                    if s[0] != 'Й':
                        if 'ЕУ' not in s:
                            ans += 1
print(ans)