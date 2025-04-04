ans = []
for n in range(1,100):
    n2 = bin(n)[2:]
    n2 = n2 +str(n2.count('1')%2)
    n2 = n2 + str(n2.count('1') % 2)
    r = int(n2,2)
    if r>75:
        ans.append(r)
print(min(ans))


