ans = 0
for p1 in '1234567':
    for p2 in '01234567':
        for p3 in '01234567':
            for p4 in '01234567':
                for p5 in '01234567':
                    for p6 in '01234567':
                        for p7 in '01234567':
                            for p8 in '01234567':
                                s = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8
                                if len(s) == len(set(s)):
                                    s = s.replace('2','0')
                                    s = s.replace('4', '0')
                                    s = s.replace('6', '0')

                                    s = s.replace('3', '1')
                                    s = s.replace('5', '1')
                                    s = s.replace('7', '1')
                                    if '00' not in s and '11' not in s:
                                        ans+=1
                                        
print(ans)





