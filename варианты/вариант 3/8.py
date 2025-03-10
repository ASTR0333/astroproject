def q(n):
    for i in range(len(n)-1):
        if not (((int(n[i])+int(n[i+1]))%2==0 and int(n[i+1])>int(n[i])) or ((int(n[i])+int(n[i+1]))%2!=0 and int(n[i+1])<int(n[i]))):
            return 0
    return 1



k = 0

for p1 in '012345678':
    for p2 in '012345678':
        for p3 in '012345678':
            for p4 in '012345678':
                for p5 in '012345678':
                    for p6 in '012345678':
                        for p7 in '012345678':
                            for p8 in '012345678':
                                for p9 in '012345678':
                                    for p10 in '012345678':
                                        for p11 in '012345678':
                                            for p12 in '012345678':
                                                s = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12
                                                if q(s):
                                                    k+=1
print(k)

