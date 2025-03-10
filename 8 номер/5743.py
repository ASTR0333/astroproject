ans = 0
for p1 in '12345678':
    for p2 in '012345678':
        for p3 in '012345678':
            for p4 in '012345678':
                for p5 in '012345678':
                    for p6 in '012345678':
                        s = p1 + p2 +p3 + p4 + p5 + p6
                        summ = int(p1) + int(p2) + int(p3) + int(p4) + int(p5) + int(p6)
                        if s.count('1') + s.count('3') + s.count('5') + s.count('7') <= 2 and summ%6==0 and summ%4 != 0:
                            ans += 1
print(ans)