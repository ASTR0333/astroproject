ans = 0
n = 0
for p1 in '1234567':    
    for p2 in '01234567': 
        for p3 in '01234567': 
            for p4 in '01234567': 
                for p5 in '01234567': 
                    for p6 in '01234567': 
                        s = p1 + p2 + p3 + p4 + p5 + p6
                        if s.count('3')==2 and '33' not in s:
                            q = s[s.find('3')+1:s.rfind('3')]
                            if '1' not in q and '2' not in q and '3' not in q and '0' not in q:
                                ans+=1
                                
                            
                            
                                
print(ans)
                        
                    