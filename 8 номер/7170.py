k = 0
for p1 in 'БНПЭ':
    for p2 in 'БНПЭ':
        for p3 in 'БНПЭ':
            for p4 in 'БНПЭ':
                s = p1 + p2 + p3 + p4
                k+=1
                if k%2==0 and s[0] != 'П' and s[-1] != 'П' and 'ЭЭ' not in s:
                    print(k,s)