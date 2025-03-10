def is_prime(n):
    if n <= 1:
        return 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 0
    return 1

ans = []

for n in range(1,100):
    k=0
    s = '9' + '1'*n + '2'*n
    while '91' in s or '92' in s:
        k+=1
        if '91' in s:
            s = s.replace('91','39',1)
        if '92' in s:
            s = s.replace('92','59',1)
        if k>100:
            break

    summ = s.count('1') + s.count('2')*2 + s.count('3')*3 + s.count('5')*5 + s.count('9')*9
    if is_prime(summ)==1 and len(str(summ))==3:
        ans.append(n)
        print(n)
print(min(ans))
