ans = 0
for p1 in 'ОБЪЕМ':
    for p2 in 'ОБЪЕМ':
        for p3 in 'ОБЪЕМ':
            for p4 in 'ОБЪЕМ':
                s = p1+p2+p3+p4
                if s.count('О') == 1 and s[0] != 'Ъ' and s[-1] != 'Ъ':
                    ans +=1
print(ans)