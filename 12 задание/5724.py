def is_prime(n):
    if n <= 1:
        return 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 0
    return 1


k=0
for n in range(10,100):
    s = '1' + '0'*n
    while '10' in s:
        if '10' in s:
            s = s.replace('10','001',1)
        if '1' in s:
            s = s.replace('1', '01', 1)
    if is_prime(len(s)) == 1:
        k+=1
print(k)


