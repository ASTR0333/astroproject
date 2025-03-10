def summ(n):
    num = int(n)
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum



s = '121212'
while '12' in s:
    s = s.replace('12','4',1)
print(summ(s))






