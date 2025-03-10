ans = 0
n = 0
for p1 in 'УНЛИГБА':
    for p2 in 'УНЛИГБА':
        for p3 in 'УНЛИГБА':
            for p4 in 'УНЛИГБА':
                for p5 in 'УНЛИГБА':
                    for p6 in 'УНЛИГБА':
                        s = p1 + p2 + p3 + p4 + p5 + p6
                        n+=1
                        if n%2!=0:
                                s1=s
                                s1 = s1.replace('У', '*')
                                s1 = s1.replace('Н', '*')
                                s1 = s1.replace('Л', '*')
                                s1 = s1.replace('И', '*')
                                s1 = s1.replace('Г', '*')
                                s1 = s1.replace('Б', '*')
                                print(n,s1,s)
                                if 'А**А' in s1  and s.count('Н')>1:
                                    ans+=1
                                    print('ok')





print(ans)
