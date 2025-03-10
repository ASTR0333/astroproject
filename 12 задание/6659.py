ans = []
def is_prime(n):
    if n <= 1:
        return 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 0
    return 1
for n in range(1,100):
    s = '>' + '0'*21 + '1'*n + '2'*11
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1','22>',1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '1>', 1)
    summ = s.count('1') + s.count('2') * 2
    if summ%n==0 and is_prime(n)==1:
        ans.append(n)
print(min(ans))


