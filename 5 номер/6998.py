ans = []
for n in range(1,1000):
    n2 = bin(n)[2:]
    if n2.count('1') % 2 == 0:
        n2 = '1' + n2 + '00'
    else:
        n2 = '11' + n2
    r = int(n2,2)
    if r >= 412:
        ans.append(n)
print(min(ans))
