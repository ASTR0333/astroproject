ans = []
for n in range(4,100):
    n2 = bin(n)[2:]
    if n%3==0:
        n2 = n2 + n2[-3:]
    else:
        n2 = n2 + bin((n%3)*3)[2:]
    r = int(n2,2)
    if r < 68:
        ans.append(r)
print(max(ans))
