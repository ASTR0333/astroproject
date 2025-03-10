k = 0
for p1 in 'ВЛТУ':
    for p2 in 'ВЛТУ':
        for p3 in 'ВЛТУ':
            for p4 in 'ВЛТУ':
                s = p1 + p2 + p3 + p4
                k+=1
                if k == 75:
                    print(s)