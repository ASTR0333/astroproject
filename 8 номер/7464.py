ans = 0
for p1 in '12345678':
    for p2 in '012345678':
        for p3 in '012345678':
            for p4 in '012345678':
                for p5 in '012345678':
                    for p6 in '012345678':
                        s = p1 + p2 + p3 + p4 + p5 + p6
                        if s[0] not in '1357' and s[-1] != '2' and s[-1] != '3' and s.count('1') >= 2:
                            ans += 1
print(ans)