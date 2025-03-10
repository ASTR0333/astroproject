n = 0
for p1 in 'АПРСУ':
    for p2 in 'АПРСУ':
        for p3 in 'АПРСУ':
            s = p1 + p2 + p3
            n+=1
            if s[0] == 'Р':
                print(n)