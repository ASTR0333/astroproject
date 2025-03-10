ans = []
for n in range(10,1000):
    n2 = bin(n)[2:]
    if n2.count('1') % 2 == 0:
        n2 = n2 + n2[-2] + n2[-1]
    else:
        n2 = n2 + n2[-1] + n2[-2]
    r = int(n2,2)
    if r>154:
        ans.append(n)
print(min(ans))

