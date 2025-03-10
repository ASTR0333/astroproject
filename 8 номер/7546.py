ans = 0
for p1 in '123456789abbb':
    for p2 in '0123456789abbb':
        for p3 in '0123456789abbb':
            for p4 in '0123456789abbb':
                for p5 in '0123456789abbb':
                    s = p1 + p2 + p3 + p4 + p5
                    if s.count('9')==1 and s.count('b')<=3:
                        ans += 1
print(ans)