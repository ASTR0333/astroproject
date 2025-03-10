for p1 in range(1,50):
    for p2 in range(1, 50):
        for p3 in range(1, 50):
            s = '0' + p1*'1' + p2 * '2' + p3 * '3' + '0'
            s1 = s
            while '00' not in s:
                s = s.replace('01','21022',1)
                s = s.replace('02', '310', 1)
                s = s.replace('03', '230112', 1)
            if s.count('1') == 96 and s.count('2') == 36 and s.count('3') == 80:
                print(len(s1))


