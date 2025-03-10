ans = []
def is_prime(n):
    if n <= 1:
        return 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 0
    return 1
for n in range(145,500):
    s = '0' + '1' * n + '2' * n + '0'
    s1 = s
    while '00' not in s:
        s = s.replace('02','101',1)
        s = s.replace('11', '2', 1)
        s = s.replace('12', '21', 1)
        s = s.replace('010', '00', 1)
    summ = s.count('1') + s.count('2') * 2
    if is_prime(summ) == 1 and '0' not in str(summ) and '2' not in str(summ) and '4' not in str(summ) and '6' not in str(summ) and '8' not in str(summ):
        ans.append(s1.count('1'))
print(min(ans))