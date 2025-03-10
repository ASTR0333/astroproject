ans = 0
for p1 in '12':
    for p2 in '012':
        for p3 in '012':
            for p4 in '012':
                for p5 in '012':
                    for p6 in '012':
                        s = p1 + p2 + p3 + p4 + p5 + p6
                        if s.count('2') == 1:
                            if s.find('2') != 5:
                                if int(s[s.find('2')+1]) % 2 == 0:
                                    ans += 1
print(ans)

