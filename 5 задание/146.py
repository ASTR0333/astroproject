ans = []
for n in range(1,1000):
    n2 = bin(n)[2:]
    n2 = n2 + bin(n2.count('1')%2)[2:]
    n2 = n2 + bin(n2.count('1') % 2)[2:]
    r = int(n2,2)
    if r>180:
        ans.append(r)
print(min(ans))

