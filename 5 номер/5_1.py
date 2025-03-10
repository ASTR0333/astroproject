def to2(n):
    n2 = bin(n)[2:]
    n2 = n2 + bin(n%4)[2:]
    r = int(n2,2)
    return r

for left in range(1,1000):
    
    for right in range(left,65+left):




