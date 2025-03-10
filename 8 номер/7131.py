ans = 0
for p1 in '123456789ABC':
    for p2 in '0123456789ABC':
        for p3 in '0123456789ABC':
            for p4 in '0123456789ABC':
                for p5 in '0123456789ABC':
                    s = p1 + p2 + p3 + p4 + p5
                    if s.count('2')==1:
                        s = s.replace('1','*')
                        s = s.replace('3', '*')
                        s = s.replace('5', '*')
                        s = s.replace('7', '*')
                        s = s.replace('9', '*')
                        s = s.replace('B', '*')
                        s = s.replace('0', '+')
                        s = s.replace('2', '+')
                        s = s.replace('4', '+')
                        s = s.replace('6', '+')
                        s = s.replace('8', '+')
                        s = s.replace('A', '+')
                        s = s.replace('C', '+')
                        if '**' not  in s and '++' not in s:
                            ans+= 1
print(ans)
