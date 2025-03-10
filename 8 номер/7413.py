n = 0
ans = 0
for p1 in 'АБОРСУЭ':
    for p2 in 'АБОРСУЭ':
        for p3 in 'АБОРСУЭ':
            for p4 in 'АБОРСУЭ':
                for p5 in 'АБОРСУЭ':
                    s = p1 + p2 + p3 + p4 + p5
                    n+=1
                    if s.count('Р')>=2 and s.count('У')==0 and n%2 == 0:
                        s = s.replace('А','*')
                        s = s.replace('Б','*')
                        s = s.replace('О','*')
                        s = s.replace('С','*')
                        s = s.replace('Э','*')
                        if 'Р*Р'in s :
                            ans+=1 
print(ans)
                            
                        
                        
                    