ans = []
for n in range(1,1000):
    n2 = bin(n)[2:]
    if n % 2 != 0:
        n2 = n2.replace('0','*')
        n2 = n2.replace('1', '0')
        n2 = n2.replace('*', '1')
    n2 = n2*2
    r2 = '1'*n2.count('1') + '0'*n2.count('0')
    r = int(r2,2)
    if r>60:
        ans.append(n)
print(min(ans))

