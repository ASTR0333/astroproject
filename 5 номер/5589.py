ans = []
for n in range(1,1000):
    n2 = bin(n)[2:]
    if len(n2) % 2 == 0:
        n2 = n2[:len(n2)//2] + '111' + n2[len(n2)//2:]
    else:
        n2 = '11' + n2[2:] + '1'
    r = int(n2,2)
    if r > 4000:
        ans.append(n)
print(min(ans))



