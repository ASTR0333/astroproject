k = 0
for n in range(0,256):
    n2 = bin(n)[2:]
    n2 = '0' * (8-len(n2)) + n2

    n2 = n2.replace('1', '*')
    n2 = n2.replace('0', '1')
    n2 = n2.replace('*', '0')

    if int(n2, 2) % 5 == 0:
        n2 = '100' + n2[3:]
    else:
        n2 = '101' + n2[3:]
    r = int(n2,2)
    if r==180:
        k+=1
print(k)





