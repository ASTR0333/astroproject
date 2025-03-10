for p1 in 'АР':
    for p2 in 'АР':
        for p3 in 'АР':
            s = p1 + p2 + p3
            if s.count('А') == 2 and s.count('Р') == 1:
                print(s)
#1) 