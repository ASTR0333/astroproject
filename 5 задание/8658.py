k = 0
for n in range(1,100000):
    n8 = oct(n)[2:]
    if len(n8) >=2:
        if n % 7 == 0:
            n8 = n8 + n8[-2] + n8[-1]
        else:
            n8 = n8 + oct((n%7)*7)[2:]
        r = int(n8,8)
        if r<3000:
            k+=1
print(k)