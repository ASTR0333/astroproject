k = 0
s = '1' * 38 + '2' * 34 + 30 * '3'
while '33' in s or '22' in s or '11' in s:
    if '33' in s:
        s = s.replace('33','12',1)
    if '11' in s:
        s = s.replace('11','32',1)
    if '22' in s:
        s = s.replace('22','31',1)
    summ = s.count('1') * 1 + s.count('2') * 2 + s.count('3') * 3
    if summ > k:
        k = summ
print(k)

