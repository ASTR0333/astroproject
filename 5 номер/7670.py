ans = []
for n in range(151,1000):
    n16 = hex(n)[2:]
    n16 = n16.replace('a', '1')
    k = 0
    for a in n16:
        if int(a,16) % 2 == 0:
            k+=1
    if k > 2:
        n16 = n16 + 'b'
    else:
        n16 = 'f' + n16
    r = int(n16,16)
    if r > 3500:
        ans.append([r,n])
print(min(ans))



