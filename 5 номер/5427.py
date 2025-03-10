ans = []
for i in range(10,1000):
    n = i - bin(i)[2:].count('0')
    n2 = bin(n)[2:]
    n2 =  n2[-3] + n2[-2] + n2[-1] + n2
    r = int(n2,2)
    if r> 224:
        ans.append(r)
print(min(ans))
