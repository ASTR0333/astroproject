ans=0
for n in range(1,1000):
    n2 = bin(n)[2:]
    if n2.count('1')%2==0:
        n2 = n2.replace(n2[0], '',1)
    else:
        n2 = n2.count('1')*'1'+'1'
    if n2.count('1')%2==0:
            n2 = n2.replace(n2[0], '', 1)
    else:
            n2 = n2.count('1')*'1'+'1'
    r=int(n2,2)
    if r==7:
        ans+=1
print(ans)