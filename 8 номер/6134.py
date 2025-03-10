ans = 0
for p1 in 'СВЯТОЛА':
    for p2 in 'СВЯТОЛА':
        for p3 in 'СВЯТОЛА':
            for p4 in 'СВЯТОЛА':
                for p5 in 'СВЯТОЛА':
                    for p6 in 'СВЯТОЛА':
                        for p7 in 'СВЯТОЛА':
                           s = p1 + p2 + p3 + p4 + p5 + p6 + p7
                           if s.count('Я') + s.count('О') + s.count('А') > s.count('С') + s.count('В') + s.count('Т') + s.count('Л'):
                               ans+=1
print(ans)



