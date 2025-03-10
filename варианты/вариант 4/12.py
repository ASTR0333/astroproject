for s in range(1,1000):
    a = '0' + '1'*s + '2'*s + '0'
    while '00' not in a:
        a = a.replace('011','20',1)
        a = a.replace('022', '10', 1)
        a = a.replace('01', '220', 1)
        a = a.replace('02', '110', 1)
        if a.count('1') == 40 and a.count('2')>50:
            print(a.count('2'))
            

